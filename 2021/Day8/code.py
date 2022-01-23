with open("data.txt") as f:
    data = f.read().splitlines()

new_data = []
for line in data:
    lines = line.split('|')
    for line in lines:
        new_data += line.split()

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

letter_count = ['a','b','c','d','e','f','g']
pattern = [[True, True, True, True, True, False, True],
        [True, True, False, False, False, False, False],
        [True, False, True, True, False, True, True],
        [True, True, True, True, False, False, False],
        [True, True, False, False, True, True, False],
        [False, True, True, True, True, True, False],
        [False, True, True, True, True, True, True],
        [True, True, False, True, False, False, False],
        [True, True, True, True, True, True, True],
        [True, True, True, True, True, True, False]]

count = 0
counter = 0
ans = 0
nums = []
for line in new_data:
    digit = [False for _ in range(7)]

    if len(line) == 2:
        digit = [True, True, False, False, False, False, False]
        count += 1
    elif len(line) == 4:
        digit = [True, True, False, False, True, True, False]
        count += 1
    elif len(line) == 3:
        digit = [True, True, False, True, False, False, False]
        count += 1
    elif len(line) == 7:
        digit = [True, True, True, True, True, True, True]
        count += 1
    else:
        for letter in line:
            digit[letter_count.index(letter)] = True

    if counter == 14:
        counter = 0
        nums = []

    if counter < 10:
        for i, p in enumerate(pattern):
            if p == digit:
                nums.append(i)
    elif counter >= 10:
        print(line)
        for i, p in enumerate(pattern):
            if p == digit:
                lol = True
                print(i)
    counter += 1

    length = len(line)
    if length == 2 or length == 3 or length == 4 or length == 7:
        count += 1

    # for i, p in enumerate(pattern):
    #     if counter == 4:
    #         ans += int(num)
    #         num = ""
    #         counter = 0
    #     if p == digit:
    #         num += str(i)
    #         counter += 1
    #         break
print(count)
print(ans)



# def get_input():
#     in_val = []
#     out_val = []
#     with open('data.txt', 'r') as file:
#         for line in file:
#             in_val.append(line.strip().split(' | ')[0].split(' '))
#             out_val.append(line.strip().split(' | ')[1].split(' '))
#     return in_val, out_val

# digits = {
#     '0': None,
#     '1': None,
#     '2': None,
#     '3': None,
#     '4': None,
#     '5': None,
#     '6': None,
#     '7': None,
#     '8': set('abcdefg'),
#     '9': None
#     }


# in_val, out_val = get_input()
# results = []

# for index, iv in enumerate(in_val):
#     digits['1'] = set(list(filter(lambda x: len(x) == 2, iv))[0])
#     digits['4'] = set(list(filter(lambda x: len(x) == 4, iv))[0])
#     digits['7'] = set(list(filter(lambda x: len(x) == 3, iv))[0])
#     seg_b_d = digits['1'] ^ digits['4']
#     seg_e_g = (digits['7'] | digits['4']) ^ digits['8']
#     seg_a = digits['7'] ^ digits['1']

#     six_segments = list(filter(lambda x: len(x) == 6, iv))
#     for d in six_segments:
#         if len(set(d) & seg_b_d) == 1:
#             digits['0'] = set(d)
#         elif len(set(d) & seg_e_g) == 1:
#             digits['9'] = set(d)
#         else:
#             digits['6'] = set(d)

#     seg_e = digits['8'] ^ digits['9']
#     seg_c = digits['8'] ^ digits['6']
#     seg_b = digits['0'] & seg_b_d 
#     seg_f = digits['1'] & digits['6']

#     digits['5'] = digits['9'] ^ seg_c 
#     digits['3'] = (digits['9'] ^ seg_b)
#     digits['2'] = (digits['8'] ^ seg_b) ^ seg_f

#     output = ''

#     for ov in out_val[index]:
#         for i in range(10):
#             if set(ov) == digits.get(str(i)):
#                 output += str(i)
#                 break
#     results.append(int(output))
# print(sum(results))