if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()
    data = [list(x.strip()) for x in data]

    width = len(data[0])
    heigh = len(data)

    init_y = next(idx for idx, x in enumerate(data) if '^' in x)
    init_x = data[init_y].index('^')
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    def check_loop(new_obs: tuple[int, int]) -> bool:
        x, y = init_x, init_y
        visited = set()
        cur_dir = 0
        while 0 <= x < width and 0 <= y < heigh:
            dx, dy = dirs[cur_dir]
            if data[y][x] == '#' or (x, y) == new_obs:
                x, y = x - dx, y - dy

                if (x, y, cur_dir) in visited:
                    return True
                visited.add((x, y, cur_dir))

                cur_dir = (cur_dir + 1) % len(dirs)
                continue
            x, y = x + dx, y + dy
        return False
    
    possible_new_obs = sum((check_loop((x, y)) for y, row in enumerate(data) for x, _ in enumerate(row)))
    print(possible_new_obs)