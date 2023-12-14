with open("data.txt") as f:
    data = f.read().splitlines()

# Part 1
rocks = set()
solid = set()
for a, line in enumerate(data):
    for b, char in enumerate(line):
        if char == "O":
            rocks.add((a, b))
        elif char == "#":
            solid.add((a, b))

changed = True
while changed:
    changed = False
    for (a, b) in rocks:
        if a - 1 < 0:
            continue
        if (a - 1, b) in solid:
            continue
        if (a - 1, b) in rocks:
            continue
        rocks.remove((a, b))
        rocks.add((a - 1, b))
        changed = True
rocks = sorted(rocks)

total = 0
for i in range(len(data), 0, -1):
    total += len([a for (a, _) in rocks if a == len(data) - i]) * i
print(total)

# Part 2
grid = [[char for char in line] for line in data]
hashes = {}
target = 10**9
counter = 0
while counter < target:
    counter += 1
    for _ in range(4):
        for b in range(len(grid[0])):
            for _ in range(len(grid)):
                for a in range(len(grid)):
                    if grid[a][b] == 'O' and a > 0 and grid[a - 1][b] == '.':
                        grid[a][b] = '.'
                        grid[a - 1][b] = 'O'
        new_grid = [['ö' for _ in range(len(grid))] for _ in range(len(grid[0]))]
        for b in range(len(grid)):
            for a in range(len(grid[0])):
                new_grid[a][len(grid) - 1 - b] = grid[b][a]
        grid = new_grid
    grid_hash = tuple(tuple(line) for line in grid)
    if grid_hash in hashes:
        length = counter - hashes[grid_hash]
        amount = (target - counter) // length
        counter += amount * length
    hashes[grid_hash] = counter
print(sum([sum([len(grid) - a for b in range(len(grid[0])) if grid[a][b] == 'O']) for a in range(len(grid))]))
