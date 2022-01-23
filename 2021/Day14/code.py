from collections import Counter

data, rules = open("data.txt").read().split('\n\n')
R = {}
for line in data.strip().split('\n'):
    start,end = line.strip().split(' -> ')
    R[start] = end

C1 = Counter()
for i in range(len(S)-1):
    C1[data[i]+data[i+1]] += 1

for t in range(41):
    if t in [10,40]:
        CF = Counter()
        for k in C1:
            CF[k[0]] += C1[k]
        CF[data[-1]] += 1
        print(max(CF.values())-min(CF.values()))

    C2 = Counter()
    for k in C1:
        C2[k[0]+R[k]] += C1[k]
        C2[R[k]+k[1]] += C1[k]
    C1 = C2