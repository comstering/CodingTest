def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first = first * (len(answers) // len(first) + 1)
    second = second * (len(answers) // len(second) + 1)
    third = third * (len(answers) // len(third) + 1)
    score = [0] * 3
    for i, f, s, t in zip(answers, first, second, third):
        if i == f:
            score[0] += 1
        if i == s:
            score[1] += 1
        if i == t:
            score[2] += 1
    answer = []
    mscore = max(score)
    for i in range(score.count(mscore)):
        answer.append(score.index(mscore) + 1)
        score[score.index(mscore)] = -1
    return answer


ans = [1, 2, 3, 4, 5]
print(solution(ans))