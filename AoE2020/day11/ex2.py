from pprint import pprint


def countNeighbours(seats, y, x):
    count = 0

    # seats[y][x] = 'O'

    flag = 0
    d = 1
    while y + d < len(seats) and seats[y + d][x] != 'L':
        if seats[y + d][x] == '#':
            flag = 1
        # seats[y + d][x] = 'X'
        d += 1
    count += flag

    flag = 0
    d = -1
    while -1 < y + d and seats[y + d][x] != 'L':
        if seats[y + d][x] == '#':
            flag = 1
        # seats[y + d][x] = 'X'
        d -= 1
    count += flag

    flag = 0
    d = 1
    while x + d < len(seats[y]) and seats[y][x + d] != 'L':
        if seats[y][x + d] == '#':
            flag = 1
        # seats[y][x + d] = 'X'
        d += 1
    count += flag

    flag = 0
    d = -1
    while -1 < x + d and seats[y][x + d] != 'L':
        if seats[y][x + d] == '#':
            flag = 1
        # seats[y][x + d] = 'X'
        d -= 1
    count += flag

    flag = 0
    d = 1
    while (y + d) < len(seats) and (x + d) < len(seats[y + d]) and seats[y + d][x + d] != 'L':
        if seats[y + d][x + d] == '#':
            flag = 1
        # seats[y + d][x + d] = 'X'
        d += 1
    count += flag

    flag = 0
    d = -1
    while -1 < (y + d) and -1 < (x + d) and seats[y + d][x + d] != 'L':
        if seats[y + d][x + d] == '#':
            flag = 1
        # seats[y + d][x + d] = 'X'
        d -= 1
    count += flag

    flag = 0
    d = 1
    while -1 < (y + d) < len(seats) and -1 < (x - d) < len(seats[y + d]) \
            and seats[y + d][x - d] != 'L':
        if seats[y + d][x - d] == '#':
            flag = 1
        # seats[y + d][x - d] = 'X'
        d += 1
    count += flag

    flag = 0
    d = 1
    while -1 < (y - d) < len(seats) and -1 < (x + d) < len(seats[y - d]) \
            and seats[y - d][x + d] != 'L':
        if seats[y - d][x + d] == '#':
            flag = 1
        # seats[y - d][x + d] = 'X'
        d += 1
    count += flag

    return count


if __name__ == '__main__':
    with open('input.txt') as file:
        seats = file.readlines()
    seats = [row[:-1] for row in seats]

    lastTimeChanged = True
    while lastTimeChanged:
        lastTimeChanged = False
        nextStep = [[seat for seat in row] for row in seats]

        for y, row in enumerate(seats):
            for x, seat in enumerate(row):
                neighbours = countNeighbours(seats, y, x)

                if (seat == '#' and neighbours >= 5) or (seat == 'L' and neighbours == 0):
                    lastTimeChanged = True
                    nextStep[y][x] = '#' if seat == 'L' else 'L'
        seats = nextStep

    count = 0
    for row in seats:
        for seat in row:
            count += 1 if seat == '#' else 0

    print(count)
