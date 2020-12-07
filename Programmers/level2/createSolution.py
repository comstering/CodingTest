from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    for p, s in zip(progresses, speeds):
        day = (100 - p) // s
        if (100 - p) % s != 0:
            day += 1
        queue.append(day)
    count = 0
    be = queue.popleft()
    print(queue)
    while queue:
        count += 1
        v = queue.popleft()
        print(v)
        if be >= v:
            continue
        else:
            be = v
            answer.append(count)
            count = 0
    count += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))    # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))    # [1, 3, 2]