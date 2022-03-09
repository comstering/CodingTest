from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    while queue:
        if queue[0] == max(queue):
            queue.popleft()
            answer += 1
            if location == 0:
                break
        else:
            queue.append(queue.popleft())

        location -= 1
        if location < 0:
            location = len(queue) - 1
    return answer


print(solution([2, 1, 3, 2], 2))    # 1
print(solution([1, 1, 9, 1, 1, 1], 0))    # 5