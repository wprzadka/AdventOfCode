import numpy as np

if __name__ == '__main__':
    with open('snd.txt') as f:
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
    basins = np.zeros_like(height)

    sources = np.argwhere(is_low)
    visited = np.full_like(height, fill_value=False, dtype=bool)
    sizes = []
    for beg in sources:
        beg += [1, 1]
        curr_size = 1
        queue = [beg]
        visited[beg[0], beg[1]] = True
        while len(queue) > 0:
            x, y = queue.pop()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if height[nx, ny] < 9 and not visited[nx, ny]:
                    queue.append([nx, ny])
                    visited[nx, ny] = True
                    curr_size += 1
        sizes.append(curr_size)

    print(sorted(sizes, reverse=True))
    print(np.prod(sorted(sizes, reverse=True)[:3]))