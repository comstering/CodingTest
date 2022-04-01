def solution(s):
    tuples = s[2:-2].split('},{')
    for i in range(len(tuples)):
        tuples[i] = list(map(int, tuples[i].split(',')))
    tuples.sort(key=len)
    for i in range(len(tuples) - 1, 0, -1):
        for j in tuples[i - 1]:
            tuples[i].remove(j)
    answer = []
    for i in tuples:
        answer.append(i[0])
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))    # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))    # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))    # [111, 20]
print(solution("{{123}}"))    # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))    # [3, 2, 4, 1]