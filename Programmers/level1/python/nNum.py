def solution(x, n):
    return list(range(x, x * (n + 1), x)) if x != 0 else list([0] * n)


print(solution(2, 5))    # [2, 4, 6, 8, 10]
print(solution(-4, 2))    # [-4, -8]