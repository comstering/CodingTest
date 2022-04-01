def solution(s):
    answer = ''
    num = 0
    for i in s:
        if i == ' ':
            num = 0
            answer += ' '
        elif num % 2 == 0:
            answer += i.upper()
            num += 1
        else:
            answer += i.lower()
            num += 1
    return answer


print(solution("try hello world"))
print(solution(' I like a problem'))