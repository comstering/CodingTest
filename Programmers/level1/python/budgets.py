def solution(d, budget):
    answer = 0
    de = sorted(d)
    for i in de:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer


print(solution([1, 3, 2, 5, 4], 9))    # 3
print(solution([2, 2, 3, 3], 10))    # 4