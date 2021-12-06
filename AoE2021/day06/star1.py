import numpy as np


if __name__ == '__main__':
    with open('fst.txt') as f:
        read = f.readline()
    fishes = np.array([int(v) for v in read.split(',')])

    day = 0
    while day < 80:
        fishes -= 1
        created = fishes < 0
        fishes[created] = 6
        fishes = np.concatenate((fishes, np.full(np.sum(created), fill_value=8)))
        day += 1
    print(fishes.size)