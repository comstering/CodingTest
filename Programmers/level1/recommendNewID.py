import re

def solution(new_id):
    # level1
    answer = new_id.lower()
    # level2
    answer = re.sub('[^a-z0-9\-\._]', '', answer)
    #level3
    answer = re.sub('\.+', '.', answer)
    # level4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # level5
    if len(answer) == 0:
        answer += 'a'
    # level6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # level7
    while(len(answer) <= 2):
        answer += answer[-1]
    return answer


print(solution("..!@BaT#*..y.abcdefghijklm"))    # bat.y.abcdefghi
print(solution("z-+.^."))    # z--
print(solution("=.="))    # aaa
print(solution("123_.def"))    # 123_.def
print(solution("abcdefghijklmn.p"))    #  abcdefghijklmn