from itertools import product

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    equations = [[v.strip() for v in x.split(':')] for x in data]

    total = 0
    ops = ['+', '*', '']
    for eq in equations:

        print(eq)
        expected = int(eq[0])
        nums = eq[1].split()

        for op_prod in product(ops, repeat=(len(nums) - 1)):
            res = int(nums[0])
            # print(res, end='')
            for pos, x in enumerate(nums[1:]):
                res = eval(f'{res}{op_prod[pos]}{x}')
            #     print(f'{op_prod[pos]}{x}', end='')
            # print(f' = {res}')
            if res == expected:
                # print("^")
                total += res
                break
    print(total)