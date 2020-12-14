from itertools import chain, combinations


def parse_line(line: str) -> tuple:
    operation, value = line[:-1].split(" = ")
    if operation == 'mask':
        return operation, None, value
    else:
        operation, arg = operation.split("[")
        return operation, int(arg[:-1]), value


def parse_addr(addr: int, mask: str) -> str:
    addr = list(reversed(bin(addr)[2:]))
    new_addr = ''
    for idx, val in enumerate(reversed(mask)):
        if val in ['1', 'X']:
            new_addr += val
        else:
            new_addr += addr[idx] if idx < len(addr) else '0'

    return new_addr[::-1]


def floating_indices(addr: str) -> list:
    return [idx for idx, val in enumerate(addr) if val == 'X']


if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()

    memory = {}
    print(f'memory size = {len(memory)}')

    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    print(f'mask length = {len(current_mask)}')

    for line in input:
        op, arg, val = parse_line(line)
        if op == 'mask':
            current_mask = val
        else:
            addr_mask = parse_addr(arg, current_mask)
            # print(addr_mask)
            base_addr = addr_mask.replace('X', '0')
            # print(base_addr)
            print('---')
            indices = floating_indices(addr_mask)
            length_sets = [list(combinations(indices, r)) for r in range(len(indices) + 1)]
            all_sets = []
            for row in length_sets:
                for x in row:
                    all_sets.append(x)
            # print(all_sets)
            for idx_set in all_sets:
                addr = ''
                for idx, v in enumerate(base_addr):
                    addr += '1' if idx in idx_set else v
                # print(idx_set)
                # print(addr)
                memory[addr] = int(val, 10)
    # from pprint import pprint
    # pprint(memory)

    print(sum(memory.values()))
