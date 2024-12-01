from collections import Counter

if __name__ == '__main__':
    with open('AoE2024/day01/input.txt') as f_in:
        data = f_in.readlines()

    pairs = [x.split() for x in data]

    fst = sorted([int(p[0]) for p in pairs])
    snd = sorted([int(p[1]) for p in pairs])
    total_diff = sum(abs(f - s) for f, s in zip(fst, snd))
    print(total_diff)

    snd_counter = Counter(snd)
    similarity = sum([x * snd_counter[x] for x in fst])
    print(similarity)