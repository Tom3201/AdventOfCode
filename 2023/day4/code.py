from collections import defaultdict

with open("data.txt") as f:
    data = f.read().splitlines()


def parse_card(card):
    win_nums = []
    card_nums = []
    pipe = False
    for x in card.split(":")[1].split(" "):
        if x.isdigit():
            if pipe:
                card_nums.append(int(x))
            else:
                win_nums.append(int(x))
            continue
        if x == "|":
            pipe = True
    return win_nums, card_nums


# Part 1
total = 0
for card in data:
    win_nums, card_nums = parse_card(card)
    points = 0
    for num in card_nums:
        if num in win_nums:
            if points > 0:
                points = points * 2
                continue
            points += 1
    total += points
print(total)


# Part 2
total = 0
total_points = defaultdict(int)
for i, card in enumerate(data):
    total_points[i] += 1
    win_nums, card_nums = parse_card(card)
    points = 0
    for num in card_nums:
        if num in win_nums:
            points += 1
    for j in range(points):
        total_points[i + 1 + j] += total_points[i]
print(sum(total_points.values()))
