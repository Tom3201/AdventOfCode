with open("data.txt") as f:
    data = f.read().splitlines()


trees = []
neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for line in data:
    row = []
    for digit in line:
        row.append(int(digit))
    trees.append(row)


#Part1
total = 0
for a, row in enumerate(trees):
    for b, tree in enumerate(row):
        if (
            a == 0 or a == len(trees)-1 or
            b == 0 or b == len(row)-1 or
            max(trees[a][:b]) < tree or
            max(trees[a][b+1:]) < tree or
            max([t[b] for t in trees[:a]]) < tree or
            max([t[b] for t in trees[a+1:]]) < tree
        ):
            total += 1
print(total)


#Part2
total = 0
for a, row in enumerate(trees):
    for b, tree in enumerate(row):
        score = 1
        for da, db in neighbors:
            dist = 0
            na = a + da
            nb = b + db
            while (
                na >= 0 and na < len(trees) and
                nb >= 0 and nb < len(row) and
                trees[na][nb] < tree
            ):
                dist += 1
                na += da
                nb += db
                if (
                    na >= 0 and na < len(trees) and
                    nb >= 0 and nb < len(row) and
                    trees[na][nb] >= tree
                ):
                    dist += 1
            score *= dist
        total = max(score, total)
print(total)
