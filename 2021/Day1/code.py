with open("data.txt") as f:
    data = f.read().splitlines()

#Part 1
increased = 0
for index in range(len(data)):
    if int(data[index]) > int(data[index - 1]):
        increased += 1
print(increased)

#Part 2
curr_sum = 0
prev_sum = 0
count = 0
for index in range(len(data)):
    if index + 2 > len(data) - 1:
        break 
    prev_sum = curr_sum
    curr_sum = int(data[index]) + int(data[index + 1]) + int(data[index + 2])
    if curr_sum > prev_sum and index > 0:
        count += 1
print(count)