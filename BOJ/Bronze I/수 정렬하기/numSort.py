n = int(input())
numList = []
for i in range(n):
    numList.append(int(input()))
numList.sort()
for i in numList:
    print(i)