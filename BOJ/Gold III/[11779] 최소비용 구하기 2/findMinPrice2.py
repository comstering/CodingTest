import sys
import heapq  # 우선 순위 큐 사용

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# float('inf') 경로 최대값 설정
bus_graph = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    # 시작, 끝, 비용
    s, e, c = map(int, sys.stdin.readline().split())
    # 시작지점에서 도착지점까지의 비용이 기존의 비용보다 작을 경우 입력
    if bus_graph[s - 1][e - 1] > c:
        bus_graph[s - 1][e - 1] = c

# 구해야할 시작지점, 도착지점
start, end = map(lambda x: x - 1, map(int, sys.stdin.readline().split()))

# 각 노드별 비용 리스트
cost_list = [float('inf')] * n
# 각 노드에 도착할 때 필요한 경로의 노드
path_node = [[] for _ in range(n)]

# 시작 노드의 비용은 0
cost_list[start] = 0
# 시작 노드의 경로 노드에 자기 자신 추가
path_node[start].append(start)

# 다익스트라 알고리즘 큐
queue = []
# 우선순위를 비용으로 두기 위해 (비용, 노드)
heapq.heappush(queue, (0, start))

# 큐가 빌 때까지 반복
while queue:
    # 비용, 노드
    current_cost, current_node = heapq.heappop(queue)
    # 비용이 현재 기록된 비용보다 크다면 더이상 진행할 필요 없음
    if cost_list[current_node] < current_cost:
        continue

    # 현재의 노드에서 인접한 노드까지의 비용
    for idx in range(n):
        # 자기 자신이면 넘어가기
        if idx == current_node:
            continue
        # 다음 인접 노드까지 가는 비용
        new_cost = bus_graph[current_node][idx]
        cost = current_cost + new_cost
        # 구한 비용이 기존의 비용보다 작으면 최저 비용으로 등록
        if cost < cost_list[idx]:
            cost_list[idx] = cost
            # 현재 위치까지의 경로 가져오기
            path = path_node[current_node][:]
            # 다음 노드 추가
            path.append(idx)
            # 다음 노드까지의 경로 저장
            path_node[idx] = path
            # 다음 인접 노드의 비용을 구하기 위해 큐에 삽입
            heapq.heappush(queue, (cost, idx))

print(cost_list[end])
print(len(path_node[end]))
print(' '.join(map(lambda x: str(x + 1), path_node[end])))
