from collections import defaultdict, Counter

with open("data.txt") as f:
    data = f.read().splitlines()

order = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

hands = defaultdict(int)
for line in data:
    hand, bid = line.split(" ")
    hands[hand] = int(bid)

# Part 1
hands_sorted = defaultdict(tuple)
for hand in hands.keys():
    points = 0
    chars = ""
    for char in hand:
        chars += chr(ord('1') + order[char])
    values = Counter(chars).values()
    if len(values) == 1:
        points += 7
    elif len(values) == 2:
        if max(values) == 4:
            points += 6
        elif max(values) == 3:
            points += 5
    elif len(values) == 3:
        if max(values) == 3:
            points += 4
        elif max(values) == 2:
            points += 3
    elif len(values) == 4:
        points += 2
    elif len(values) == 5:
        points += 1
    hands_sorted[hand] = (points, chars)
hands_sorted = sorted(hands_sorted, key=lambda k: hands_sorted[k])

total = 0
for i, hand in enumerate(hands_sorted):
    total += hands[hand] * (i + 1)
print(total)

# Part 2
order["J"] = 0
hands_sorted = defaultdict(tuple)
for hand in hands.keys():
    points = 0
    chars = ""
    for char in hand:
        chars += chr(ord('1') + order[char])
    counter = Counter(chars)
    highest_value = max(counter.keys())
    if counter[highest_value] < max(counter.values()):
        max_values = sorted(counter, key=lambda k: counter[k], reverse=True)
        if max_values[0] != "1":
            highest_value = max_values[0]
        elif len(max_values) > 1:
            highest_value = max_values[1]
    if "1" in counter and highest_value != "1":
        counter[highest_value] += counter["1"]
        del counter["1"]

    values = counter.values()
    if len(values) == 1:
        points += 7
    elif len(values) == 2:
        if max(values) == 4:
            points += 6
        elif max(values) == 3:
            points += 5
    elif len(values) == 3:
        if max(values) == 3:
            points += 4
        elif max(values) == 2:
            points += 3
    elif len(values) == 4:
        points += 2
    elif len(values) == 5:
        points += 1
    hands_sorted[hand] = (points, chars)
hands_sorted = sorted(hands_sorted, key=lambda k: hands_sorted[k])

total = 0
for i, hand in enumerate(hands_sorted):
    total += hands[hand] * (i + 1)
print(total)
