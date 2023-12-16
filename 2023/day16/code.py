data = open("data.txt").read().strip().split('\n')
grid = [[cell for cell in row] for row in data]


def count_seen_cells(grid, start_row, start_col, start_direction):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def step(row, col, direction):
        return row + directions[direction][0], col + directions[direction][1], direction

    seen_cells = set()
    temp_cells = set()
    seen_cells.add((start_row, start_col, start_direction))
    queue = [(start_row, start_col, start_direction)]
    while True:
        temp_queue = []
        if not queue:
            break
        for (row, col, direction) in queue:
            if 0 <= row < rows and 0 <= col < cols:
                seen_cells.add((row, col))
                if (row, col, direction) in temp_cells:
                    continue
                temp_cells.add((row, col, direction))
                char = grid[row][col]
                if char == ".":
                    temp_queue.append(step(row, col, direction))
                elif char == "/":
                    temp_queue.append(step(row, col, {0: 1, 1: 0, 2: 3, 3: 2}[direction]))
                elif char == "\\":
                    temp_queue.append(step(row, col, {0: 3, 1: 2, 2: 1, 3: 0}[direction]))
                elif char == "|":
                    if direction in [0, 2]:
                        temp_queue.append(step(row, col, direction))
                    else:
                        temp_queue.append(step(row, col, 0))
                        temp_queue.append(step(row, col, 2))
                elif char == "-":
                    if direction in [1, 3]:
                        temp_queue.append(step(row, col, direction))
                    else:
                        temp_queue.append(step(row, col, 1))
                        temp_queue.append(step(row, col, 3))
        queue = temp_queue
    return len(seen_cells) - 1


# Part 1
initial_score = count_seen_cells(grid, 0, 0, 1)
print(initial_score)

# Part 2
rows = len(grid)
cols = len(grid[0])
max_seen_cells = 0
for r in range(rows):
    max_seen_cells = max(max_seen_cells, count_seen_cells(grid, r, 0, 1))
    max_seen_cells = max(max_seen_cells, count_seen_cells(grid, r, cols - 1, 3))
for c in range(cols):
    max_seen_cells = max(max_seen_cells, count_seen_cells(grid, 0, c, 2))
    max_seen_cells = max(max_seen_cells, count_seen_cells(grid, rows - 1, c, 0))
print(max_seen_cells)
