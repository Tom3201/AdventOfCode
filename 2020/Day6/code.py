from functools import reduce

with open('data.txt') as f:
    answers_mess = f.read().split('\n\n')

answers = []
for line in answers_mess:
    answers.append(line.replace('\n', ''))

group_sum = 0
for group in answers:
    group_sum = group_sum + len(set(group))
print(group_sum)

group_all_ans = 0
for group in answers_mess:
    group_all_ans = group_all_ans + len(reduce(set.intersection, map(set, group.split())))
print(group_all_ans)