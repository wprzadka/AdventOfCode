import numpy as np


def check_bingo_locally(marks: np.ndarray, pos: tuple) -> [int]:
    z, x, y = pos
    return all(marks[z, x, :]) or all(marks[z, :, y])


def create_map(tiles: np.ndarray) -> dict:
    positions = {}
    for z, tile in enumerate(tiles):
        for x, col in enumerate(tile):
            for y, val in enumerate(col):
                if val not in positions:
                    positions[val] = []
                positions[val].append((z, x, y))
    return positions


if __name__ == '__main__':
    tile_size = 5
    with open('fst.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    tiles_num = (len(lines) - 1) // (tile_size + 1)
    numbers = [int(v) for v in lines[0].split(',')]
    tiles = np.empty((tiles_num, tile_size, tile_size), dtype=int)
    marks = np.full_like(tiles, fill_value=False, dtype=bool)
    for i, _ in enumerate(tiles):
        tiles[i] = np.array([
            [int(num) for num in row.split()]
            for row in lines[i * (tile_size + 1) + 2: i * (tile_size + 1) + 2 + tile_size]
        ])
    positions = create_map(tiles)

    last_number = 0
    won_tile = None
    for num in numbers:
        if won_tile:
            break
        if num not in positions:
            continue
        for z, x, y in positions[num]:
            marks[z, x, y] = True
            if check_bingo_locally(marks, (z, x, y)):
                last_number = num
                won_tile = z
                break
    free_tiles_sum = np.sum(tiles[won_tile][~marks[won_tile]])
    print(last_number, free_tiles_sum)  # 96 662
    print(free_tiles_sum * last_number)  # 63552
