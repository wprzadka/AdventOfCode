if __name__ == '__main__':
    with open('fst.txt') as f:
        lines = f.readlines()

    # length = len(lines[0]) - 1
    # values = [int(v) for v in lines]
    # gamma = 0
    # epsilon = 0
    # for bit in range(length):
    #     count = sum([(value & (1 << bit)) != 0 for value in values])
    #     if count > len(values) / 2:
    #         gamma += (1 << bit)
    #     else:
    #         epsilon += (1 << bit)
    # print(bin(gamma), bin(epsilon))
    # print(gamma, epsilon)
    # print(gamma * epsilon)  # 1943756

    gamma = ''
    epsilon = ''

    for idx in range(len(lines[0]) - 1):
        counter = {'0': 0, '1': 0}
        for w in [word[idx] for word in lines]:
            counter[w] += 1
        if counter['1'] > counter['0']:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))
