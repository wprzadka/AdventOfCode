
import re
if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.read()

    iter = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    total = sum(int(match.group(1)) * int(match.group(2)) for match in iter)
    print(total)
