def solution(s, n):
    answer = ''
    for i in s:
        ch = ord(i)
        if not(ord('a') <= ch <= ord('z') or ord('A') <= ch <= ord('Z')):
            answer += i
            continue
        newch = ch + n
        if ord('a') <= ch <= ord('z') and not(ord('a') <= newch <= ord('z')):
            newch -= 26
        elif ord('A') <= ch <= ord('Z') and not(ord('A') <= newch <= ord('Z')):
            newch -= 26
        ch = chr(newch)
        answer += ch
    return answer

print(solution("h   Z", 25))