if __name__ == '__main__':
    with open('input.txt') as file:
        _ = file.readline()
        temp = file.readline()

    buss_id = []
    for shift, id in enumerate(temp.split(',')):
    # TODO remove
    # for shift, id in enumerate(('1789','37','47','1889')):
    # for shift, id in enumerate(('17','x','13','19')):
    # for shift, id in enumerate(('67','x','7','59','61')):
        if id != 'x':
            try:
                buss_id.append((int(id, 10), shift))
            except ValueError:
                print(id)
        # else:
        #     buss_id.append(-1)
    print(buss_id)



    t = 100000000000000  # min(buss_id)[0]
    foundFlag = False
    while not foundFlag:
        foundFlag = True
        t += 1

        beg = t % buss_id[0][0]
        for buss, shift in buss_id:

            if (t + shift) % buss != beg:
                foundFlag = False
                break
    print(t)