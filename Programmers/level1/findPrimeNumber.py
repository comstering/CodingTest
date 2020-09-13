def solution(n):
    numList = [True] * n
    numList[0] = False
    for i in range(2, n):
        if numList[i - 1]:
            for j in range(2 * i, n + 1, i):
                numList[j - 1] = False
    return numList.count(True)


print(solution(10))