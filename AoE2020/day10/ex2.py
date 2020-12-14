if __name__ == '__main__':
    with open('input.txt') as file:
        input = [int(x, 10) for x in file.readlines()]

    ordered = sorted(input)
    ways = [0 for _ in range(ordered[-1] + 1)]
    ways[0] = 1
    for val in ordered:
        for d in [1, 2, 3]:
            if val - d >= 0:
                ways[val] += ways[val - d]
    print(ways[-1])
