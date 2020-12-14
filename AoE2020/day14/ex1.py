def parse_line(line: str) -> tuple:
    operation, value = line[:-1].split(" = ")
    if operation == 'mask':
        return operation, None, value
    else:
        operation, arg = operation.split("[")
        return operation, int(arg[:-1], 10), value


def parse_value(mask: str, value: int) -> int:
    value = list(reversed(bin(value)[2:]))
    accumulator = 0
    # acc_bin = []
    for bit_num, mask_bit_val in enumerate(reversed(mask)):
        bit_val = 0
        if mask_bit_val == '1' or (mask_bit_val == 'X' and bit_num < len(value) and value[bit_num] == '1'):
            bit_val = 1
        # acc_bin.append(bit_val)
        accumulator += (bit_val << bit_num)
    # print(list(reversed(acc_bin)))
    return accumulator


if __name__ == '__main__':
    with open('input.txt') as file:
        input = file.readlines()

    size = 0
    for line in input:
        op, arg, val = parse_line(line)
        if arg and arg > size:
            size = arg
    print(f'memory size = {size}')
    memory = [0 for _ in range(size + 1)]
    current_mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    print(f'mask length = {len(current_mask)}')

    for line in input:
        op, arg, val = parse_line(line)
        if op == 'mask':
            current_mask = val
        else:
            acc = parse_value(current_mask, int(val, 10))
            # print(acc)
            memory[arg] = acc

    print(sum(memory))