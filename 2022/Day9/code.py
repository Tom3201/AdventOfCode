with open("data.txt") as f:
    data = f.read().splitlines()
moves = []
movements = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
for line in data:
    move = {}
    line = line.split()
    move[line[0]] = int(line[1])
    moves.append(move)


def checkTail(h, t):
    if (
        abs(h[0] - t[0]) > 1 or
        abs(h[1] - t[1]) > 1
    ):
        if abs(h[0] - t[0]) > 1:
            if h[0] < t[0]:
                h = (h[0]+1, h[1])
            else:
                h = (h[0]-1, h[1])
        if abs(h[1] - t[1]) > 1:
            if h[1] < t[1]:
                h = (h[0], h[1]+1)
            else:
                h = (h[0], h[1]-1)
        return h
    return t


#Part1
last_update = (0, 0)
head = (0, 0)
tail = last_update
grid = {}
for move in moves:
    for a, v in move.items():
        pattern = movements[a]
        for _ in range(v):
            head = tuple(map(sum, zip(pattern, head)))
            tail = checkTail(head, tail)
            if tail not in grid:
                grid[tail] = 1
                continue
            grid[tail] += 1
print(len(grid))


#Part2
head = (0, 0)
tail = [(0, 0) for _ in range(9)]
grid = {}
for move in moves:
    for a, v in move.items():
        pattern = movements[a]
        for _ in range(v):
            head = tuple(map(sum, zip(pattern, head)))
            tail[0] = checkTail(head, tail[0])
            for c in range(1, 9):
                tail.insert(c, checkTail(tail[c-1], tail[c]))
                tail.pop(c+1)
                if tail[8] not in grid:
                    grid[tail[8]] = 1
                    continue
                grid[tail[8]] += 1
print(len(grid))
