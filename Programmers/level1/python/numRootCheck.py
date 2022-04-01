def solution(n):
    num = pow(n, 0.5)
    answer = int(pow(num + 1, 2)) if num % 1 == 0 else -1
    return answer


print(solution(121))