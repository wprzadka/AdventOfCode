from typing import Optional, Union
import numpy as np


def add(fst: list, snd: list) -> list:
    num = [fst, snd]
    # print(f'after addition: {num}')
    needs_action = True
    while needs_action:
        path = needs_explode(num)
        if path:
            num = explode(num, path)
            # print(f'after explode:  {num}')
            continue
        path = needs_split(num, path)
        if path:
            num = split(num, path)
            # print(f'after split:  {num}')
            continue
        else:
            needs_action = False
    return num


def needs_explode(num: list, path: list = None) -> Optional[list]:
    if not path:
        path = []

    if type(num) == int:
        if len(path) > 4:
            return path
        return None

    new_path = needs_explode(num[0], path + [0])
    if new_path:
        return new_path
    new_path = needs_explode(num[1], path + [1])
    if new_path:
        return new_path
    return None


def get_part(num: list, path: list) -> list:
    iterator = num
    for p in path:
        iterator = iterator[p]
    return iterator


def explode(num: list, path: list) -> list:
    left, right = get_part(num, path[:-1])

    # closer elem
    p_next = path[:-1]
    p_next[-1] = 1 if p_next[-1] == 0 else 0

    iterator = get_part(num, p_next[:-1])
    if type(iterator[p_next[-1]]) == int:
        iterator[p_next[-1]] += left if p_next[-1] == 0 else right
    elif p_next[-1] == 0:
        iterator[0][1] += left
    else:
        iterator[1][0] += right
    close_side = p_next[-1]

    # wider element
    p_next = path[:-1]
    idx = -2
    while abs(idx) < len(p_next) and p_next[idx] != close_side:
        idx -= 1

    if p_next[idx] == close_side:
        p_next[idx] = 1 if p_next[idx] == 0 else 0

        iterator = get_part(num, p_next[:idx])
        if type(iterator[p_next[idx]]) == int:
            iterator[p_next[idx]] += left if p_next[idx] == 0 else right  # ???
        else:
            iterator = iterator[p_next[idx]]
            side = 1 if p_next[idx] == 0 else 0
            while type(iterator[side]) != int:
                iterator = iterator[side]
            iterator[side] += right if side == 0 else left

    iterator = get_part(num, path[:-2])
    iterator[path[-2]] = 0
    return num


def needs_split(num: list, path: list = None) -> Optional[list]:
    if not path:
        path = []
    for i, sub_num in enumerate(num):
        if type(sub_num) == int:
            if sub_num > 9:
                return path + [i]
        else:
            new_path = needs_split(sub_num, path + [i])
            if new_path:
                return new_path
    return None


def split(num: list, path: list) -> list:
    iterator = num
    for p in path[:-1]:
        iterator = iterator[p]
    val = iterator[path[-1]]
    left = val // 2
    right = left + val % 2
    iterator[path[-1]] = [left, right]
    return num


def compute_magintude(num: Union[list, int]) -> int:
    if type(num) == int:
        return num
    left, right = num
    return 3 * compute_magintude(left) + 2 * compute_magintude(right)


if __name__ == '__main__':

    with open('fst.txt') as f:
        numbers = [eval(v.rstrip()) for v in f.readlines()]

    summed = numbers[0]
    for num in numbers[1:]:
        summed = add(summed, num)
        print(summed)
    print(compute_magintude(summed))
