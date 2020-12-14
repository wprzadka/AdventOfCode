from pprint import pprint


def execute(line: dict) -> tuple:
    if line['cmd'] == 'nop':
        return 1, 0
    if line['cmd'] == 'acc':
        return 1, int(line['arg'], 10)
    if line['cmd'] == 'jmp':
        return int(line['arg'], 10), 0


if __name__ == '__main__':

    with open('input.txt') as file:
        lines = file.readlines()
    program = [line.split() for line in lines]
    program = [{'cmd': cmd, 'arg': arg, 'visited': False} for cmd, arg in program]

    idx = 0
    acc = 0
    curr = program[idx]
    while not curr['visited']:
        program[idx]['visited'] = True
        inc_idx, inc_acc = execute(curr)
        idx += inc_idx
        acc += inc_acc
        curr = program[idx]

    print(acc)