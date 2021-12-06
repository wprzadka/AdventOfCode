if __name__ == '__main__':
    with open('snd.txt') as f:
        read = [int(v) for v in f.readline().split(',')]
    fishes = [read.count(i) for i in range(9)]

    day = 0
    while day < 256:
        created = fishes[0]
        for i, v in enumerate(fishes[1:]):
            fishes[i] = v
        fishes[8] = created
        fishes[6] += created
        day += 1
    print(sum(fishes))
