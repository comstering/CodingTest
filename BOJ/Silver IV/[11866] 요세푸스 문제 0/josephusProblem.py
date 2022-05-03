from collections import deque

n, k = map(int, input().split())

num_list = [i + 1 for i in range(n)]

queue = deque(num_list)

result_list = []

count = 1
while queue:
    if count % k == 0:
        result_list.append(queue.popleft())
    else:
        queue.append(queue.popleft())
    count += 1

print(f'<{", ".join(map(str, result_list))}>')
