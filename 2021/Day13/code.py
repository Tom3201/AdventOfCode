with open("data.txt") as f:
    data = f.read().splitlines()

part1 = True
Grid1 = {}
for line in data:
    if line and line.startswith('fold along'):
        Grid2 = {}
        instr = line.split()[-1]
        direction, value = instr.split('=')
        value = int(value)
        if direction == 'x':
            for (x, y) in Grid1:
                if x < value:
                    Grid2[(x, y)] = True
                else:
                    Grid2[(value - (x - value), y)] = True
        elif direction == 'y':
            for (x, y) in Grid1:
                if y < value:
                    Grid2[(x,y)] = True
                else:
                    Grid2[(x, value - (y - value))] = True
        Grid1 = Grid2
        if part1:
            part1 = False
            print(len(Grid1))
    elif line:
        x,y = [int(v) for v in line.split(',')]
        Grid1[(x,y)] = True

max_x = max([int(x) for x,y in Grid1.keys()])
max_y = max([int(y) for x,y in Grid1.keys()])

part2 = ''
for y in range(max_y + 1):
    for x in range(max_x + 1):
        part2 += ('x' if (x, y) in Grid1 else ' ')
    print(part2)
    part2 = ''