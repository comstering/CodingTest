def dfs(idx, numbers):
    if idx == len(numbers) - 1:
        return numbers[-1], -numbers[-1]

    result = []
    for i in dfs(idx + 1, numbers):
        result.append(numbers[idx] + i)
        result.append(-numbers[idx] + i)
    return result


def solution(numbers, target):
    return dfs(0, numbers).count(target)


print(solution([1, 1, 1, 1, 1], 3))    # 5
print(solution([4, 1, 2, 1], 4))    # 2
