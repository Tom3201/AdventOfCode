with open("data.txt") as f:
    data = f.read().splitlines()

grid = []
for line in data:
    numbers = [int(x) for x in line.split(" ")]
    grid.append(numbers)

# Part 1
total_nums = 0
for numbers in grid:
    total = []
    total.append(numbers)
    calc_values = []
    while sum(total[len(total) - 1]) != 0:
        numbers = [j - i for i, j in zip(numbers[:-1], numbers[1:])]
        total.append(numbers)
    for i in range(len(total), 0, -1):
        if i == len(total):
            calc_values.append(0)
            continue
        new_number = total[i - 1][-1] + calc_values[-1]
        calc_values.append(new_number)
    total_nums += calc_values[-1]
print(total_nums)

# Part 2
total_nums = 0
for numbers in grid:
    total = []
    total.append(numbers)
    calc_values = []
    while sum(total[len(total) - 1]) != 0:
        numbers = [j - i for i, j in zip(numbers[:-1], numbers[1:])]
        total.append(numbers)
    for i in range(len(total), 0, -1):
        if i == len(total):
            calc_values.append(0)
            continue
        new_number = total[i - 1][0] - calc_values[-1]
        calc_values.append(new_number)
    total_nums += calc_values[-1]
print(total_nums)
