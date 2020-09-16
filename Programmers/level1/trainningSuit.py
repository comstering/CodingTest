def solution(n, lost, reserve):
    std = [1] * n
    for i in lost:
        std[i - 1] -= 1
    for i in reserve:
        std[i - 1] += 1
    for i in range(0, n):
        if std[i] == 2:
            if i > 0 and std[i - 1] == 0:
                std[i - 1] += 1
                std[i] -= 1
            elif i < n - 1 and std[i + 1] == 0:
                std[i + 1] += 1
                std[i] -= 1
    return len(list(filter(lambda x: x >= 1, std)))


print(solution(5, [2, 4], [1, 3, 5]))    # 5
print(solution(5, [2, 4], [3]))    # 4
print(solution(3, [3], [1]))   # 2