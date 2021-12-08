if __name__ == '__main__':

    with open('fst.txt') as f:
        digits = [v.split('|')[1].strip().split() for v in f.readlines()]
    print(sum([sum([len(v) in (2, 3, 4, 7) for v in row]) for row in digits]))
