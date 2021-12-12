import numpy as np


def create_graph(edges: list):
    graph = {a: [] for v in edges for a in v}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(graph: dict, visited: dict, beg='start', path=None) -> int:
    if not path:
        path = []
    else:
        path = path.copy()
    path.append(beg)
    visited[beg] = True

    paths_to_end = 0
    for v in graph[beg]:
        if visited[v] and v.islower():
            continue
        # visited[v] = True
        if v == 'end':
            print(path + ['end'])
            paths_to_end += 1
        else:
            paths_to_end += dfs(graph.copy(), visited.copy(), v, path)
    return paths_to_end


if __name__ == '__main__':
    with open('fst.txt') as f:
        edges = [v.rstrip().split('-') for v in f.readlines()]
    graph = create_graph(edges)
    visited = {v: False for v in graph.keys()}

    # visited['start'] = True
    print(dfs(graph, visited))
