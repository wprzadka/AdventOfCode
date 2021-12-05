import numpy as np


def get_boundaries(coords: list):
    max_x, max_y = 0, 0
    for crd in coords:
        for x, y in crd:
            max_x = max(x, max_x)
            max_y = max(y, max_y)
    return max_x + 1, max_y + 1


if __name__ == '__main__':
    with open('snd.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    coords = [
        (
            tuple(int(x) for x in a.split(',')),
            tuple(int(x) for x in b.split(','))
        )
        for a, b in [v.split(' -> ') for v in lines]
    ]
    bounds = get_boundaries(coords)
    terrain = np.zeros(bounds, dtype=int)

    for (bx, by), (ex, ey) in coords:
        if bx == ex or by == ey:
            low_x, up_x = min(bx, ex), max(bx, ex)
            low_y, up_y = min(by, ey), max(by, ey)

            terrain[low_y:up_y+1, low_x:up_x+1] += 1
        else:
            dx = 1 if bx < ex else -1
            dy = 1 if by < ey else -1
            for x, y in zip(range(bx, ex + dx, dx), range(by, ey + dy, dy)):
                terrain[y, x] += 1
    print(terrain)
    print(np.sum(terrain > 1))