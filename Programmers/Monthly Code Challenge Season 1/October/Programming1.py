def solution(n):
    third = 3
    while third <= n:
        third *= 3
    third //= 3
    th = []
    while third > 0:
        sub = n // third
        n -= third * sub
        third //= 3
        th.append(sub)
    answer = 0
    third = 1
    print(th)
    for i in th:
        answer += i * third
        third *= 3
    return answer


print(solution(45))    # 7
print(solution(125))    # 229