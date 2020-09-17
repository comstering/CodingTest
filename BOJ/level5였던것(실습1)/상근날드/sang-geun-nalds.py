count = 0

bugger = []
drink = []

while count < 3:
    count += 1
    bugger.append(int(input()))

while count < 5:
    count += 1
    drink.append(int(input()))

minbugger = 5000
mindrink = 5000

for i in bugger:
    if minbugger > i:
        minbugger = i

for i in drink:
    if mindrink > i:
        mindrink = i

print(minbugger + mindrink - 50)