if __name__ == '__main__':
    with open('fst.txt') as f:
        lines = [(a, int(b)) for a, b in [line.split() for line in f.readlines()]]
    horizontal, depth = 0, 0
    for move, value in lines:
        if move == 'forward':
            horizontal += value
        elif move == 'up':
            depth -= value
        elif move == 'down':
            depth += value
        else:
            raise 'No such command error'

    print(horizontal * depth)
