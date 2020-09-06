def solution(s):
    slen = len(s)
    answer = s[(slen - 1) // 2:slen // 2 + 1]
    return answer


print(solution("abcde"))