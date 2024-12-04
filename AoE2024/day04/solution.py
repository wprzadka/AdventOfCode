def findAdjWord(data: list[list[str]], pos: tuple[int, int]) -> int:
    key = 'XMAS'
    counter = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            nx, ny = pos
            idx = 0
            while idx < len(key):
                if not (0 <= ny < len(data) and 0 <= nx < len(data[0])):
                    break
                if data[ny][nx] != key[idx]:
                    break
                idx += 1
                nx += dx
                ny += dy
            if idx == len(key):
                counter += 1
    return counter

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    total_count = 0
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == 'X':
                total_count += findAdjWord(data, (c, r))
    print(total_count)