num = int(input())
count = num

while count > 0:
    print(" " * (num - count) + "*" * (count * 2 - 1))
    count -= 1

count += 1

while count < num:
    count += 1
    print(" " * (num - count) + "*" * (count * 2 - 1))