def solution(citations):
    answer = 0
    for i in range(len(citations)):
        count = list(map(lambda x: x >= i + 1, citations)).count(True)
        if i + 1 > answer and count >= i + 1:
            answer = i + 1
    return answer


print(solution([3, 0, 6, 1, 5]))    # 3