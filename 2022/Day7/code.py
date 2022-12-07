with open("data.txt") as f:
    data = f.read().splitlines()


path = []
directories = {}
for line in data:
    if line[0] == "$":
        line = line[2:]
    line = line.split()
    if line[0] == "cd":
        if line[1] == "..":
            path.pop()
            continue
        path.append(line[1]) 
    elif line[0] not in ["dir", "ls"]:
        for a in range(1, len(path) + 1):
            name = '/'.join(path[:a])
            if name not in directories:
                directories[name] = 0
            directories[name] += int(line[0])


#Part1
total = 0
for _, a in directories.items():
    if a <= 100000:
        total += a
print(total)


#Part2
used = directories['/']
max_space = 70000000 - 30000000
needed_space = used - max_space
total = used + 1
for _, a in directories.items():
    if a > needed_space:
        total = min(total, a)
print(total)
