with open("data.txt") as f:
    data = f.read().splitlines()

directions = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

# Part 1
start = [(0, 0)]
total = 0
for line in data:
    direction, num, _ = line.split()
    dest_row, dest_col = directions[direction]
    num = int(num)
    total += num
    row, col = start[-1]
    start.append((row + dest_row * num, col + dest_col * num))
print(abs(sum(start[i][0] * (start[i - 1][1] - start[(i + 1) % len(start)][1]) for i in range(len(start)))) // 2 - total // 2 + 1 + total)

# Part 2
start = [(0, 0)]
total = 0
for line in data:
    _, _, code = line.split()
    code = code[2:-1]
    dest_row, dest_col = directions["RDLU"[int(code[-1])]]
    num = int(code[:-1], 16)
    total += num
    r, c = start[-1]
    start.append((r + dest_row * num, c + dest_col * num))
print(abs(sum(start[i][0] * (start[i - 1][1] - start[(i + 1) % len(start)][1]) for i in range(len(start)))) // 2 - total // 2 + 1 + total)
