import copy

with open("data.txt") as f:
    data = f.read().splitlines()

def search(data, search_value):
    for line in data:
        if line == search_value:
            return True
    return False

acc = 0
idx = 0
index_list = []
while not search(index_list, idx):
    if idx < (len(data) - 1):
        op, value = data[idx].split()
        index_list.append(idx)

        if op == "nop":
            idx += 1
        elif op == "jmp":
            idx += int(value)
        elif op == "acc":
            acc += int(value)
            idx += 1
    else:
        print('Index value out of range: ' + str(idx) + '/' + str(len(data)))
        exit()
print(acc)

for i in range(len(data)):
    new_data = copy.deepcopy(data)
    if new_data[i].split()[0] == "jmp":
        new_data[i] = new_data[i].replace("jmp", "nop")
    elif new_data[i].split()[0] == "nop":
        new_data[i] = new_data[i].replace("nop", "jmp")

    acc = 0
    idx = 0
    index_list = []
    while not search(index_list, idx):
        op, value = new_data[idx].split()
        index_list.append(idx)

        if op == "nop":
            idx += 1
        elif op == "jmp":
            idx += int(value)
        elif op == "acc":
            acc += int(value)
            idx += 1

        if idx == (len(new_data) - 1):
            print(acc)
            break
