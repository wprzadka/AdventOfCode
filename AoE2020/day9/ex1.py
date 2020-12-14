
if __name__ == '__main__':
    interval = 25
    with open('input.txt') as file:
        row = file.readlines()
    values = [int(v) for v in row[:-1]]

    for idx, val in enumerate(values[25:], 25):
        sums_flag = False

        for y in range(1, interval + 1):
            for x in range(1, interval + 1):
                if x != y and val == values[idx - y] + values[idx - x]:
                    sums_flag = True
                    break

        if not sums_flag:
            print(val)
            break