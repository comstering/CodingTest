n = 10000
numList = [True] * n
numList[0] = False
for i in range(2, n):
    if numList[i - 1]:
        for j in range(2 * i, n + 1, i):
            numList[j - 1] = False
test = int(input())
for i in range(test):
    num = int(input())
    if numList[num // 2 - 1]:
        print(num // 2, num // 2)
    else:
        for j in range(num // 2, 0, -1):
            if numList[j - 1] and numList[num - j - 1]:
                print(j, num - j)
                break