import numpy as np


def flash(energy: np.ndarray) -> int:
    count = 0
    for x in range(energy.shape[0]):
        for y in range(energy.shape[1]):
            if energy[x, y] <= 9:
                continue
            count += 1
            energy[max(x - 1, 0):x + 2, max(y - 1, 0):y + 2] += 1
            energy[x, y] = -100
    return count


if __name__ == '__main__':
    with open('fst.txt') as f:
        energy = np.array([[int(x) for x in v.rstrip()] for v in f.readlines()])

    step = 0
    flashes_count = 0
    # print(energy, end='\n\n')
    while step < 100:
        step += 1
        energy += 1
        while energy.max() > 9:
            flashes_count += flash(energy)
        energy[energy < 0] = 0
        # print(energy, end='\n\n')

    print(flashes_count)
