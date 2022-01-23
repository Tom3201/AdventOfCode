import re

with open("data.txt") as f:
    data = f.read().splitlines()

RGX = r'([0-9]+),([0-9]+).*?([0-9]+),([0-9]+)'

grid_part1 = {}
grid_part2 = {}
for line in data:
    line = re.search(RGX, line)
    x1 = int(line.group(1))
    y1 = int(line.group(2))
    x2 = int(line.group(3))
    y2 = int(line.group(4))

    dif_x = x2 - x1
    dif_y = y2 - y1

    for lol in range(max(abs(dif_x), abs(dif_y)) + 1):
        if dif_x > 0:
            x = x1 + 1 * lol
        elif dif_x < 0:
            x = x1 - 1 * lol
        else:
            x = x1 + 0 * lol

        if dif_y > 0:
            y = y1 + 1 * lol
        elif dif_y < 0:
            y = y1 - 1 * lol
        else:
            y = y1 + 0 * lol

        if dif_x == 0 or dif_y == 0:
            if (x,y) not in grid_part1:
                grid_part1[(x,y)] = 0
            grid_part1[(x,y)] += 1

        if (x,y) not in grid_part2:
            grid_part2[(x,y)] = 0
        grid_part2[(x,y)] += 1

ans = 0
for grid in grid_part1:
    if grid_part1[grid] > 1:
        ans += 1
print(ans)

ans = 0
for grid in grid_part2:
    if grid_part2[grid] > 1:
        ans += 1
print(ans)