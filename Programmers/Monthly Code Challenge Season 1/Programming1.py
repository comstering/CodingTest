def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer


print(solution([5, 0, 2, 7]))