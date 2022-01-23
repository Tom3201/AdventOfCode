with open("data.txt") as f:
    data = f.readlines()

#Part 1
position = 0
depth = 0
for line in data:
    line = line.split(' ')
    if line[0] == "forward":
        position += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])
print(position * depth)

#Part 2
position = 0
depth = 0
aim = 0
for line in data:
    line = line.split(' ')
    if line[0] == "forward":
        position += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
print(position * depth)