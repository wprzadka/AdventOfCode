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

            count_char = 0
            for char in word:
                if char == letter:
                    count_char += 1
            if lower <= count_char <= upper:
                count_password += 1
            row = file.readline()
    print(count_password)
