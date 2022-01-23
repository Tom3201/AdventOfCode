from copy import deepcopy

with open("data.txt") as f:
  data = f.read().splitlines()

#Part 1
gamma_rate = ""
epsilon_rate = ""
for i in range(0, len(data[0])):
  avg_0 = 0
  avg_1 = 0
  for index, line in enumerate(data):
    if line[i] == "0":
      avg_0 += 1
    elif line[i] == "1":
      avg_1 += 1
  if avg_0 > avg_1:
    gamma_rate += "0"
    epsilon_rate += "1"
  elif avg_0 < avg_1:
    gamma_rate += "1"
    epsilon_rate += "0"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

#Part 2
oxygen_generator_rating = deepcopy(data)
for i in range(0, len(oxygen_generator_rating[0])):
  avg_0 = 0
  avg_1 = 0
  avg_0_index = []
  avg_1_index = []
  for index, line in enumerate(oxygen_generator_rating):
    if line[i] == "0":
      avg_0 += 1
      avg_0_index.append(line)
    elif line[i] == "1":
      avg_1 += 1
      avg_1_index.append(line)
  if avg_0 > avg_1:
    for j in avg_1_index:
      oxygen_generator_rating.remove(j)
  elif avg_0 < avg_1:
    for j in avg_0_index:
      oxygen_generator_rating.remove(j)
  else:
    for j in avg_0_index:
      oxygen_generator_rating.remove(j)

scrubber_rating = deepcopy(data)
for i in range(0, len(scrubber_rating[0])):
  avg_0 = 0
  avg_1 = 0
  avg_0_index = []
  avg_1_index = []
  for index, line in enumerate(scrubber_rating):
    if line[i] == "0":
      avg_0 += 1
      avg_0_index.append(line)
    elif line[i] == "1":
      avg_1 += 1
      avg_1_index.append(line)
  if len(scrubber_rating) == 1:
    break
  elif avg_0 > avg_1:
    for j in avg_0_index:
      scrubber_rating.remove(j)
  elif avg_0 < avg_1:
    for j in avg_1_index:
      scrubber_rating.remove(j)
  else:
    for j in avg_1_index:
      scrubber_rating.remove(j)

print(int(oxygen_generator_rating[0], 2) * int(scrubber_rating[0], 2))
