import numpy as np


def search(graph: np.ndarray) -> np.ndarray:
    costs = np.full_like(graph, fill_value=-1)
    costs[0, 0] = 0
    queue = [((0, 0), 0)]
    while len(queue) > 0:
        queue.sort(key=lambda ent: ent[1])
        (x, y), cost = queue.pop(0)
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if not 0 <= nx < graph.shape[0] or not 0 <= ny < graph.shape[1]:
                continue
            if costs[nx, ny] != -1:
                continue
            costs[nx, ny] = cost + graph[nx, ny]

            on_queue = False
            for i, ((qx, qy), old_cost) in enumerate(queue):
                if nx != qx or ny != qy:
                    continue
                on_queue = True
                queue[i] = (qx, qy), min(old_cost, costs[nx, ny])
                break
            if not on_queue:
                queue.append(((nx, ny), costs[nx, ny]))
    return costs


def create_grid(smaller: np.ndarray) -> np.ndarray:
    bigger = np.empty((small_grid.shape[0] * 5, small_grid.shape[1] * 5), dtype=int)

    size_x, size_y = smaller.shape
    for tile_x in range(5):
        for tile_y in range(5):
            for x in range(size_x):
                for y in range(size_y):
                    bigger[x + tile_x * size_x, y + tile_y * size_y] =\
                        (smaller[x, y] + tile_x + tile_y) % 10 + (smaller[x, y] + tile_x + tile_y) // 10
    return bigger


if __name__ == '__main__':

    with open('snd.txt') as f:
        small_grid = np.array([[int(a) for a in v.rstrip()] for v in f.readlines()], dtype=int)
    big_grid = create_grid(small_grid)
    # for row in big_grid:
    #     for i in range(5):
    #         print(row[i * small_grid.shape[0]: (i+1) * small_grid.shape[0]])
    #     print()
    costs = search(big_grid)
    print(costs)
