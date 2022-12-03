import string


with open("data.txt") as f:
    data = f.read().splitlines()


#Part1
alphabet = list(string.ascii_letters)
total = 0
for line in data:
    part1, part2 = line[:int(len(line)/2)], line[int(len(line)/2):]
    for letter in part1:
        if letter in part2:
            total += alphabet.index(letter)+1
            break
print(total)


#Part2
rucksacks = []
total = 0
for line in data:
    rucksacks.append(line)
    if len(rucksacks) >= 3:
        for letter in rucksacks[0]:
            if letter in rucksacks[1] and letter in rucksacks[2]:
                total += alphabet.index(letter)+1
                rucksacks = []
                break
print(total)