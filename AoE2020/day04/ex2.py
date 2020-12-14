import re


def isValid(key: str, value: str) -> bool:
    if key in ['byr', 'iyr', 'eyr']:
        try:
            value = int(value, 10)
        except ValueError:
            return False

    if key == 'byr':
        return 1920 <= value <= 2002
    elif key == 'iyr':
        return 2010 <= value <= 2020
    elif key == 'eyr':
        return 2020 <= value <= 2030
    elif key == 'hgt':
        unit = value[-2:]
        try:
            value = int(value[:-2], 10)
        except ValueError:
            return False
        if unit == 'cm':
            return 150 <= value <= 193
        elif unit == 'in':
            return 59 <= value <= 76
        else:
            return False
    elif key == 'hcl':
        return re.fullmatch('#[a-z0-9]{6}', value) is not None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.fullmatch('[0-9]{9}', value) is not None
    elif key == 'cid':
        return True
    else:
        return False


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
                    key, val = pair.split(':')
                    if isValid(key, val):
                        fields[key] = True
                    else:
                        print(key, ': ', val)
                row = file.readline()
            if all(fields.values()):
                count += 1
            row = file.readline()
    print(count)
