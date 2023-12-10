from collections import defaultdict, deque
from copy import deepcopy

with open("data.txt") as f:
    data = f.read().splitlines()

grid = defaultdict(list)
for i, line in enumerate(data):
    grid[i] = [char for char in line]
    if "S" in line:
        start_pos = (i, line.index("S"))

valid = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(1, 0), (0, -1)],
    "J": [(1, 0), (0, 1)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, -1), (-1, 0)]
}
look_around = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Part 1
current_pos = start_pos
next_look = (-1, -1)
steps = 1
while True:
    steps += 1
    if next_look == (-1, -1):
        for look in look_around:
            a, b = current_pos
            a += look[0]
            b += look[1]
            if a < 0 or len(grid) <= a or b < 0 or len(grid[0]) <= b:
                continue
            if grid[a][b] == ".":
                continue
            options = deepcopy(valid[grid[a][b]])
            if look not in options:
                print(f"{current_pos} is illegal")
                continue
            options.remove(look)
            next_look = (options[0][0] * -1, options[0][1] * -1)
            current_pos = (a, b)
            break
    a, b = current_pos
    a += next_look[0]
    b += next_look[1]
    if a < 0 or len(grid) <= a or b < 0 or len(grid[0]) <= b:
        continue
    if grid[a][b] == ".":
        continue
    elif grid[a][b] == "S":
        print("Info: Start reached again")
        break
    options = deepcopy(valid[grid[a][b]])
    if next_look not in options:
        print(f"{current_pos} is illegal")
        continue
    options.remove(next_look)
    next_look = (options[0][0] * -1, options[0][1] * -1)
    current_pos = (a, b)
print(steps // 2)

# Part 2
a, b = start_pos
up = (grid[a - 1][b] in ["|", "7", "F"])
right = (grid[a][b + 1] in ["-", "7", "J"])
down = (grid[a + 1][b] in ["|", "L", "J"])
left = (grid[a][b - 1] in ["-", "L", "F"])
if up and down:
    grid[a][b] = "|"
elif up and right:
    grid[a][b] = "L"
elif up and left:
    grid[a][b] = "J"
elif down and right:
    grid[a][b] = "F"
elif down and left:
    grid[a][b] = "7"
elif left and right:
    grid[a][b] = "-"

vision_field = [['.' for _ in range((len(grid[0]) * 3))] for _ in range((len(grid.values()) * 3))]
for a_idx, a_val in enumerate(grid.values()):
    aa = a_idx * 3
    for b_idx, b_val in enumerate(a_val):
        bb = b_idx * 3
        if b_val == ".":
            continue
        elif b_val == "|":
            vision_field[aa][bb + 1] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa + 2][bb + 1] = "x"
        elif b_val == "-":
            vision_field[aa + 1][bb] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa + 1][bb + 2] = "x"
        elif b_val == "L":
            vision_field[aa][bb + 1] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa + 1][bb + 2] = "x"
        elif b_val == "J":
            vision_field[aa + 1][bb] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa][bb + 1] = "x"
        elif b_val == "7":
            vision_field[aa + 1][bb] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa + 2][bb + 1] = "x"
        elif b_val == "F":
            vision_field[aa + 2][bb + 1] = "x"
            vision_field[aa + 1][bb + 1] = "x"
            vision_field[aa + 1][bb + 2] = "x"

Q = deque()
for a_idx in range(len(grid.values()) * 3):
    Q.append((a_idx, 0))
    Q.append((a_idx, len(grid[0]) * 3 - 1))
for b_idx in range(len(grid[0]) * 3):
    Q.append((0, b_idx))
    Q.append((len(grid.values()) * 3 - 1, b_idx))

seen = set()
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
while Q:
    a, b = Q.popleft()
    if (a, b) in seen:
        continue
    if not (0 <= a < len(grid.values()) * 3 and 0 <= b < len(grid[0]) * 3):
        continue
    seen.add((a, b))
    if vision_field[a][b] == "x":
        continue
    for i in range(4):
        Q.append((a + da[i], b + db[i]))

total = 0
for a_idx, a_val in enumerate(grid.values()):
    for b_idx, _ in enumerate(a_val):
        visible = any((a_idx * 3 + aa, b_idx * 3 + bb) in seen for aa in [0, 1, 2] for bb in [0, 1, 2])
        if not visible:
            total += 1
print(total)
