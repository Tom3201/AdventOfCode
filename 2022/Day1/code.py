with open("data.txt") as f:
    data = f.read().splitlines()


#Part 1
elves = []
total = 0
for calory in data:
    if not calory:
        elves.append(total)
        total = 0
        continue
    total += int(calory)
print(max(elves))


#Part 2
top = 3
total = 0
for t in range(top):
    total += max(elves)
    elves.remove(max(elves))
print(total)