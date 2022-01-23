with open("data.txt") as f:
    data = f.read().splitlines()

new_data = []
for line in data:
    new_data.append(int(line))
new_data = sorted(new_data)

#Part 1
preamble = []
for line in new_data:
    if int(line) <= 25:
        preamble.append(int(line))
    else:
        possible = 0
        for i in preamble:
            for j in preamble:
                if not i == j and (i + j) == int(line):
                    possible = 1
        if possible == 1:
            preamble.append(int(line))
        elif possible == 0:
            target = line
            print(target)
            break

#Part 2
preamble = []
for i in range(0, len(data)):
    line = 0
    index = i
    while line < target:
        line += int(data[index])
        index += 1
    if line == target:
        print(int(min(data[i:index])) + int(max(data[i:index])))
        break