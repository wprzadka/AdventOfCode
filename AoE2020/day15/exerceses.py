if __name__ == '__main__':
    game_length = 30000000
    input = [1, 0, 15, 2, 10, 13]
    # input = [0, 3, 6]
    # input = [3,1,2]
    last_spoken = [-1 for _ in range(game_length + 1)]
    for idx, val in enumerate(input, 1):
        last_spoken[val] = idx

    print(input)

    current = input[-1]
    for t in range(len(input) + 1, game_length + 1):

        rec = last_spoken[current]
        last_spoken[current] = t - 1

        if rec == -1:
            current = 0
        else:
            current = t - 1 - rec
        # print(current)

    print(current)
