#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def get_number_of_segments():
    patterns = [
        'abcefg',
        'cf',
        'acdeg',
        'acdfg',
        'bcdf',
        'abdfg',
        'abdefg',
        'acf',
        'abcdefg',
        'abcdfg'
    ]
    num_lens = {}
    for i, v in enumerate(patterns):
        if len(v) not in num_lens:
            num_lens[len(v)] = []
        num_lens[len(v)].append(i)
    return num_lens


if __name__ == '__main__':

    print(get_number_of_segments())

    with open('snd.txt') as f:
        writes = [v.split(' | ') for v in f.readlines()]
        signals = [(v[0].split(), v[1].strip().split()) for v in writes]

    outputs = []
    for patterns, digits in signals:
        segments = {
            'up': '',
            'left': '',
            'right': '',
            'mid': '',
            'down': '',
            'right_up': '',
            'right_down': '',
            'left_up': '',
            'left_down': ''
        }
        get_with_len = lambda x: [seg for seg in patterns if len(seg) == x]
        numbers = ['' for _ in range(10)]
        numbers[8] = get_with_len(7)[0]

        # get right segment with "one"
        numbers[1] = get_with_len(2)[0]
        segments['right'] = numbers[1]

        # find up segment with "seven"
        numbers[7] = get_with_len(3)[0]
        segments['up'] = [v for v in numbers[7] if v not in numbers[1]][0]

        numbers[6] = [seg for seg in get_with_len(6) if sum([v in segments['right'] for v in seg]) == 1][0]
        segments['right_down'] = [v for v in segments['right'] if v in numbers[6]][0]
        segments['right_up'] = [v for v in segments['right'] if v not in numbers[6]][0]

        numbers[3] = [seg for seg in get_with_len(5)
                      if segments['right_down'] in seg
                      and segments['right_up'] in seg][0]
        numbers[5] = [seg for seg in get_with_len(5)
                      if segments['right_down'] in seg
                      and segments['right_up'] not in seg][0]
        numbers[2] = [seg for seg in get_with_len(5)
                      if segments['right_down'] not in seg
                      and segments['right_up'] in seg][0]
        numbers[4] = get_with_len(4)[0]
        numbers[9] = [seg for seg in get_with_len(6) if sum([v in numbers[4] for v in seg]) == 4][0]
        numbers[0] = [seg for seg in get_with_len(6) if seg != numbers[6] and seg != numbers[9]][0]

        numbers = [set(n) for n in numbers]
        digits = [set(d) for d in digits]
        out = []
        for dig in digits:
            for i, num in enumerate(numbers):
                if num == dig:
                    out.append(str(i))
                    break
        outputs.append(int(''.join(out)))
    print(sum(outputs))