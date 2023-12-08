from collections import defaultdict
from math import lcm

with open("data.txt") as f:
    data = f.read().splitlines()

directions = ""
nodes = defaultdict(list)
for i, line in enumerate(data):
    if i == 0:
        directions = line
        continue
    if line != "":
        node, neighbors = line.split("=")
        neighbors = neighbors.replace("(", "").replace(")", "")
        nodes[node.strip()] = [s.strip() for s in neighbors.strip().split(",")]

# Part 1
start = "AAA"
end = "ZZZ"
current_pos = start
steps = 0
while current_pos != end:
    for direction in directions:
        steps += 1
        if current_pos == end:
            break
        if direction == "L":
            direction = 0
        elif direction == "R":
            direction = 1
        current_pos = nodes[current_pos][direction]
print(steps)

# Part 2
current_poses = []
for node in nodes.keys():
    if node.endswith("A"):
        current_poses.append(node)
total_steps = 0
steps = []
while all([True if current_pos.endswith("Z") else False for current_pos in current_poses]) is False:
    for direction in directions:
        total_steps += 1
        if direction == "L":
            direction = 0
        elif direction == "R":
            direction = 1
        for i, current_pos in enumerate(current_poses):
            if nodes[current_pos][direction].endswith("Z"):
                steps.append(total_steps)
            if current_pos.endswith("Z"):
                continue
            current_poses[i] = nodes[current_pos][direction]
total = 1
for step in steps:
    total = lcm(total, step)
print(total)
