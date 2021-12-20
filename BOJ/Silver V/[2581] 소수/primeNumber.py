n = 10000
numList = [True] * n
numList[0] = False
for i in range(2, n):
    if numList[i - 1]:
        for j in range(2 * i, n + 1, i):
            numList[j - 1] = False
num1 = int(input())
num2 = int(input())
summary = 0
for i in range(num1, num2 + 1):
    if numList[i - 1]:
        summary += i
if summary == 0:
    print(-1)
else:
    print(summary)
    print(num1 + numList[num1 - 1: num2 + 1].index(True))