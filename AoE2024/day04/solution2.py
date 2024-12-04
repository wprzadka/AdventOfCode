def findAdjWord(data: list[list[str]], pos: tuple[int, int]) -> bool:
    key_len = 3
    cx, cy = pos
    ok_count = 0
    for dx, dy in ((1, -1), (1, 1)):
        nx, ny = cx - dx, cy - dy
        res = ''
        while len(res) < key_len:
            if not (0 <= ny < len(data) and 0 <= nx < len(data[0])):
                return False
            res += data[ny][nx]
            nx += dx
            ny += dy
        if res == 'MAS' or res == 'SAM':
            ok_count += 1
    return ok_count == 2

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    total_count = 0
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == 'A':
                total_count += findAdjWord(data, (c, r))
    print(total_count)