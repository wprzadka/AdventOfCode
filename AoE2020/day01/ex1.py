if __name__ == '__main__':
    values = []
    with open('input.txt') as file:
        row = file.readline()
        while row != '':
            values.append(int(row, 10))
            row = file.readline()
    results = []
    for y_idx, y in enumerate(values):
        for x_idx, x in enumerate(values):
            if x_idx != y_idx and x + y == 2020:
                results.append(x * y)
    for x in results:
        print(x)
