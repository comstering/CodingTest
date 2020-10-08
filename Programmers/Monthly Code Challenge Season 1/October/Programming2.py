def solution(arr):
    answer = [0, 0]
    s = []
    for i in arr:
        s += i
    if len(set(s)) == 1:
        answer[s[0]] = 1
        return answer
    sub = [[], [], [], []]
    for i in range(len(arr) // 2):
        sub[0] += [arr[i][:len(arr) // 2]]
        sub[1] += [arr[i][len(arr) // 2:]]
    for i in range(len(arr) // 2, len(arr)):
        sub[2] += [arr[i][:len(arr) // 2]]
        sub[3] += [arr[i][len(arr) // 2:]]
    for i in sub:
        an = solution(i)
        answer[0] += an[0]
        answer[1] += an[1]
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))    # [4, 9]
print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))    # [10, 15]