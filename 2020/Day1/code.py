data = []
with open("data.txt") as f:
    data = f.readlines()
    for number1 in data:
        for number2 in data:
            for number3 in data:
                sum = int(number1) + int(number2) + int(number3)
                if sum == 2020:
                    print(int(number1) * int(number2) * int(number3))
                    exit()