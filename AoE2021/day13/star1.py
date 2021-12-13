def print_grid(points: set):
    max_x = max([x for x, _ in points])
    max_y = max([y for _, y in points])
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in points:
        grid[y][x] = '#'
    for row in grid:
        print(row)


if __name__ == '__main__':

    dots = set()
    folds = []
    with open('fst.txt') as f:
        line = f.readline()
        while line != '\n':
            dots.add(tuple(int(v) for v in line.rstrip().split(',')))
            line = f.readline()

        line = f.readline()
        while line:
            a, b = line.split('=')
            folds.append((a[-1], int(b.rstrip())))
            line = f.readline()
    print(dots)
    print(folds)

    axis, val = folds[0]

    if axis == 'x':
        dots = {(2*val - x, y) if x > val else (x, y) for x, y in dots}
    else:
        dots = {(x, 2*val - y) if y > val else (x, y) for x, y in dots}

    print(len(dots))
    # print_grid(dots)
