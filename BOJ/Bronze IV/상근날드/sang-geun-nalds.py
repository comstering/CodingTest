count = 0

bugger = []
drink = []

while count < 3:
    count += 1
    bugger.append(int(input()))

while count < 5:
    count += 1
    drink.append(int(input()))

print(min(bugger) + min(drink) - 50)