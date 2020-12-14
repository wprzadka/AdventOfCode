
if __name__ == '__main__':
    with open('input.txt') as file:
        input = [int(x, 10) for x in file.readlines()]

    ordered = sorted(input)
    # print(ordered)
    diffs = [ordered[idx] - val for idx, val in enumerate(ordered[:-1], 1)]
    # print(diffs)
    x = 1
    y = 1
    for elem in diffs:
        if elem == 1:
            x += 1
        else:
            y += 1
    print(x, y, x * y)