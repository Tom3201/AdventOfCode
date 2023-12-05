with open("data.txt") as f:
    data = f.read().splitlines()

seeds = []
raw_seed_soil = []
raw_soil_fertilizer = []
raw_fertilizer_water = []
raw_water_light = []
raw_light_temperature = []
raw_temperature_humidity = []
raw_humidity_location = []

line_break = 0
for line in data:
    if "seeds" in line:
        seeds = [int(x) for x in line.split(":")[1].strip().split(" ")]
    if line == "":
        line_break += 1
        continue
    if ":" in line:
        continue
    if line_break == 1:
        raw_seed_soil.append([int(x) for x in line.split(" ")])
    elif line_break == 2:
        raw_soil_fertilizer.append([int(x) for x in line.split(" ")])
    elif line_break == 3:
        raw_fertilizer_water.append([int(x) for x in line.split(" ")])
    elif line_break == 4:
        raw_water_light.append([int(x) for x in line.split(" ")])
    elif line_break == 5:
        raw_light_temperature.append([int(x) for x in line.split(" ")])
    elif line_break == 6:
        raw_temperature_humidity.append([int(x) for x in line.split(" ")])
    elif line_break == 7:
        raw_humidity_location.append([int(x) for x in line.split(" ")])

# Part 1
lowest_location = -1
for seed in seeds:
    soil = seed
    for rule in raw_seed_soil:
        dest, source, range_len = rule
        if seed >= source and seed <= source + range_len:
            soil = dest - source + seed
            break
    fertilizer = soil
    for rule in raw_soil_fertilizer:
        dest, source, range_len = rule
        if soil >= source and soil <= source + range_len:
            fertilizer = dest - source + soil
            break
    water = fertilizer
    for rule in raw_fertilizer_water:
        dest, source, range_len = rule
        if fertilizer >= source and fertilizer <= source + range_len:
            water = dest - source + fertilizer
            break
    light = water
    for rule in raw_water_light:
        dest, source, range_len = rule
        if water >= source and water <= source + range_len:
            light = dest - source + water
            break
    temperature = light
    for rule in raw_light_temperature:
        dest, source, range_len = rule
        if light >= source and light <= source + range_len:
            temperature = dest - source + light
            break
    humidity = temperature
    for rule in raw_temperature_humidity:
        dest, source, range_len = rule
        if temperature >= source and temperature <= source + range_len:
            humidity = dest - source + temperature
            break
    location = humidity
    for rule in raw_humidity_location:
        dest, source, range_len = rule
        if humidity >= source and humidity <= source + range_len:
            location = dest - source + humidity
            break
    if lowest_location == -1:
        lowest_location = location
    elif location < lowest_location:
        lowest_location = location
print(lowest_location)

# Part 2
total = []
for seed1, seed2 in list(zip(seeds[::2], seeds[1::2])):
    seed_range = [(seed1, seed1 + seed2)]
    for factor in [raw_seed_soil, raw_soil_fertilizer, raw_fertilizer_water, raw_water_light, raw_light_temperature, raw_temperature_humidity, raw_humidity_location]:
        overlaps = []
        for dest, source, range_len in factor:
            source_end = source + range_len
            neighbors = []
            while seed_range:
                start, end = seed_range.pop()
                before = (start, min(end, source))
                overlap = (max(start, source), min(source_end, end))
                after = (max(source_end, start), end)
                if before[1] > before[0]:
                    neighbors.append(before)
                if overlap[1] > overlap[0]:
                    overlaps.append((overlap[0] - source + dest, overlap[1] - source + dest))
                if after[1] > after[0]:
                    neighbors.append(after)
            seed_range = neighbors
        seed_range = overlaps + neighbors
    total.append(min(seed_range)[0])
print(min(total))
