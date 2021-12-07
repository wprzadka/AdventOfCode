import numpy as np


if __name__ == '__main__':
    with open('snd.txt') as f:
        positions = np.array([int(v) for v in f.readline().split(',')])
    beg = np.min(positions)
    end = np.max(positions)

    min_fuel = (end - beg) * 2**32
    for p in range(beg, end + 1):
        steps = np.abs(p - positions)
        costs = np.array([sum(range(i + 1)) for i in steps])
        min_fuel = min(min_fuel, np.sum(costs))
    print(min_fuel)
