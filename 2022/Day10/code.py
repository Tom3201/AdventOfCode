with open("data.txt") as f:
    data = f.read().splitlines()


def checkCycle(c, x, t):
    if abs(x - ((c-1)%40)) < 2:
        grid[(c-1)//40][(c-1)%40] = '#'
    if c in [20, 60, 100, 140, 180, 220]:
        t += c * x
    return t


#Part2
global grid
grid = [[' ' for _ in range(40)] for _ in range(6)]


#Part1
cycle = 0
x = 1
total = 0
for line in data:
    if line == "noop":
        cycle += 1
        total = checkCycle(cycle, x, total)
    elif "add" in line:
        _, v = line.split()
        cycle += 1
        total = checkCycle(cycle, x, total)
        cycle += 1
        total = checkCycle(cycle, x, total)
        x += int(v)
print(total)


#Part2
for a in range(len(grid)):
    print(''.join(grid[a]))
