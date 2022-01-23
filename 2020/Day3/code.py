f = open("data.txt")
data = [line.replace('\n','') for line in f]

def count_trees(data, down, right):
    pos_down = 0
    pos_right = 0
    trees = 0
    for index in range(len(data)):
        if index == pos_down:
            if data[pos_down][pos_right] == "#":
                trees += 1
            pos_right = (pos_right + right) % len(data[0])
            pos_down = pos_down + down
    return trees

print(int(count_trees(data, 1, 1)) * int(count_trees(data, 1, 3)) * int(count_trees(data, 1, 5)) * int(count_trees(data, 1, 7)) * int(count_trees(data, 2, 1)))