with open("data.txt") as f:
    data = f.read().splitlines()


def generate_combinations(pattern, numbers, memo, dot_index=0, block_index=0, current_block=0):
    key = (dot_index, block_index, current_block)
    if key in memo:
        return memo[key]

    if dot_index == len(pattern):
        if (block_index == len(numbers) and current_block == 0) or (block_index == len(numbers) - 1 and numbers[block_index] == current_block):
            return 1
        return 0

    total_combinations = 0
    for char in ['.', '#']:
        if pattern[dot_index] == char or pattern[dot_index] == '?':
            if char == '.' and current_block == 0:
                total_combinations += generate_combinations(pattern, numbers, memo, dot_index + 1, block_index, 0)
            elif char == '.' and current_block > 0 and block_index < len(numbers) and numbers[block_index] == current_block:
                total_combinations += generate_combinations(pattern, numbers, memo, dot_index + 1, block_index + 1, 0)
            elif char == '#':
                total_combinations += generate_combinations(pattern, numbers, memo, dot_index + 1, block_index, current_block + 1)

    memo[key] = total_combinations
    return total_combinations


# Part 1
total = 0
for line in data:
    memo = {}
    pattern = line.split(" ")[0]
    numbers = [int(x) for x in line.split(" ")[1].split(",")]
    total += generate_combinations(pattern, numbers, memo)
print(total)

# Part 2
total = 0
for line in data:
    memo = {}
    pattern = '?'.join([line.split(" ")[0]] * 5)
    numbers = [int(x) for x in line.split(" ")[1].split(",")] * 5
    total += generate_combinations(pattern, numbers, memo)
print(total)
