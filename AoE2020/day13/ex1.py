if __name__ == '__main__':
    with open('input.txt') as file:
        arriving_time = int(file.readline(), 10)
        temp = file.readline()
    buss_id = []
    for id in temp.split(','):
        if id != 'x':
            buss_id.append(int(id, 10))
    print(buss_id)

    buss_time = [x for x in buss_id]
    for idx, buss in enumerate(buss_id):
        while buss_time[idx] < arriving_time:
            buss_time[idx] += buss

    min_buss = {'id': 0, 'time': max(buss_time)}
    for idx, time in enumerate(buss_time):
        if time < min_buss['time']:
            min_buss['time'] = time
            min_buss['id'] = buss_id[idx]
    waiting_time = min_buss['time'] - arriving_time
    print(min_buss['id'] * waiting_time)