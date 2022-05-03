import sys
import heapq

# 입력
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

# 각 노드에 연결된 노드와 가중치 저장 그래프
graph = [[] for _ in range(v + 1)]

# 입력
for _ in range(e):
    n1, n2, length = map(int, sys.stdin.readline().split())
    graph[n1].append((length, n2))

# 각 노드별 비용 리스트
cost_list = [float('inf')] * (v + 1)
# 시작노드의 비용은 0
cost_list[k] = 0

# 다익스트라 알고리즘 큐
queue = []

# 우선순위를 비용으로 두기 위해 (비용, 노드)
heapq.heappush(queue, (0, k))

# 큐가 빌 때까지 반복
while queue:
    # 비용, 노드
    current_cost, current_node = heapq.heappop(queue)
    # 비용이 현재 기록된 비용보다 크다면 더이상 진행할 필요 없음
    if cost_list[current_node] < current_cost:
        continue

    # 현재 노드에서 인접한 노드까지의 비용
    for node in graph[current_node]:
        # 다음 인접노드와 인접노드로 가는 비용
        new_cost, new_node = node
        cost = current_cost + new_cost
        # 구한 비용이 기존의 비용보다 작으면 최저비용으로 등록
        if cost < cost_list[new_node]:
            cost_list[new_node] = cost
            heapq.heappush(queue, (cost, new_node))

for i in cost_list[1:]:
    print(str(i).upper())
