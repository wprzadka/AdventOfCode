if __name__ == '__main__':
    count = 0
    with open('input.txt') as file:
        row = file.readline()
        while row != '':
            fields = {
                'byr': False,
                'iyr': False,
                'eyr': False,
                'hgt': False,
                'hcl': False,
                'ecl': False,
                'pid': False,
                'cid': True,
            }
            while row != '\n':
                pairs = row.split()
                for pair in pairs:
                    fields[pair.split(':')[0]] = True
                row = file.readline()
            if all(fields.values()):
                count += 1
            row = file.readline()
    print(count)
