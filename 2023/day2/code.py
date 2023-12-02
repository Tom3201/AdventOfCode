with open("data.txt") as f:
    data = f.read().splitlines()

# Part 1
red = 12
green = 13
blue = 14

total = 0
for line in data:
    game = line.split(" ")[1][:-1]
    results = line.split(":")[1].strip().split(";")
    valid = True
    for result in results:
        colors = result.split(",")
        for color in colors:
            value = int(color.strip().split(" ")[0])
            if "red" in color:
                maxval = red
            elif "green" in color:
                maxval = green
            else:
                maxval = blue
            if value > maxval:
                valid = False
    if valid:
        total += int(game)
print(total)

# Part 2
total = 0
for line in data:
    game = line.split(" ")[1][:-1]
    results = line.split(":")[1].strip().split(";")
    maxred = 0
    maxgreen = 0
    maxblue = 0
    for result in results:
        colors = result.split(",")
        for color in colors:
            value = int(color.strip().split(" ")[0])
            if "red" in color:
                if value > maxred:
                    maxred = value
            elif "green" in color:
                if value > maxgreen:
                    maxgreen = value
            else:
                if value > maxblue:
                    maxblue = value
    total += maxred * maxgreen * maxblue
print(total)
