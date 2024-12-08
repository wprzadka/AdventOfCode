from itertools import combinations

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()
    data = [list(x.strip()) for x in data]

    antennas = {}
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == '.':
                continue
            if v not in antennas:
                antennas[v] = []
            antennas[v].append((x, y))
    
    height = len(data)
    width = len(data[0])

    print(antennas)

    for positions in antennas.values():
        if len(positions) < 2:
            continue
        
        for (ax, ay), (bx, by) in combinations(positions, 2):
            dx, dy = (bx - ax), (by - ay)
            nx, ny = bx, by
            while 0 <= nx < width and 0 <= ny < height:
                data[ny][nx] = '#'
                nx, ny = nx + dx, ny + dy
            nx, ny = bx, by
            while 0 <= nx < width and 0 <= ny < height:
                data[ny][nx] = '#'
                nx, ny = nx - dx, ny - dy

    for x in data:
        print(''.join(x))
    
    ant_count = sum([1 if x == '#' else 0 for row in data for x in row])
    print(ant_count)