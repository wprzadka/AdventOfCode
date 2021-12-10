import numpy as np


def is_opening(b: chr) -> bool:
    return b in ['(', '[', '{', '<']


def is_closing(b: chr) -> bool:
    return b in [')', ']', '}', '>']


if __name__ == '__main__':

    bracket_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
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

    with open('snd.txt') as f:
        lines = [v.rstrip() for v in f.readlines()]
    scores = []

    for line in lines:
        aside = []
        for i, v in enumerate(line):
            if is_opening(v):
                aside.append(v)
            if is_closing(v):
                if aside[-1] != complementary[v]:
                    aside.clear()
                    break
                aside.pop(-1)
        if len(aside) > 0:
            curr_score = 0
            for v in reversed(aside):
                curr_score *= 5
                curr_score += bracket_score[complementary[v]]
            print(f'{line} : {"".join([complementary[v] for v in reversed(aside)])} -> {curr_score}')
            scores.append(curr_score)

    print(sorted(scores))
    print(sorted(scores)[len(scores) // 2])