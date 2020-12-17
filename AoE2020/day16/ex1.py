from pprint import pprint

if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()

    fields = []
    tickets = []

    sepFlag = False
    for row in data:
        if row == '\n':
            sepFlag = True
        if not sepFlag:
            fields.append(row)
        else:
            tickets.append(row)
    nerby_tickets = tickets[5:]

    fields = [f[:-1].split(':')[1].split('or') for f in fields]
    fields = [(fst.split('-'), snd.split('-')) for fst, snd in fields]
    fields = [({'low': int(fst[0]), 'up': int(fst[1])},
               {'low': int(snd[0]), 'up': int(snd[1])})
              for fst, snd in fields]

    # pprint(fields)

    nerby_tickets = [tck[:-1].split(',') for tck in nerby_tickets]
    # for tck in nerby_tickets:
    #     print(tck)

    invalid = []
    for tck in nerby_tickets:
        for val in tck:
            val = int(val)
            invalid_flag = True
            for f in fields:
                if f[0]['low'] <= val <= f[0]['up'] or f[1]['low'] <= val <= f[1]['up']:
                    invalid_flag = False
            if invalid_flag:
                invalid.append(val)

    print(invalid)
    print(sum(invalid))
