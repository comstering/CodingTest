def check(s):
    checkCount = {"[": 0, "{": 0, "(": 0}
    newS = ''
    for i in range(len(s)):
        newS += s[i]
        if s[i] in ['[', '{', '(']:
            checkCount[s[i]] += 1
        else:
            match = '[' if s[i] == ']' else '{' if s[i] == '}' else '('
            if checkCount[match] > 0:
                for j in range(len(newS) - 1, -1, -1):
                    if newS[j] in ['[', '{', '(']:
                        if match != newS[j]:
                            break
                        else:
                            newS = newS[:j] + 'A'
                            checkCount[match] -= 1
                            break
                    else:
                        continue
            else:
                break
    return set(list(newS)) == {'A'}


def solution(s):
    answer = 0
    for i in range(len(s)):
        if check("{0}{1}".format(s[i:], s[:i])):
            answer += 1
    return answer


print(solution("[](){}"))    # 3
print(solution("}]()[{"))    # 2
print(solution("[)(]"))    # 0
print(solution("}}}"))    # 0