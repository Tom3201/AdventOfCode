with open("data.txt") as f:
    data = f.read().splitlines()

numbers = 0
part1 = True
tickets = []
line_numbers = []
checked_tickets = []
for index, line in enumerate(data):
    if index == 0:
        numbers = line.split(",")
    elif index > 1:
        if line:
            line_numbers.append(line.split())
        else:
            tickets.append(line_numbers)
            line_numbers = []
        if index == len(data) - 1:
            tickets.append(line_numbers)

for ticket in tickets:
    checked_tickets.append([[False for _ in range(5)] for _ in range(5)])

all_wins = [False for _ in range(len(checked_tickets))]
for number in numbers:
    for i, ticket in enumerate(tickets):
        for j, line in enumerate(ticket):
            for k, num in enumerate(line):
                if int(number) == int(num):
                    checked_tickets[i][j][k] = True

        win = False
        for j, line in enumerate(ticket):
            ok = True
            for k, num in enumerate(line):
                if not checked_tickets[i][j][k]:
                    ok = False
            if ok:
                win = True
        for k in range(5):
            ok = True
            for j in range(5):
                if not checked_tickets[i][j][k]:
                    ok = False
            if ok:
                win = True
        
        if win:
            all_wins[i] = True
            if part1:
                not_marked = 0
                for j in range(5):
                    for k in range(5):
                        if not checked_tickets[i][j][k]:
                            not_marked += int(ticket[j][k])
                part1 = False
                print(not_marked * int(number))
            if all([all_wins[j] for j in range(len(checked_tickets))]):
                not_marked = 0
                for j in range(5):
                    for k in range(5):
                        if not checked_tickets[i][j][k]:
                            not_marked += int(ticket[j][k])
                print(not_marked * int(number))
                exit()