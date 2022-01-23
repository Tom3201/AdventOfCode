from collections import deque

data = []
for line in open("data.txt"):
    data.append([int(x) for x in line.strip()])

risk = 0
for i, line in enumerate(data):
    for j, num in enumerate(line):
        low = True
        if j > 0:
            low = low and num < line[j - 1]
        if j + 1 < len(data[i]):
            low = low and num < line[j + 1]
        if i > 0:
            low = low and num < data[i - 1][j]
        if i + 1 < len(data):
            low = low and num < data[i + 1][j]
        if low:
            risk += num + 1
            again = True
print(risk)

erg = []
marked = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if (y, x) not in marked and data[y][x] < 9:
            size = 0
            Q = deque()
            Q.append((y, x))
            while Q:
                (y, x) = Q.popleft()
                if (y, x) in marked:
                    continue
                marked.append((y, x))
                size += 1
                for d in range(4):
                    xy_dir = [-1, 0, 1, 0]
                    tmp_y = y + xy_dir[d]
                    tmp_x = x + xy_dir[len(xy_dir) - 1 - d]
                    if 0 <= tmp_y < len(data) and 0 <= tmp_x < len(data[y]) and data[tmp_y][tmp_x] < 9:
                        Q.append((tmp_y, tmp_x))
            erg.append(size)
erg.sort()
print(erg[-1] * erg[-2] * erg[-3])
