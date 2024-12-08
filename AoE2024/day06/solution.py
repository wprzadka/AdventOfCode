if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()
    data = [list(x.strip()) for x in data]
    y = next(idx for idx, x in enumerate(data) if '^' in x)
    x = data[y].index('^')
    # print(x, y)

    width = len(data[0])
    heigh = len(data)
    count_visited = 1
    data[y][x] = 'X'
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    cur_dir = 0
    while 0 <= x < width and 0 <= y < heigh:
        dx, dy = dirs[cur_dir]
        if data[y][x] == '.':
            count_visited += 1
            data[y][x] = 'X'
        elif data[y][x] == '#':
            x, y = x - dx, y - dy
            cur_dir = (cur_dir + 1) % len(dirs)
            continue
        x, y = x + dx, y + dy

    # for r in data:
    #     print(r)

    """
['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']
['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#']
['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.']
['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.']
['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.']
['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.']
['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.']
['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.']
['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.']
['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']
41
    """

    print(count_visited)