num = int(input())
if num < 100:
    print(num)
else:
    count = 99
    for i in range(100, num + 1):
        if ((i // 100) - ((i % 100) // 10)) == (((i % 100) // 10) - (i % 10)):
            count += 1
    print(count)