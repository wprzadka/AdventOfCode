import numpy as np

def is_safe(report: list[int]) -> bool:
    sign_val = np.sign(report[1] - report[0])
    
    last = report[0]
    for x in report[1:]:
        diff = x - last
        if np.dot(sign_val, diff) <= 0 or abs(diff) > 3:
            return False
        last = x

    return True

if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()

    reports = [[int(v) for v in x.split()] for x in data]

    count_safe = 0
    for rep in reports:
        count_safe += is_safe(rep)
    
    print(count_safe)

    