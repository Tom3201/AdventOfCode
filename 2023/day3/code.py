with open("data.txt") as f:
    data = f.read().splitlines()

# Part 1
neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
total = 0
for a, line in enumerate(data):
    number = 0
    part = False
    for b, num in enumerate(line):
        if num.isdigit():
            number = int(str(number) + num)
        else:
            part = False
            number = 0
            continue
        for da, db in neighbors:
            na = a + da
            nb = b + db
            if na >= 0 and na < len(data) and nb >= 0 and nb < len(line):
                if not data[na][nb].isdigit() and data[na][nb] != ".":
                    part = True
        if b + 1 < len(line) and line[b + 1].isdigit():
            continue
        if part:
            total += number
print(total)

# Part 2
total = 0
for row_index, row in enumerate(data):
    for col_index, char in enumerate(row):
        if char != "*":
            continue
        cells = set()
        for neighbor_row in [row_index - 1, row_index, row_index + 1]:
            for neighbor_col in [col_index - 1, col_index, col_index + 1]:
                if neighbor_row < 0 or neighbor_row >= len(data) or neighbor_col < 0 or neighbor_col >= len(data[neighbor_row]) or not data[neighbor_row][neighbor_col].isdigit():
                    continue
                while neighbor_col > 0 and data[neighbor_row][neighbor_col - 1].isdigit():
                    neighbor_col -= 1
                cells.add((neighbor_row, neighbor_col))
        if len(cells) != 2:
            continue

        neighbor_sums = []
        for neighbor_row, neighbor_col in cells:
            neighbor_value = ""
            while neighbor_col < len(data[neighbor_row]) and data[neighbor_row][neighbor_col].isdigit():
                neighbor_value += data[neighbor_row][neighbor_col]
                neighbor_col += 1
            neighbor_sums.append(int(neighbor_value))
        total += neighbor_sums[0] * neighbor_sums[1]
print(total)
