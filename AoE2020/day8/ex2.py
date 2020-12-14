from pprint import pprint


def execute(line: dict) -> tuple:
    if line['cmd'] == 'nop':
        return 1, 0
    if line['cmd'] == 'acc':
        return 1, int(line['arg'], 10)
    if line['cmd'] == 'jmp':
        return int(line['arg'], 10), 0


def run_program(program: list) -> tuple:
    idx = 0
    acc = 0
    curr = program[idx]
    while not curr['visited'] and idx < len(program):
        program[idx]['visited'] = True
        inc_idx, inc_acc = execute(curr)
        idx += inc_idx
        acc += inc_acc

        try:
            curr = program[idx]
        except IndexError:
            curr = program[-1]

    exec_code = 0 if idx == len(program) else -1
    return acc, exec_code


if __name__ == '__main__':

    with open('input.txt') as file:
        lines = file.readlines()
    program = [line.split() for line in lines]
    program = [{'cmd': cmd, 'arg': arg, 'visited': False} for cmd, arg in program]

    for idx, line in enumerate(program):
        if line['cmd'] in ['nop', 'jmp']:
            mutant = [{'cmd': row['cmd'], 'arg': row['arg'], 'visited': False} for row in program]
            mutant[idx]['cmd'] = 'jmp' if line['cmd'] == 'nop' else 'nop'
            acc, code = run_program(mutant)
            if code == 0:
                print(acc, code)
                break
