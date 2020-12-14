if __name__ == '__main__':
    multiplied_count = 1
    for step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count = 0
        pos = 0
        with open('input.txt') as file:
            row = file.readline()
            while row != '':
                count += 1 if row[pos] == '#' else 0
                pos = (pos + step[0]) % (len(row) - 1)

                for _ in range(step[1]):
                    row = file.readline()

        multiplied_count *= count
    print(multiplied_count)