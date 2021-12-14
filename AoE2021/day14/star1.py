if __name__ == '__main__':

    with open('fst.txt') as f:
        word = f.readline().rstrip()
        f.readline()
        pairs = [v.rstrip().split(' -> ') for v in f.readlines()]
    grammar = {a: b for a, b in pairs}
    print(word)
    print(grammar)

    for time in range(10):
        additions = ''
        for i, _ in enumerate(word[:-1]):
            additions += grammar[word[i: i+2]]
        new_word = ''
        for i, _ in enumerate(word[:-1]):
            new_word += word[i]
            new_word += additions[i]
        new_word += word[-1]
        word = new_word

    counted = [word.count(a) for a in set(word)]
    print(counted)
    max_repetitions = max(counted)
    min_repetitions = min(counted)
    print(max_repetitions - min_repetitions)
