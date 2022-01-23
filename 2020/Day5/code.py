data = []
with open("data.txt") as f:
    data = f.read().split('\n')

new_seat_id = 0
seat_id = []

for line in data:
    start_row = 0
    end_row = 127
    end_row_var = end_row
    start_col = 0
    end_col = 7
    end_col_var = end_col

    for index, letter in enumerate(line):
        if index < 7:
            if letter == "F":
                end_row_var = (((end_row_var + 1) - start_row) / 2 + start_row) - 1
            elif letter == "B":
                start_row = (end_row + 1) / (2 ** (index + 1)) + start_row
        elif index >= 7:
            if letter == "L":
                end_col_var = (((end_col_var + 1) - start_col) / 2 + start_col) - 1
            elif letter == "R":
                start_col = (end_col + 1) / (2 ** (index - 6)) + start_col

    erg = start_row * 8 + start_col  
    seat_id.append(int(erg))  
    if erg > new_seat_id:
        new_seat_id = int(erg)
print(new_seat_id)

seat_id = sorted(seat_id)
place = set(range(seat_id[0], seat_id[-1])) - set(seat_id)
print(place)