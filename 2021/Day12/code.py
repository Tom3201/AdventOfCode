from collections import defaultdict, deque

data = []
with open("data.txt") as f:
    data = f.read().splitlines()

paths = defaultdict(list)
for line in data:
    a,b = line.split('-')
    paths[a].append(b)
    paths[b].append(a)

part1 = True
for i in range(2):
    start = ('start', set(['start']), None)
    ans = 0
    queue = deque([start])
    while queue:
        pos, small, twice = queue.popleft()
        if pos == 'end':
            ans += 1
            continue
        for y in paths[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                queue.append((y, new_small, twice))
            elif y in small and twice == None and y not in ['start', 'end'] and not part1:
                queue.append((y, small, y))
    part1 = False
    print(ans)
