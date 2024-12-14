from functools import reduce
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

    end_pos = [(p + v * 100) % size for p, v in zip(pos, vel)]

    # temp = [[0 for _ in range(width)] for _ in range(height)]
    # for x, y in end_pos:
    #     temp[y][x] += 1
    # for r in temp:
    #     print(r)

    quarters = [0, 0, 0, 0]
    mid_point = size // 2
    for p in end_pos:
        if any(p == mid_point):
            continue
        gt = (p > mid_point)
        quarters[(gt[0] << 1) + gt[1]] += 1
    print(quarters)
    res = reduce(lambda a, b: a * b, quarters)
    print(res)
