from collections import deque

with open("data.txt") as f:
    data = f.read().splitlines()

start_row, start_col = next((a, b) for a, row in enumerate(data) for b, ch in enumerate(row) if ch == "S")

# Part 1
total = set()
seen = {(start_row, start_col)}
steps = 64
queue = deque([(start_row, start_col, steps)])
while queue:
    row, col, step = queue.popleft()

    if step % 2 == 0:
        total.add((row, col))
    if step == 0:
        continue

    for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if next_row < 0 or next_row >= len(data) or next_col < 0 or next_col >= len(data[0]) or data[next_row][next_col] == "#" or (next_row, next_col) in seen:
            continue
        seen.add((next_row, next_col))
        queue.append((next_row, next_col, step - 1))
print(len(total))


# Part 2
def fill(row, col, step):
    ans = set()
    seen = {(row, col)}
    queue = deque([(row, col, step)])

    while queue:
        row, col, step = queue.popleft()

        if step % 2 == 0:
            ans.add((row, col))
        if step == 0:
            continue
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if next_row < 0 or next_row >= len(data) or next_col < 0 or next_col >= len(data[0]) or data[next_row][next_col] == "#" or (next_row, next_col) in seen:
                continue
            seen.add((next_row, next_col))
            queue.append((next_row, next_col, step - 1))
    return len(ans)


size = len(data)
steps = 26501365
odd = (steps // size - 1 // 2 * 2 + 1) ** 2
even = ((steps // size - 1 + 1) // 2 * 2) ** 2

odd_points = fill(start_row, start_col, size * 2 + 1)
even_points = fill(start_row, start_col, size * 2)
corner_right = fill(start_row, 0, size - 1)
corner_bottom = fill(0, start_col, size - 1)
corner_left = fill(start_row, size - 1, size - 1)
corner_top = fill(size - 1, start_col, size - 1)
small_top_left = fill(size - 1, size - 1, size // 2 - 1)
small_top_right = fill(size - 1, 0, size // 2 - 1)
small_bottom_left = fill(0, size - 1, size // 2 - 1)
small_bottom_right = fill(0, 0, size // 2 - 1)
large_top_left = fill(size - 1, size - 1, size * 3 // 2 - 1)
large_top_right = fill(size - 1, 0, size * 3 // 2 - 1)
large_bottom_left = fill(0, size - 1, size * 3 // 2 - 1)
large_bottom_right = fill(0, 0, size * 3 // 2 - 1)

print(odd * odd_points + even * even_points + corner_top + corner_right + corner_bottom + corner_left + (steps // size - 1 + 1) * (small_top_right + small_top_left + small_bottom_right + small_bottom_left) + steps // size - 1 * (large_top_right + large_top_left + large_bottom_right + large_bottom_left))
