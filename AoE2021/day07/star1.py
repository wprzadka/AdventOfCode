import numpy as np


if __name__ == '__main__':
    with open('fst.txt') as f:
        positions = np.array([int(v) for v in f.readline().split(',')])
    beg = np.min(positions)
    end = np.max(positions)

    min_fuel = (end - beg) * positions.size
    for p in range(beg, end + 1):
        min_fuel = min(min_fuel, np.sum(np.abs(p - positions)))
    print(min_fuel)