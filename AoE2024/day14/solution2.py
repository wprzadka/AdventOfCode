import os
import re
import numpy as np

if __name__ == '__main__':
    with open('input.txt', encoding='utf-8') as f_in:
        data = f_in.readlines()

    width = 101  # 101 11
    height = 103  # 103 7
    size = np.array([width, height])

    pos = []
    vel = []
    for row in data:
        match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', row)
        assert match
        pos.append(np.array([int(x) for x in match.group(1, 2)]))
        vel.append(np.array([int(x) for x in match.group(3, 4)]))

    idx = 0
    max_diags = 0
    while True:
        idx += 1

        pos = [(p + v) % size for p, v in zip(pos, vel)]
        temp = [[0 for _ in range(width)] for _ in range(height)]
        for x, y in pos:
            temp[y][x] += 1

        diags = 0
        for y, row in enumerate(temp):
            for x, c in enumerate(row):
                if c == 0:
                    continue
                for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height and temp[ny][nx] > 0:
                        diags += 1

        if diags > max_diags:
            max_diags = diags

            for r in temp:
                print(''.join([str(x) for x in r]).replace('0', '.'))
            print(idx)
            os.system('cls')

# .........................................1...................1........1..............................
# .....................................................................................................
# .......................1111111111111111111111111111111..1..1.........................................
# .......................1.............................1.........1....1............................1...
# .......................1.............................1...............................................
# .......................1.............................1........................1......................
# .......................1.............................1..........................1....................
# .......................1..............1..............1...............................................
# .......................1.............111.............1..........1......................1.............
# .1...1.................1............11111............1.....................................1.........
# .......................1...........1111111...........1...............................................
# .......................1..........111111111..........1...............................................
# ......1................1............11111............1.....1....................1....................
# .......................1...........1111111...........1...................................1...........
# .1.....................1..........111111111..........1.............................1.................
# .......................1.........11111111111.........1..........1............1....................1..
# .......................1........1111111111111........1...1...........................................
# .........1.............1..........111111111..........1...............................................
# .......1.....1.........1.........11111111111.........1...............................................
# .......................1........1111111111111........1..1....................................1.......
# ....................1..1.......111111111111111.......1...............................................
# .......................1......11111111111111111......1...1...........................................
# .......................1........1111111111111........1.............1............................1....
# .......................1.......111111111111111.......1...............................................
# .....................1.1......11111111111111111......1..............................1.......1........
# .......................1.....1111111111111111111.....1......................1............1...........
# ......1................1....111111111111111111111....1...............................................
# .......................1.............111.............1...........1...................................
# .......................1.............111.............1...............................................
# .......................1.............111.............1...............................................
# .......................1.............................1........................1......................
# .......................1.............................1...............1...............................
# .......................1.............................1...............................................
# .......................1.............................1...............................................
# .......................1111111111111111111111111111111...............................1...........1...
# ................1....................................................................................

