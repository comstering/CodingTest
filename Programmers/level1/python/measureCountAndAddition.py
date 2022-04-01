def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        data = i
        num = 2
        primeList = []
        while num <= data:
            if data % num == 0:
                primeList.append(num)
                data //= num
            else:
                num += 1
        count = 1
        primeSet = set(primeList)
        for j in primeSet:
            count *= (primeList.count(j) + 1)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


print(solution(13, 17))    # 43
print(solution(24, 27))    # 52