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


if __name__ == '__main__':

    with open('fst.txt') as f:
        grid = np.array([[int(a) for a in v.rstrip()] for v in f.readlines()])
    print(grid)
    costs = search(grid)
    print(costs)
