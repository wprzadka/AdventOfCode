from modint import ChineseRemainderConstructor, chinese_remainder

if __name__ == '__main__':
    with open('input.txt') as file:
        _ = file.readline()
        input = file.readline()

    remainders = []
    shifts = []
    for shift, val in enumerate(input.split(',')):
        if val != 'x':
            val = int(val, 10)
            remainders.append(val)
            shifts.append(-shift % val)
    print(shifts)
    print(remainders)

    cr = ChineseRemainderConstructor(remainders)
    print(cr.rem(shifts))