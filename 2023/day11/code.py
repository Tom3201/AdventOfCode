from collections import defaultdict

with open("data.txt") as f:
    data = f.read().splitlines()

galaxies = set()
empty_x = []
empty_y = []
temp = defaultdict(bool)
for a, line in enumerate(data):
    if "#" not in line:
        empty_x.append(a)
    for b, char in enumerate(line):
        if char == "#":
            galaxies.add((a, b))
            temp[b] = False
            continue
        if temp[b] or a == 0:
            temp[b] = True
for b, empty in enumerate(temp.values()):
    if empty:
        empty_y.append(b)

# Part 1
new_galaxies = set()
factor = 1
expansion_x = 0
for x in range(len(data)):
    expansion_y = 0
    if x in empty_x:
        expansion_x += factor
        continue
    for y in range(len(data[0])):
        if y in empty_y:
            expansion_y += factor
            continue
        if (x, y) in galaxies:
            new_galaxies.add((x + expansion_x, y + expansion_y))
new_galaxies = sorted(new_galaxies)
shortest_path = 0
for i, galaxy1 in enumerate(new_galaxies):
    for j in range(i + 1, len(new_galaxies)):
        shortest_path += abs(new_galaxies[j][0] - galaxy1[0]) + abs(new_galaxies[j][1] - galaxy1[1])
print(shortest_path)

# Part 2
new_galaxies = set()
factor = 999999
expansion_x = 0
for x in range(len(data)):
    expansion_y = 0
    if x in empty_x:
        expansion_x += factor
        continue
    for y in range(len(data[0])):
        if y in empty_y:
            expansion_y += factor
            continue
        if (x, y) in galaxies:
            new_galaxies.add((x + expansion_x, y + expansion_y))
new_galaxies = sorted(new_galaxies)
shortest_path = 0
for i, galaxy1 in enumerate(new_galaxies):
    for j in range(i + 1, len(new_galaxies)):
        shortest_path += abs(new_galaxies[j][0] - galaxy1[0]) + abs(new_galaxies[j][1] - galaxy1[1])
print(shortest_path)
