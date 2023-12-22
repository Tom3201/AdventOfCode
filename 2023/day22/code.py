from collections import deque

with open("data.txt") as f:
    data = f.read().splitlines()

bricks = [list(map(int, line.replace("~", ",").split(","))) for line in data]
bricks.sort(key=lambda brick: brick[2])


def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])


for a, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:a]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

vertical = {a: set() for a in range(len(bricks))}
horizontal = {a: set() for a in range(len(bricks))}

for b, upper in enumerate(bricks):
    for a, lower in enumerate(bricks[:b]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            vertical[a].add(b)
            horizontal[b].add(a)

# Part 1
total = 0
for a in range(len(bricks)):
    if all(len(horizontal[b]) >= 2 for b in vertical[a]):
        total += 1
print(total)

# Part 2
total = 0
for a in range(len(bricks)):
    queue = deque(b for b in vertical[a] if len(horizontal[b]) == 1)
    falling = set(queue)
    falling.add(a)
    while queue:
        b = queue.popleft()
        for k in vertical[b] - falling:
            if horizontal[k] <= falling:
                queue.append(k)
                falling.add(k)
    total += len(falling) - 1
print(total)
