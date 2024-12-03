
import re
if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.read()

    iter = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', data)
    total = 0
    enable = True
    for match in iter:
        print(match)
        if match.group(0) == 'do()':
            enable = True
        elif match.group(0) == 'don\'t()':
            enable = False
        elif enable:
            total += int(match.group(1)) * int(match.group(2))
    print(total)
