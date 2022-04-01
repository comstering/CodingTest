def solution(s):
    al = list(s)
    al.sort()
    al.reverse()
    answer = ''.join(al)
    return answer


print(solution("Zbcdefg"))