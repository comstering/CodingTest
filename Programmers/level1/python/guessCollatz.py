def solution(num):
    answer = 0
    while num != 1:
        if answer >= 500:
            answer = -1
            break
        answer += 1
        num = num // 2 if num % 2 == 0 else num * 3 + 1
    return answer


print(solution(6))    # 8
print(solution(16))    # 4
print(solution(626331))    # -1