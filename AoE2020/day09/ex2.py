
if __name__ == '__main__':
    interval = 25
    with open('input.txt') as file:
        row = file.readlines()
    values = [int(v) for v in row[:-1]]
    size = len(values)

    target = 177777905
    beg = 0
    end = 1
    total = sum(values[0:2])
    while beg < size or end < size:
        if total == target:
            print(min(values[beg: end + 1]) + max(values[beg: end + 1]))
            break
        elif total > target:
            total -= values[beg]
            beg += 1
        else:
            end += 1
            total += values[end]