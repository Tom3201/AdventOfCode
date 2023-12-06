from functools import reduce

with open("data.txt") as f:
    data = f.read().splitlines()

times = []
distances = []
for i, line in enumerate(data):
    for item in line.split(" "):
        if item.isdigit() and i == 0:
            times.append(int(item))
        elif item.isdigit() and i == 1:
            distances.append(int(item))

# Part 1
total = []
for i, time in enumerate(times):
    ways = 0
    for j in range(1, time + 1):
        if (time - j) * j > distances[i]:
            ways += 1
    total.append(ways)
print(reduce(lambda x, y: x * y, total))

# Part 2
ways = 0
new_time = 0
new_distance = 0
for i in range(0, len(times)):
    new_time = int(f"{new_time}{times[i]}")
    new_distance = int(f"{new_distance}{distances[i]}")

for j in range(1, new_time + 1):
    if (new_time - j) * j > new_distance:
        ways += 1
print(ways)
