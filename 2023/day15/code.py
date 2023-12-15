from collections import defaultdict

with open("data.txt") as f:
    data = f.read().splitlines()[0].split(",")

# Part 1
total = 0
for line in data:
    current_value = 0
    for char in line:
        ascii = ord(char)
        current_value += ascii
        current_value = (current_value * 17) % 256
    total += current_value
print(total)

# Part 2
boxes = defaultdict(list)
for line in data:
    current_value = 0
    for char in line.replace("-", "=").split("=")[0]:
        ascii = ord(char)
        current_value += ascii
        current_value = (current_value * 17) % 256
    if line[-1] == "-":
        boxes[current_value] = [(name, value) for (name, value) in boxes[current_value] if name != line[:-1]]
    elif "=" in line:
        if line[:line.index("=")] in [name for (name, _) in boxes[current_value]]:
            boxes[current_value] = [(name, int(line[line.index("=") + 1:]) if name == line[:line.index("=")] else value) for (name, value) in boxes[current_value]]
            continue
        boxes[current_value].append((line[:line.index("=")], int(line[line.index("=") + 1:])))

total = 0
for i in boxes:
    for j, (_, value) in enumerate(boxes[i]):
        total += (i + 1) * (j + 1) * value
print(total)
