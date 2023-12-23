with open("data.txt") as f:
    data = f.read().splitlines()

start = (0, data[0].index("."))
end = (len(data) - 1, data[-1].index("."))

points = [start, end]

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "#":
            continue
        neighbors = 0
        for next_row, next_col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= next_row < len(data) and 0 <= next_col < len(data[0]) and data[next_row][next_col] != "#":
                neighbors += 1
        if neighbors >= 3:
            points.append((r, c))


def depth_first(seen, pt):
    if pt == end:
        return 0

    m = -float("inf")
    seen.add(pt)
    for next in graph[pt]:
        if next not in seen:
            m = max(m, depth_first(seen, next) + graph[pt][next])
    seen.remove(pt)
    return m


# Part 1
graph = {pt: {} for pt in points}
directions = {"^": [(-1, 0)], "v": [(1, 0)], "<": [(0, -1)], ">": [(0, 1)], ".": [(-1, 0), (1, 0), (0, -1), (0, 1)]}
for start_row, start_col in points:
    stack = [(0, start_row, start_col)]
    seen = {(start_row, start_col)}
    while stack:
        n, row, col = stack.pop()
        if n != 0 and (row, col) in points:
            graph[(start_row, start_col)][(row, col)] = n
            continue
        for dest_row, dest_col in directions[data[row][col]]:
            next_row = row + dest_row
            next_col = col + dest_col
            if 0 <= next_row < len(data) and 0 <= next_col < len(data[0]) and data[next_row][next_col] != "#" and (next_row, next_col) not in seen:
                stack.append((n + 1, next_row, next_col))
                seen.add((next_row, next_col))

seen = set()
print(depth_first(seen, start))

# Part 2
graph = {pt: {} for pt in points}
for start_row, start_col in points:
    stack = [(0, start_row, start_col)]
    seen = {(start_row, start_col)}
    while stack:
        n, row, col = stack.pop()
        if n != 0 and (row, col) in points:
            graph[(start_row, start_col)][(row, col)] = n
            continue
        for dest_row, dest_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = row + dest_row
            next_col = col + dest_col
            if 0 <= next_row < len(data) and 0 <= next_col < len(data[0]) and data[next_row][next_col] != "#" and (next_row, next_col) not in seen:
                stack.append((n + 1, next_row, next_col))
                seen.add((next_row, next_col))
seen = set()
print(depth_first(seen, start))
