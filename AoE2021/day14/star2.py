if __name__ == '__main__':

    with open('snd.txt') as f:
        word = f.readline().rstrip()
        f.readline()
        pairs = [v.rstrip().split(' -> ') for v in f.readlines()]
    grammar = {a: b for a, b in pairs}
    encoded = {}
    for i, _ in enumerate(word[:-1]):
        if word[i:i+2] not in encoded:
            encoded[word[i:i+2]] = 0
        encoded[word[i:i+2]] += 1
    print(encoded)

    for i in range(40):
        new_enc = {}
        for w, num in encoded.items():
            x = grammar[w]
            for nw in (w[0]+x, x+w[1]):
                if nw not in new_enc:
                    new_enc[nw] = 0
                new_enc[nw] += num
        print(new_enc)
        encoded = new_enc

    symbols = {a: 0 for w in encoded.keys() for a in w}
    for (a, b), num in encoded.items():
        symbols[a] += num
        symbols[b] += num

    symbols[word[0]] += 1
    symbols[word[-1]] += 1
    for v in symbols.keys():
        symbols[v] //= 2
    print(symbols)

    max_repetitions = max(symbols.values())
    min_repetitions = min(symbols.values())
    print(max_repetitions - min_repetitions)
