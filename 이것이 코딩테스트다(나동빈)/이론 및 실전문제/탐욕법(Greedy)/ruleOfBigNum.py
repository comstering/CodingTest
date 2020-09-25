def solution1(n, m, k, numList):
    numList.sort()
    count = 0
    answer = 0
    for i in range(m):
        if count >= k:
            answer += numList[n - 2]
            count = 0
        else:
            answer += numList[n - 1]
            count += 1
    return answer


def solution2(n, m, k, numList):
    numList.sort()
    first = numList[n - 1]
    second = numList[n - 2]
    # 가장 큰 수가 더해지는 횟수 계산
    count = (m // (k + 1)) * k
    count += m % (k + 1)

    answer = 0
    answer += count * first    # 가장 큰 수 더하기
    answer += (m - count) * second    # 두 번째로 큰 수 더하기

    return answer


print(solution1(5, 8, 3, [2, 4, 5, 4, 6]))
print(solution2(5, 8, 3, [2, 4, 5, 4, 6]))