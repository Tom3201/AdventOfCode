with open("data.txt") as f:
    data = f.read().splitlines()


#Part1
total = 0
for line in data:
    elve1, elve2 = line.split(",")
    elve1min = int(elve1.split("-")[0])
    elve1max = int(elve1.split("-")[1])
    elve2min = int(elve2.split("-")[0])
    elve2max = int(elve2.split("-")[1])
    if (
        elve2min >= elve1min and elve2max <= elve1max or
        elve1min >= elve2min and elve1max <= elve2max
    ):
        total += 1
print(total)


#Part2
total = 0
for line in data:
    elve1, elve2 = line.split(",")
    elve1min = int(elve1.split("-")[0])
    elve1max = int(elve1.split("-")[1])
    elve2min = int(elve2.split("-")[0])
    elve2max = int(elve2.split("-")[1])
    if (
        elve2min in range(elve1min, elve1max+1) or
        elve2max in range(elve1min, elve1max+1) or
        elve1min in range(elve2min, elve2max+1) or
        elve1max in range(elve2min, elve2max+1)
    ):
        total += 1
print(total)