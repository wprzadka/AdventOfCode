if __name__ == '__main__':
    values = []
    count_password = 0

    with open('input.txt') as file:
        row = file.readline()
        while row != '':
            interval, letter, word = row.split(' ')
            lower, upper = interval.split('-')
            lower = int(lower)
            upper = int(upper)
            letter = letter[0]

            count_char = (1 if word[lower - 1] == letter else 0) + (1 if word[upper - 1] == letter else 0)
            if count_char == 1:
                count_password += 1
            row = file.readline()
    print(count_password)
