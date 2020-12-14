if __name__ == '__main__':
    count = 0
    pos = 0
    with open('input.txt') as file:
        row = file.readline()
        while row != '':

            count += 1 if row[pos] == '#' else 0
            # print(row, end='')
            # print(pos)
            # print(f"{row[:pos]} {'X' if row[pos] == '#' else 'O'} {row[pos + 1:]}")
            pos = (pos + 3) % (len(row) - 1)

            row = file.readline()
    print(count)