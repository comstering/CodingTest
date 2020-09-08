def solution(s):
    answer = s.isdecimal() and (len(s) == 4 or len(s) == 6)
    return answer


print(solution("6177234"))