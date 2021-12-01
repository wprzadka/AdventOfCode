if __name__ == '__main__':
    with open('fst.txt') as f:
        lines = [int(l) for l in f.readlines()]

    counter = sum([lines[i + 1] > val for i, val in enumerate(lines[:-1])])
    print(counter)  # 1581
