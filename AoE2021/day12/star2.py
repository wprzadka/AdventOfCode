import numpy as np


def create_graph(edges: list):
    graph = {a: [] for v in edges for a in v}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def is_visitable(visits_count: dict, v: str, extra_visit_available: bool) -> bool:
    if v.isupper():
        return True
    if visits_count[v] == 0:
        return True
    if visits_count[v] == 1:
        return extra_visit_available and v not in ['start', 'end']
    return False


def dfs(graph: dict, visited: dict, beg='start', path=None, extra_visit_available=True) -> int:
    if not path:
        path = []
    else:
        path = path.copy()
    path.append(beg)
    visited[beg] += 1
    if visited[beg] > 1 and beg.islower():
        extra_visit_available = False

    paths_to_end = 0
    for v in graph[beg]:
        if not is_visitable(visited, v, extra_visit_available):
            continue
        if v == 'end':
            print(path + ['end'])
            paths_to_end += 1
        else:
            paths_to_end += dfs(graph.copy(), visited.copy(), v, path, extra_visit_available)
    return paths_to_end


if __name__ == '__main__':
    with open('snd.txt') as f:
        edges = [v.rstrip().split('-') for v in f.readlines()]
    graph = create_graph(edges)
    visited = {v: 0 for v in graph.keys()}

    # visited['start'] = True
    print(dfs(graph, visited))
