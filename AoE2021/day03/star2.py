from typing import Callable


def most_common(words: list, pos: int) -> chr:
    counter = {'0': 0, '1': 0}
    for bit in [w[pos] for w in words]:
        counter[bit] += 1
    return '1' if counter['1'] >= counter['0'] else '0'


def least_common(words: list, pos: int) -> chr:
    return '1' if most_common(words, pos) == '0' else '0'


def get_diagnostic_value(words: list, criteria: Callable[[list, int], str]):
    idx = 0
    while idx < len(lines[0]) - 1 and len(words) > 1:
        c_value = criteria(words, idx)
        words = [w for w in words if w[idx] == c_value]
        idx += 1
    return words[0]


if __name__ == '__main__':
    with open('snd.txt') as f:
        lines = f.readlines()

    oxygen = get_diagnostic_value([v.rstrip() for v in lines], most_common)
    co2 = get_diagnostic_value([v.rstrip() for v in lines], least_common)

    print(oxygen, co2)
    print(int(oxygen, 2) * int(co2, 2))  # 4474944
