import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    sep = data.index('\n')

    terrain = np.array([list(x.strip()) for x in data[:sep]])
    moves = ''.join((x.strip() for x in data[sep + 1:]))

    print(terrain)
    print(moves)

    y = [y for y, row in enumerate(terrain) if '@' in row].pop()
    x = np.where(terrain[y] == '@')[0][0]
    rob_pos = np.array([y, x])
    print(rob_pos)

    dirs_map = {'^': np.array([-1, 0]), '>': np.array([0, 1]), 'v': np.array([1, 0]), '<': np.array([0, -1])}
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
        elif elem == 'O':  
            changed = ['@']
            while elem == 'O':
                changed.append(elem)
                new_pos += direction
                elem = terrain[*new_pos]
            changed.append(terrain[*new_pos])
            new_pos += direction                
            changed = sorted(changed, key=['.', '@', 'O', '#'].index)            
            new_rob_pos = rob_pos + direction * changed.index('@')
            x = rob_pos.copy()
            idx = 0
            while any(x != new_pos):
                terrain[*x] = changed[idx]
                idx += 1
                x += direction
            rob_pos = new_rob_pos
        
        print(terrain)
        
    total_coords = 0
    for y, row in enumerate(terrain):
        for x, val in enumerate(row):
            if val != 'O':
                continue
            total_coords += y * 100 + x

    print(total_coords)
