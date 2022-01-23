import re

data = []
with open("data.txt") as f:
    data = f.readlines()
RGX = '([0-9]+)-([0-9]+) ([a-z]): (.*)'
valid = 0
valid2 = 0
for line in data:
    line = re.search(RGX, line)
    min_amount = int(line.group(1))
    max_amount = int(line.group(2))
    letter = line.group(3)
    password = line.group(4)
    counter = password.count(letter)
    if counter >= min_amount and counter <= max_amount:
        valid += 1
    if password[min_amount - 1] == letter and not password[max_amount - 1] == letter or password[max_amount - 1] == letter and not password[min_amount - 1] == letter:
        valid2 += 1
print(valid)
print(valid2)