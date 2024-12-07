if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    equations = [[v.strip() for v in x.split(':')] for x in data]

    total = 0
    ops = ['+', '*']
    for eq in equations:

        # print(eq)
        expected = int(eq[0])
        nums = eq[1].split()

        for op_id in range(1 << (len(nums) - 1)):
            res = nums[0]
            for pos, x in enumerate(nums[1:]):
                op = (op_id >> pos) & 1
                # print(op, end='')
                res = eval(f'{res}{ops[op]}{x}')
            # print()
            # print(res, expected)
            if res == expected:
                total += res
                break

    print(total)