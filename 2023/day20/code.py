from math import gcd
from collections import defaultdict, deque

data = open("data.txt").read().strip().split('\n')
grid = [[c for c in row] for row in data]
num_rows = len(grid)
num_cols = len(grid[0])


def adjust_variable(variable):
    if variable in type_mapping:
        return type_mapping[variable] + variable
    else:
        return variable


def calculate_lcm(numbers):
    ans = 1
    for x in numbers:
        ans = (ans * x) // gcd(x, ans)
    return ans


type_mapping = {}
rules = {}
for line in data:
    source, destination = line.split('->')
    source = source.strip()
    destination = destination.strip()
    destination = destination.split(', ')
    rules[source] = destination
    type_mapping[source[1:]] = source[0]

dependencies = {}
inverse_dependencies = defaultdict(list)
for x, ys in rules.items():
    rules[x] = [adjust_variable(y) for y in ys]
    for y in rules[x]:
        if y[0] == '&':
            if y not in dependencies:
                dependencies[y] = {}
            dependencies[y][x] = 'lo'
        inverse_dependencies[y].append(x)

watch_list = inverse_dependencies[inverse_dependencies['rx'][0]]
low_count = 0
high_count = 0
queue = deque()
on_set = set()
previous_timestamps = {}
count = defaultdict(int)
to_lcm = []
total = 0
for current_timestamp in range(1, 10**8):
    queue.append(('broadcaster', 'button', 'lo'))

    while queue:
        current_node, from_node, node_type = queue.popleft()

        if node_type == 'lo':
            if current_node in previous_timestamps and count[current_node] == 2 and current_node in watch_list:
                to_lcm.append(current_timestamp - previous_timestamps[current_node])
            previous_timestamps[current_node] = current_timestamp
            count[current_node] += 1
        if len(to_lcm) == len(watch_list):
            total = calculate_lcm(to_lcm)
            break

        if node_type == 'lo':
            low_count += 1
        else:
            high_count += 1

        if current_node not in rules:
            continue
        if current_node == 'broadcaster':
            for next_node in rules[current_node]:
                queue.append((next_node, current_node, node_type))
        elif current_node[0] == '%':
            if node_type == 'hi':
                continue
            if current_node not in on_set:
                on_set.add(current_node)
                new_type = 'hi'
            else:
                on_set.discard(current_node)
                new_type = 'lo'
            for next_node in rules[current_node]:
                queue.append((next_node, current_node, new_type))
        elif current_node[0] == '&':
            dependencies[current_node][from_node] = node_type
            new_type = ('lo' if all(value == 'hi' for value in dependencies[current_node].values()) else 'hi')
            for next_node in rules[current_node]:
                queue.append((next_node, current_node, new_type))

    # Part 1
    if current_timestamp == 1000:
        print(low_count * high_count)

    # Part 2
    if total > 0:
        print(total)
        break
