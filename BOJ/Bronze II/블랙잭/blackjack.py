n, m = map(int, input().split())
numList = list(map(int, input().split()))
resultList = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            result = numList[i] + numList[j] + numList[k]
            if result <= m:
                resultList.append(result)
resultList.sort()
print(resultList[-1])