def countNeighbours(seats, y, x):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if -1 < (y + dy) < len(seats) and -1 < (x + dx) < len(seats[y + dy]) and (dx != 0 or dy != 0):
                count += 1 if seats[y + dy][x + dx] == '#' else 0
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
                if (seat == '#' and neighbours >= 4) or (seat == 'L' and neighbours == 0):
                    lastTimeChanged = True
                    nextStep[y][x] = '#' if seat == 'L' else 'L'
        seats = nextStep

    count = 0
    for row in seats:
        for seat in row:
            count += 1 if seat == '#' else 0
    print(count)