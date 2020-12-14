if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()

    rows = [(x[0], int(x[1:], 10)) for x in input]

    state = {'N': 0, 'E': 0, 'S': 0, 'W': 0, 'R': 90}
    rotations = [(0, 'N'), (90, 'E'), (180, 'S'), (270, 'W')]

    for row in rows:
        if row[0] in ['N', 'E', 'S', 'W']:
            state[row[0]] += row[1]
        elif row[0] == 'R':
            state['R'] = (state['R'] + row[1]) % 360
        elif row[0] == 'L':
            ambient = (state['R'] - row[1])
            state['R'] = ambient if ambient >= 0 else ambient + 360
        elif row[0] == 'F':
            for rotate in rotations:
                if rotate[0] == state['R']:
                    state[rotate[1]] += row[1]
        else:
            print('wrong input: ', row[0])

    x, y = abs(state['N'] - state['S']), abs(state['E'] - state['W'])
    print(x + y)