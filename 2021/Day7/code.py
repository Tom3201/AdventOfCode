with open("data.txt") as f:
    data = f.read().split(',')

sorted_data = []
for line in data:
    sorted_data.append(int(line))
sorted_data.sort()

#Part 1
ans = 0
median = sorted_data[len(sorted_data) // 2]
for line in sorted_data:
    ans += abs(line - median)
print(ans)

#Part 2
best = 0
for median in range(len(sorted_data)):
    fuel_cost = 0
    for line in sorted_data:
        fuel_cost += int(abs(line - median) * (abs(line - median) + 1) / 2)
    if median == 0:
        best = fuel_cost
    elif fuel_cost < best:
        best = fuel_cost
print(best)