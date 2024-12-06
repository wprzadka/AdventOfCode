if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    sep = data.index('\n')

    rules = {}
    for x in data[:sep]:
        a, b = x.strip().split('|')
        if a not in rules:
            rules[a] = []
        rules[a].append(b)

    pages = [[v for v in x.strip().split(',')] for x in data[sep + 1:]]

    total = 0
    for row in pages:

        is_ok = True
        for fst_idx, fst in enumerate(row):
            for snd in row[fst_idx + 1:]:
                if snd in rules and fst in rules[snd]:
                    is_ok = False
                    break
        if is_ok:
            continue

        while not is_ok:
            is_ok = True
            for fst_idx, _ in enumerate(row):
                for snd_idx, _ in enumerate(row[fst_idx + 1:], fst_idx + 1):
                    if row[snd_idx] in rules and row[fst_idx] in rules[row[snd_idx]]:
                        is_ok = False
                        temp = row[fst_idx]
                        row[fst_idx] = row[snd_idx]
                        row[snd_idx] = temp
        if is_ok:
            total += int(row[len(row) // 2])
    print(total)
