if __name__ == '__main__':
    with open('snd.txt') as f:
        lines = [(a, int(b)) for a, b in [line.split() for line in f.readlines()]]
    horizontal, depth, aim = 0, 0, 0
    for move, value in lines:
        if move == 'forward':
            horizontal += value
            depth += aim * value
        elif move == 'up':
            aim -= value
        elif move == 'down':
            aim += value
        else:
            raise 'No such command error'

    print(horizontal * depth)
