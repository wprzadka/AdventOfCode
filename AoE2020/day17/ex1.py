from pprint import pprint


def count_neighbours(tiles, pos):
    cx, cy, cz = pos
    count = 0
    for z, lvl in enumerate(tiles[cz-1:cz+2]):
        for y, row in enumerate(lvl[cy-1:cy+2]):
            for x, val in enumerate(row[cx-1:cx+2]):
                if (x, y, z) != (1, 1, 1) and val == '#':
                    count += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [row[:-1] for row in data]
    space = range(21)
    center = 9
    tiles = [[['.' for _ in space] for _ in space] for _ in space]
    for row_idx, row in enumerate(data):
        for idx, val in enumerate(row):
            tiles[center + 0][center + row_idx][center + idx] = val

    pprint(tiles[center])

    for t in range(6):
        new_tiles = [[['.' for _ in space] for _ in space] for _ in space]
        for z, level in enumerate(tiles):
            for y, row in enumerate(level):
                for x, elem in enumerate(row):
                    neighbours = count_neighbours(tiles=tiles, pos=(x, y, z))
                    if elem == '#' and neighbours in [2, 3] or elem == '.' and neighbours == 3:
                        new_tiles[z][y][x] = '#'
        tiles = new_tiles

    count = 0
    for z, level in enumerate(tiles):
        for y, row in enumerate(level):
            for x, elem in enumerate(row):
                if elem == '#':
                    count += 1
    print(count)