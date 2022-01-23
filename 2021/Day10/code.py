with open("data.txt") as f:
    data = f.read().splitlines()

characters = [
    ['(', ')'],
    ['[', ']'],
    ['{', '}'],
    ['<', '>']
]

point_list_part1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

point_list_part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

points_part1 = 0
points_part2 = []
for line in data:
    open_chars = []
    part2 = True
    for ch in line:
        for character in characters:
            if ch in character[0]:
                open_chars.append(ch)
            elif ch in character[1] and open_chars.pop() != character[0]:
                points_part1 += point_list_part1.get(ch)
                part2 = False
    
    if part2:
        added_chars = []
        points = 0
        for ch in open_chars[::-1]:
            for character in characters:
                if ch in character[0]:
                    added_chars.append(character[1])
                    points = points * 5 + point_list_part2.get(character[1], 0)
        points_part2.append(points)

points_part2.sort()
print(points_part1)
print(points_part2[len(points_part2) // 2])
