from collections import deque

with open("data.txt") as file:
    rules_data, parts_data = file.read().strip().split('\n\n')

rules = {}
for rule in rules_data.splitlines():
    name, conditions = rule.replace('}', '').split('{')
    rules[name] = conditions

# Part 1
total = 0
for part_data in parts_data.splitlines():
    part = {x.split('=')[0]: int(x.split('=')[1]) for x in part_data[1:-1].split(',')}
    current_state = "in"
    response = ""
    while response not in ["A", "R"]:
        rule_conditions = rules[current_state]
        for condition in rule_conditions.split(','):
            condition_applies = True
            response = condition
            if ":" in condition:
                condition_var, response = condition.split(':')
                var_name = condition_var[0]
                operation = condition_var[1]
                threshold = int(condition_var[2:])
                if operation == ">":
                    condition_applies = part[var_name] > threshold
                else:
                    condition_applies = part[var_name] < threshold
            if condition_applies:
                if response == "A":
                    total += part["x"] + part["m"] + part["a"] + part["s"]
                current_state = response
                break
print(total)


# Part 2
def update_ranges(var, operation, threshold, *ranges):
    def update_range(operation, threshold, lower, upper):
        if operation == ">":
            lower = max(lower, threshold + 1)
        elif operation == "<":
            upper = min(upper, threshold - 1)
        elif operation == ">=":
            lower = max(lower, threshold)
        elif operation == "<=":
            upper = min(upper, threshold)
        return lower, upper

    if var == "x":
        ranges = update_range(operation, threshold, *ranges[:2]) + ranges[2:]
    elif var == "m":
        ranges = ranges[:2] + update_range(operation, threshold, *ranges[2:4]) + ranges[4:]
    elif var == "a":
        ranges = ranges[:4] + update_range(operation, threshold, *ranges[4:6]) + ranges[6:]
    elif var == "s":
        ranges = ranges[:6] + update_range(operation, threshold, *ranges[6:])
    return ranges


total = 0
queue = deque([("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
while queue:
    current_state, xl, xh, ml, mh, al, ah, sl, sh = queue.pop()
    if xl > xh or ml > mh or al > ah or sl > sh:
        continue
    if current_state == "A":
        current_combinations = (xh - xl + 1) * (mh - ml + 1) * (ah - al + 1) * (sh - sl + 1)
        total += current_combinations
        continue
    elif current_state == "R":
        continue
    rule_conditions = rules[current_state]
    for condition in rule_conditions.split(','):
        condition_applies = True
        response = condition
        if ':' in condition:
            condition_var, response = condition.split(':')
            var_name = condition_var[0]
            operation = condition_var[1]
            threshold = int(condition_var[2:])
            queue.append((response, *update_ranges(var_name, operation, threshold, xl, xh, ml, mh, al, ah, sl, sh)))
            xl, xh, ml, mh, al, ah, sl, sh = update_ranges(var_name, "<=" if operation == ">" else ">=", threshold, xl, xh, ml, mh, al, ah, sl, sh)
            continue
        queue.append((response, xl, xh, ml, mh, al, ah, sl, sh))
        break
print(total)
