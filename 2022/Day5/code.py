from copy import deepcopy
import re


with open("data.txt") as f:
    raw = f.read().splitlines()


head = []
data = []
newline = 0
for line in raw:
    if line == "":
        newline += 1
        continue
    if newline == 0:
        temp = [(line[i:i+4].strip()) for i in range(0, len(line), 4)]
        temp = [(re.sub(r"[\[\]]", "", i)) for i in temp]
        head.append(temp)
    else:
        temp = [int(i) for i in line.split() if i.isdigit()]
        data.append(temp)
head = head[:-1]
dataset = []
for i in range(0, len(head[0])):
    dataset.append([(a[i]) for a in head if a[i] != ""])
part1 = deepcopy(dataset)
part2 = deepcopy(dataset)


#Part1
for line in data:
    a, s, d = line
    craves = part1[s-1][:a]
    part1[s-1] = part1[s-1][a:]
    part1[d-1] = list(reversed(craves)) + part1[d-1]
total = ""
for line in part1:
    total += line[0]
print(total)


#Part2
for line in data:
    a, s, d = line
    craves = part2[s-1][:a]
    part2[s-1] = part2[s-1][a:]
    part2[d-1] = craves + part2[d-1]
total = ""
for line in part2:
    total += line[0]
print(total)
