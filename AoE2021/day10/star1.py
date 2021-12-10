import numpy as np


def is_opening(b: chr) -> bool:
    return b in ['(', '[', '{', '<']


def is_closing(b: chr) -> bool:
    return b in [')', ']', '}', '>']


if __name__ == '__main__':
    
    bracket_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    complementary = {
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '<': '>',
        '>': '<'
    }
    
    with open('fst.txt') as f:
        lines = [v.rstrip() for v in f.readlines()]
    score = 0

    for line in lines:
        aside = []
        for i, v in enumerate(line):
            if is_opening(v):
                aside.append(v)
            if is_closing(v):
                if aside[-1] == complementary[v]:
                    aside.pop(-1)
                else:
                    score += bracket_score[v]
                    print(line)
                    print(' ' * i, '^', sep='')
                    break
    print(score)