import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    sep = data.index('\n')

    terrain = np.array([list(x.strip().replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for x in data[:sep]])
    moves = ''.join((x.strip() for x in data[sep + 1:]))

    print('\n'.join(''.join(row) for row in terrain))
    print(moves)

    y = [y for y, row in enumerate(terrain) if '@' in row].pop()
    x = np.where(terrain[y] == '@')[0][0]
    rob_pos = np.array([y, x])
    print(rob_pos)

    dirs_map = {'^': np.array([-1, 0]), '>': np.array([0, 1]), 'v': np.array([1, 0]), '<': np.array([0, -1])}
    def neighbour(pos: np.ndarray) -> np.ndarray: 
        return pos + np.array([0, 1 if terrain[*pos] == '[' else -1])
            
    for m in moves:
        direction = dirs_map[m]
        print(m)
        
        new_pos = rob_pos + direction
        elem = terrain[*new_pos]
        
        if elem == '#':
            continue
        elif elem == '.':
            terrain[*rob_pos] = '.'
            terrain[*new_pos] = '@'
            rob_pos = new_pos
        elif elem in '[]':
            moved_parts = set([tuple(x) for x in (rob_pos, new_pos, neighbour(new_pos))])
            expanded = [np.array(x) + direction for x in moved_parts]
            new_expanded = True
            while new_expanded and '#' not in (terrain[*x] for x in expanded):
                new_expanded = False
                for x in expanded:
                    if terrain[*x] in '[]' and tuple(x) not in moved_parts:
                        new_expanded = True
                        moved_parts.add(tuple(x))
                        moved_parts.add(tuple(neighbour(x)))
                expanded = [np.array(x) + direction for x in moved_parts]
            
            if '#' in (terrain[*x] for x in expanded):
                continue
            
            vals_copy = [(pos, terrain[*pos]) for pos in moved_parts]
            for pos, val in vals_copy:
                terrain[*pos] = '.'
            for pos, val in vals_copy:
                terrain[*(pos + direction)] = val

            rob_pos = new_pos

    print('\n'.join(''.join(row) for row in terrain))
        
    total_coords = 0
    for y, row in enumerate(terrain):
        for x, val in enumerate(row):
            if val != '[':
                continue
            total_coords += y * 100 + x

    print(total_coords)
