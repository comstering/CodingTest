num = int(input())

count = 0
number = 0
while True:
    number += 1
    if str(number).count('666'):
        count += 1
    if count == num:
        break

print(number)