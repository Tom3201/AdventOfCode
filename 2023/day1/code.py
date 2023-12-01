with open("data.txt") as f:
    data = f.read().splitlines()

# Part 1
total = 0
for line in data:
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)
    total += int(f"{numbers[0]}{numbers[len(numbers)-1]}")
print(total)

# Part 2
total = 0
units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    numbers = []
    for i, unit in enumerate(units):
        templine = line
        while unit in templine:
            number = {"num": 0, "pos": 0}
            number["num"] = i + 1
            number["pos"] = templine.find(unit)
            numbers.append(number)
            templine = templine.replace(unit, f"{'.'*len(unit)}", 1)
    for i, char in enumerate(line):
        if not char.isdigit():
            continue
        numbers.append({"num": int(char), "pos": i})
    numbers = sorted(numbers, key=lambda num: num["pos"])
    total += int(f"{numbers[0]['num']}{numbers[-1]['num']}")
print(total)
