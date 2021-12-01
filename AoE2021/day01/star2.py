if __name__ == '__main__':
    with open('snd.txt') as f:
        lines = [int(l.split(' ')[0]) for l in f.readlines()]

    sums = [sum(lines[i:i+3]) for i, _ in enumerate(lines)]
    counter = sum([sums[i + 1] > val for i, val in enumerate(sums[:-1])])
    print(counter)
