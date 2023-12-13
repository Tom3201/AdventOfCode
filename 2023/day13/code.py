from collections import defaultdict

with open("data.txt") as f:
    data = f.read().splitlines()

# Part 1
horizontal_lines = []
mirror = []
vertical_lines = defaultdict(str)
start_index = 0
for i, line in enumerate(data):
    if line == "" or len(data) == i + 1:
        vertical_lines = list(vertical_lines.values())
        found = False
        while vertical_lines.count(vertical_lines[0]) > 1 and not found:
            j = vertical_lines[1:].index(vertical_lines[0]) + 1
            for a in range(j // 2 + 1):
                if vertical_lines[a] != vertical_lines[j - a]:
                    vertical_lines[j] = vertical_lines[j] + "lol"
                    break
                if a == j // 2:
                    mirror.append(a + 1)
                    vertical_lines[j] = vertical_lines[j] + "lol"
                    found = True
        while vertical_lines.count(vertical_lines[-1]) > 1 and not found:
            j = vertical_lines.index(vertical_lines[-1])
            for a in range(j, j + (len(vertical_lines) - j) // 2):
                if vertical_lines[a] != vertical_lines[len(vertical_lines) - 1 - (a - j)]:
                    vertical_lines[j] = vertical_lines[j] + "lol"
                    break
                if a + 1 == len(vertical_lines) - 1 - (a - j):
                    mirror.append(a + 1)
                    vertical_lines[j] = vertical_lines[j] + "lol"
                    found = True
        while horizontal_lines.count(horizontal_lines[0]) > 1 and not found:
            j = horizontal_lines[1:].index(horizontal_lines[0]) + 1
            for a in range(j // 2 + 1):
                if horizontal_lines[a] != horizontal_lines[j - a]:
                    horizontal_lines[j] = horizontal_lines[j] + "lol"
                    break
                if a == j // 2:
                    mirror.append((a + 1) * 100)
                    horizontal_lines[j] = horizontal_lines[j] + "lol"
                    found = True
        while horizontal_lines.count(horizontal_lines[-1]) > 1 and not found:
            j = horizontal_lines.index(horizontal_lines[-1])
            for a in range(j, j + (len(horizontal_lines) - j) // 2):
                if horizontal_lines[a] != horizontal_lines[len(horizontal_lines) - 1 - (a - j)]:
                    horizontal_lines[j] = horizontal_lines[j] + "lol"
                    break
                if a + 1 == len(horizontal_lines) - 1 - (a - j):
                    mirror.append((a + 1) * 100)
                    horizontal_lines[j] = horizontal_lines[j] + "lol"
                    found = True

        horizontal_lines = []
        vertical_lines = defaultdict(str)
        continue
    start_index += 1
    horizontal_lines.append(line)
    for k, char in enumerate(line):
        vertical_lines[k] = char + vertical_lines[k]
print(sum(mirror))

# Part 2
result = 0
grids = []
grid = []
for i, grid_data in enumerate(data):
    if grid_data != "":
        grid.append(grid_data)
    if grid_data == "" or i == len(data) - 1:
        grids.append(grid)
        grid = []

for grid in grids:
    rows = len(grid)
    cols = len(grid[0])

    for col in range(cols - 1):
        inconsistency = 0
        for dest_col in range(cols):
            left_col = col - dest_col
            right_col = col + 1 + dest_col
            if 0 <= left_col < right_col < cols:
                for row in range(rows):
                    if grid[row][left_col] != grid[row][right_col]:
                        inconsistency += 1
        if inconsistency == 1:
            result += col + 1

    for row in range(rows - 1):
        inconsistency = 0
        for dest_row in range(rows):
            up_row = row - dest_row
            down_row = row + 1 + dest_row
            if 0 <= up_row < down_row < rows:
                for col in range(cols):
                    if grid[up_row][col] != grid[down_row][col]:
                        inconsistency += 1
        if inconsistency == 1:
            result += 100 * (row + 1)
print(result)
