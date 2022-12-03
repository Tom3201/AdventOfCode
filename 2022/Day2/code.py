with open("data.txt") as f:
    data = f.read().splitlines()


#Part1
strategy = {"win": {"A": "Y", "B": "Z", "C": "X"}, "draw": {"A": "X", "B": "Y", "C": "Z"}, "loss": {"A": "Z", "B": "X", "C": "Y"}}
points = {"win": 6, "draw": 3, "loss": 0, "X": 1, "Y": 2, "Z": 3}
total = 0
for line in data:
    match = line.split(" ")
    if strategy["win"][match[0]] == match[1]:
        total += points["win"]
        total += points[match[1]]
    elif strategy["draw"][match[0]] == match[1]:
        total += points["draw"]
        total += points[match[1]]
    else:
        total += points["loss"]
        total += points[match[1]]
print(total)


#Part2
guide = {"X": "loss", "Y": "draw", "Z": "win"}
total = 0
for line in data:
    match = line.split(" ")
    total += points[guide[match[1]]]
    total += points[strategy[guide[match[1]]][match[0]]]
print(total)