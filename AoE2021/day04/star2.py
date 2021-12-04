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
    with open('snd.txt') as f:
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

    won_boards = np.full(shape=tiles_num, fill_value=False, dtype=bool)
    boards_left = tiles_num
    last_number = None
    last_board = None

    for num in numbers:
        if boards_left == 0:
            break
        if num not in positions:
            continue
        for z, x, y in positions[num]:
            marks[z, x, y] = True
            if not won_boards[z] and check_bingo_locally(marks, (z, x, y)):
                last_number = num
                last_board = z
                won_boards[z] = True
                boards_left -= 1

    print(last_board)
    free_tiles_sum = np.sum(tiles[last_board][~marks[last_board]])
    print(last_number, free_tiles_sum)  # 20 451
    print(free_tiles_sum * last_number)  # 9020
