with open("data.txt") as f:
    data, rules = f.read().split('\n\n')

R = {}
for line in rules.splitlines():
    start, end = line.split(' -> ')
    R[start] = end