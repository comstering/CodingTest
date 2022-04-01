def solution(x):
    summary = sum(list(map(int, str(x))))
    answer = True if x % summary == 0 else False
    return answer


print(solution(10))    # True
print(solution(11))    # False