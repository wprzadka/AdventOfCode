from pprint import pprint


def count_neighbours(tiles, pos):
    cx, cy, cz, cw = pos
    count = 0

    for w, dim in enumerate(tiles[cw-1:cw+2]):
        for z, lvl in enumerate(dim[cz-1:cz+2]):
            for y, row in enumerate(lvl[cy-1:cy+2]):
                for x, val in enumerate(row[cx-1:cx+2]):
                    if (x, y, z, w) != (1, 1, 1, 1) and val == '#':
                        count += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [row[:-1] for row in data]
    space = range(21)
    center = 9
    tiles = [[[['.' for _ in space] for _ in space] for _ in space]for _ in space]
    for row_idx, row in enumerate(data):
        for idx, val in enumerate(row):
            tiles[center][center][center + row_idx][center + idx] = val

    # pprint(tiles[center][center])

    for t in range(6):
        new_tiles = [[[['.' for _ in space] for _ in space] for _ in space] for _ in space]
        for w, dimention in enumerate(tiles):
            for z, level in enumerate(dimention):
                for y, row in enumerate(level):
                    for x, elem in enumerate(row):
                        neighbours = count_neighbours(tiles=tiles, pos=(x, y, z, w))
                        if elem == '#' and neighbours in [2, 3] or elem == '.' and neighbours == 3:
                            new_tiles[w][z][y][x] = '#'
        tiles = new_tiles

    count = 0
    for z, dimention in enumerate(tiles):
        for z, level in enumerate(dimention):
            for y, row in enumerate(level):
                for x, elem in enumerate(row):
                    if elem == '#':
                        count += 1
    print(count)