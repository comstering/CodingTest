def solution(record):
    answer = []
    user = dict()
    for i in record:
        log = i.split()
        if log[0] == 'Enter':
            user[log[1]] = log[2]
            answer.append([log[1], '님이 들어왔습니다.'])
        elif log[0] == 'Leave':
            answer.append([log[1], '님이 나갔습니다.'])
        elif log[0] == 'Change':
            user[log[1]] = log[2]
    answer = [''.join([user[i[0]], i[1]]) for i in answer]
    return answer


print(solution(['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan']))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]