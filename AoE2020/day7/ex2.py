
if __name__ == '__main__':

    with open('input.txt') as file:

        entries = []
        row = file.readline()
        while row != '':
            name, contains = row.split('bags contain')
            contains = contains[:-2].split(',')
            for idx, cont in enumerate(contains):
                content = cont.replace(' ', '')
                numEnd = -1
                temp = '0'
                while ord('0') <= ord(temp) <= ord('9'):
                    temp = content[numEnd + 1]
                    numEnd += 1
                try:
                    numOfBags = 0 if numEnd == 0 else int(content[:numEnd])
                except ValueError:
                    print("!!!" + content + "!!!")
                containsName = content[numEnd:].replace('bags', '').replace('bag', '')

                entries.append((name.replace(' ', ''), containsName, numOfBags))
            row = file.readline()

    # for name, cont, num in entries:
    #     print(f'{name} -> {cont} ({num})')

    bagsInside = 0
    currentLayer = {'shinygold': 1}
    while currentLayer:
            nextLayer = dict()
            for name, contains, num in entries:
                if name in currentLayer.keys():
                    currNum = nextLayer.get(contains, 0)
                    nextLayer[contains] = currentLayer[name] * num + currNum
                    bagsInside += currentLayer[name] * num
            currentLayer = nextLayer

    # for bag, num in bagsInside.items():
    #     print(f'{bag} -> {num}')
    # -1 because don't contain shinygold itself
    print(bagsInside)