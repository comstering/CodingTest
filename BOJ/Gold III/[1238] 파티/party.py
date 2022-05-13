import heapq


# 하나의 노드에서 모든 노드까지의 최단 시간 리스트를 반환하는 함수
def dijkstra(n_count, graph, start):
    # 거리 저장 리스트
    cost_list = [float('inf')] * (n_count + 1)
    # 시작노드의 거리는 0
    cost_list[start] = 0
    # 우선순위 큐
    queue = []
    # 시간, 노드
    heapq.heappush(queue, (0, start))

    # 큐가 빌 때까지 반복
    while queue:
        # 시간, 노드
        current_cost, current_node = heapq.heappop(queue)
        # 시간이 저장된 시간 보다 클경우 더이상 진행 필요 X
        if cost_list[current_node] < current_cost:
            continue

        # 현재 노드에 연결된 노드들의 시간 비교
        for node, cost in graph[current_node]:
            # 현재 노드에서 다음 노드로 걸리는 시간
            new_cost = current_cost + cost
            # 새로 구한 시간이 저장된 시간보다 빠를 경우 갱신
            if new_cost < cost_list[node]:
                cost_list[node] = new_cost
                heapq.heappush(queue, (new_cost, node))

    return cost_list


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 그래프 만들기
for _ in range(m):
    start, end, t = map(int, input().split())
    graph[start].append((end, t))

# x에서 각 노드로 돌아가는데 걸리는 최단 시간 리스트
x_cost_list = dijkstra(n, graph, x)

# 결과 구하기
answer = 0
for idx in range(1, n + 1):
    # 'x까지 가는 시간 + x에서 돌아오는 시간'들 중 최대값을 answer에 최종적으로 저장
    answer = max(answer, x_cost_list[idx] + dijkstra(n, graph, idx)[x])

print(answer)
