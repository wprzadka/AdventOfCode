if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()

    rows = [(x[0], int(x[1:], 10)) for x in input]

    state = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
    # rotations = [(0, 'N'), (90, 'E'), (180, 'S'), (270, 'W')]

    op_idx = 0
    for row in rows:
        print(op_idx, ':')
        y, x = abs(state['N'] - state['S']), abs(state['E'] - state['W'])
        print(x, y)
        print(waypoint)
        op_idx += 1

        if row[0] in ['N', 'E', 'S', 'W']:
            waypoint[row[0]] += row[1]
        elif row[0] in ['R', 'L']:
            step = row[1] // 90
            if row[0] == 'R':
                # reverse order -> we take value from (idx + step)
                step *= -1
            print('step: ', step)
            new_waypoint = {}
            vals = list(waypoint.values())
            for idx, key in enumerate(waypoint.keys()):
                try:
                    # next = idx + step
                    # next = next % 4 if next >= 0 else next + 4
                    new_waypoint[key] = vals[(idx + step) % 4]
                except IndexError:
                    print(next)
                    print(vals)
            waypoint = new_waypoint
            print(waypoint)

        elif row[0] == 'F':
            for key, val in waypoint.items():
                state[key] += row[1] * val
        else:
            print('wrong input: ', row[0])

    y, x = abs(state['N'] - state['S']), abs(state['E'] - state['W'])
    print(x, y)
    print(waypoint)
    print(x + y)