from collections import defaultdict

with open("data.txt") as f:
    data = f.read().split(',')

new_data = []
for i in data:
    new_data.append(int(i))

day = 0
max_days = 80
for day in range(max_days):
    new_num = 0
    for index, num in enumerate(new_data):
        if num == 0:
            new_data[index] += 7
            new_num += 1
        new_data[index] -= 1
    if new_num > 0:
        for i in range(new_num):
            new_data.append(8)

print(len(new_data))

old_fishs = defaultdict(int)
for n in data:
    n = int(n)
    if n not in old_fishs:
        old_fishs[n] = 0
    old_fishs[n] += 1

for day in range(256):
    new_fishs = defaultdict(int)
    for x, count_value in old_fishs.items():
        if x==0:
            new_fishs[6] += count_value
            new_fishs[8] += count_value
        else:
            new_fishs[x - 1] += count_value
    old_fishs = new_fishs
print(sum(old_fishs.values()))