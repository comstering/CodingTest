num = int(input())
summary = 0
for i in range(1, 100000000):
    summary += i
    if summary >= num:
        break
print(summary)