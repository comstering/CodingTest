num = int(input())
summary = 0
for i in range(1, 1000):
    sum += i
    if summary >= num:
        print(i)
        break