def solution(strings, n):
    answer = []
    for i in range(0, len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for i in strings:
        answer.append(i[1:])
    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))