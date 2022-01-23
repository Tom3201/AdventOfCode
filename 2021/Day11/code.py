data = []
for line in open("data.txt"):
    data.append([int(x) for x in line.strip()])

y_length = len(data)
x_length = len(data[0])
ans = 0
def flash(y, x):
    global ans
    yx_range = [-1, 0, 1]
    ans += 1
    data[y][x] = -1
    for y_range in yx_range:
        for x_range in yx_range:
            new_y = y + y_range
            new_x = x + x_range
            if 0 <= new_y < y_length and 0 <= new_x < x_length and data[new_y][new_x] != -1:
                data[new_y][new_x] += 1
                if data[new_y][new_x] > 9:
                    flash(new_y, new_x)

counter = 0
all_flash = False
while not all_flash:
    counter += 1
    for y in range(y_length):
        for x in range(x_length):
            data[y][x] += 1
    for y in range(y_length):
        for x in range(x_length):
            if data[y][x] == 10:
                flash(y, x)
    all_flash = True
    for y in range(y_length):
        for x in range(x_length):
            if data[y][x] == -1:
                data[y][x] = 0
            else:
                all_flash = False
    # Part1
    if counter == 100:
        print(ans)
#Part2
print(counter)