
if __name__ == '__main__':

    with open('input.txt') as file:

        entries = []
        row = file.readline()
        while row != '':
            name, contains = row.split('bags contain')
            contains = contains[:-2].split(',')
            for idx, cont in enumerate(contains):
                contains[idx] = cont.replace(' ', '')
                numEnd = -1
                temp = '0'
                while ord('0') <= ord(temp) <= ord('9'):
                    temp = contains[idx][numEnd + 1]
                    numEnd += 1
                contains[idx] = contains[idx][numEnd:].replace('bags', '').replace('bag', '')
            entries.append((name.replace(' ', ''), contains))
            row = file.readline()

    for ent in entries:
        print(ent[0], ent[1])

    possibleBags = set()
    lookingFor = {'shinygold'}
    while len(lookingFor) > 0:

            lookingForNext = set()
            for name, contains in entries:
                for cont in contains:
                    isFound = False
                    if cont in lookingFor:
                        isFound = True
                    if isFound:
                        lookingForNext.add(name)
            possibleBags.update(lookingForNext)
            lookingFor = lookingForNext

    print(len(possibleBags))