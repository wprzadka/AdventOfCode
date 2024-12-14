if __name__ == '__main__':
    with open('input.txt') as f_in:
        data = f_in.readlines()
    data = [[int(x) for x in row.strip()] for row in data]
    height = len(data)
    width = len(data[0])

    def findTracks(pos: tuple[int, int]) -> int:
        res = set()
        paths_count = 0
        que = [pos]
        while len(que) > 0:
            x, y = que.pop(0)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < width and 0 <= ny < height):
                    continue
                if data[ny][nx] - data[y][x] != 1:
                    continue
                if data[ny][nx] == 9:
                    res.add((nx, ny))
                    paths_count += 1
                else:
                    que.append((nx, ny))
        return len(res), paths_count

    total_tracks = 0
    total_paths = 0
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v != 0:
                continue
            tracks, paths = findTracks((x, y))
            # print(x, y, tracks_found)
            total_tracks += tracks
            total_paths += paths
    print(total_tracks, total_paths)
