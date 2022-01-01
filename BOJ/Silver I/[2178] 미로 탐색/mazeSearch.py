from collections import deque


def solution(graph, n, m, fx, fy):
    # 좌 우 상 하
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((fx, fy))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간 벗어날 경우 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            # 벽인 경우 무시
            if graph[ny][nx] == 0:
                continue

            # 해당 노드가 처음 가는 길이라면 최단 거리로 기록
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, list(input()))))

print(solution(graph, n, m, 0, 0))