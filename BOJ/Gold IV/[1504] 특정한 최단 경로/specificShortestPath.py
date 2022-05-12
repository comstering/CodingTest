import sys, heapq


n, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

# 그래프 만들기
for _ in range(e):
    n1, n2, v = map(int, sys.stdin.readline().split())
    graph[n1].append((n2, v))
    graph[n2].append((n1, v))

v1, v2 = map(int, sys.stdin.readline().split())

# v1에 대한 cost 리스트
v1_cost_list = [float('inf')] * (n + 1)
v1_cost_list[v1] = 0

# 우선순위 큐
queue = []
heapq.heappush(queue, (0, v1))

# v1에서의 각 노드별 최단 경로 구하기
while queue:
    # 비용, 노드
    current_cost, current_node = heapq.heappop(queue)
    # cost가 현재 기록된 cost보다 클 경우 더이상 진행 불필요
    if v1_cost_list[current_node] < current_cost:
        continue

    # 노드에 연결된 노드들과의 cost 비교
    for node, cost in graph[current_node]:
        new_cost = current_cost + cost
        # 기록된 cost보다 작을 경우 cost 값 갱신하고 우선순위 큐에 추가
        if new_cost < v1_cost_list[node]:
            v1_cost_list[node] = new_cost
            heapq.heappush(queue, (new_cost, node))

# v2에 대한 cost 리스트
v2_cost_list = [float('inf')] * (n + 1)
v2_cost_list[v2] = 0

# 우선순위 큐
heapq.heappush(queue, (0, v2))

# v2에서의 각 노드별 최단 경로 구하기
while queue:
    # 비용, 노드
    current_cost, current_node = heapq.heappop(queue)
    # cost가 현재 기록된 cost보다 클 경우 더이상 진행 불필요
    if v2_cost_list[current_node] < current_cost:
        continue

    # 노드에 연결된 노드들과의 cost 비교
    for node, cost in graph[current_node]:
        new_cost = current_cost + cost
        # 기록된 cost보다 작을 경우 cost 값 갱신하고 우선순위 큐에 추가
        if new_cost < v2_cost_list[node]:
            v2_cost_list[node] = new_cost
            heapq.heappush(queue, (new_cost, node))

# 결과
answer = float('inf')

# 1 -> v1 -> v2 -> n의 경로
answer = min(answer, v1_cost_list[1] + v1_cost_list[v2] + v2_cost_list[n])

# 1 -> v2 -> v1 -> n의 경로
answer = min(answer, v2_cost_list[1] + v2_cost_list[v1] + v1_cost_list[n])

print(answer if answer != float('inf') else -1)
