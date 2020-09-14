def solution(n):
    n = sorted(str(n), reverse=True)
    answer = int("".join(n))
    return answer


print(solution(118372))