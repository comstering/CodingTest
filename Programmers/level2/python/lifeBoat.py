from collections import deque


def solution(people, limit):
    queue = deque(sorted(people))
    answer = 0
    while queue:
        if len(queue) == 1:
            queue.pop()
        elif queue[0] + queue[-1] <= limit:
            queue.popleft()
            queue.pop()
        else:
            queue.pop()
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3
