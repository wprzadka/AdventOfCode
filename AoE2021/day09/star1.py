import numpy as np

if __name__ == '__main__':
    with open('fst.txt') as f:
        reads = np.array([[int(x) for x in v.rstrip()] for v in f.readlines()])
    height = np.full(reads.shape + np.array([2, 2], dtype=int), fill_value=reads.max() + 1)
    height[1:-1, 1:-1] = reads
    is_low = np.full_like(reads, fill_value=False, dtype=bool)
    x = 0
    while x < is_low.shape[0]:
        y = 0
        while y < is_low.shape[1]:
            nx, ny = x + 1, y + 1
            h = height[nx, ny]
            if h < height[nx - 1, ny] and h < height[nx + 1, ny] and\
               h < height[nx, ny - 1] and h < height[nx, ny + 1]:
                is_low[x, y] = True
            y += 1
        x += 1
    print(np.sum(height[1:-1, 1:-1][is_low] + 1))