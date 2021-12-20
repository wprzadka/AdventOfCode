import numpy as np


def add_padding(img: list, padding: int = 1, mark: chr = '.'):
    empty_row = [mark] * (len(img[0]) + 2 * padding)
    img = [empty_row] * padding + \
          [padding * [mark] + row + padding * [mark] for row in img] + \
          [empty_row] * padding
    return img


def correct_boundary(img: list, value: chr) -> list:
    size_y = len(img)
    size_x = len(img[0])
    for y in range(size_y):
        img[y][0] = value
        img[y][size_x - 1] = value
    for x in range(size_x):
        img[0][x] = value
        img[size_y - 1][x] = value
    return img


def compute_pixel(img: np.ndarray, code: str, pos: tuple) -> chr:
    x, y = pos
    # ker = [v[x-1:x+2] for v in img[y-1:y+2]]
    ker = img[x-1:x+2, y-1:y+2]
    # print(ker)
    idx = int(''.join(ker.flatten()).replace('.', '0').replace('#', '1'), 2)
    return code[idx]


if __name__ == '__main__':
    with open('fst.txt') as f:
        code = f.readline()
        _ = f.readline()
        image = [[a for a in v.rstrip()] for v in f.readlines()]

    print(code)

    image = np.array(add_padding(image, 2))

    print(image.shape)
    for row in image:
        print(''.join(row))
    print()

    for step in range(2):
        output = [
            [
                compute_pixel(image, code, (j, i))
                for i in range(1, len(image[0]) - 1)
            ]
            for j in range(1, len(image) - 1)
        ]
        if code[0] == '#' and code[-1] == '.':
            output = correct_boundary(output, '.' if step % 2 == 1 else '#')
        elif code[0] == '#' and code[-1] == '#':
            output = correct_boundary(output, '#')

        image = np.array(add_padding(output, 2, output[0][0]))
        print(image.shape)

        for row in image:
            print(''.join(row))
        print()

        print(np.sum(image == '#'))
