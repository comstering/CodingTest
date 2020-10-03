n = 1000
numList = [True] * n
numList[0] = False
for i in range(2, n):
    if numList[i - 1]:
        for j in range(2 * i, n + 1, i):
            numList[j - 1] = False
num = int(input())
numSet = map(int, input().split())
count = 0
for i in numSet:
    if numList[i - 1]:
        count += 1
print(count)