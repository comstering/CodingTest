from collections import deque
import sys


def solution(graph, n, m):
    graph[0][0] = -1
    # 이동 방향
    dx = [0, 0, -1, 1]  # udlr
    dy = [-1, 1, 0, 0]  # udlr

    queue = deque()
    queue.append((0, 0))

    # 처음 탐색에서 인접한 벽만 담는 큐
    wall_queue = deque()

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이면 패스
            if nx < 0 or nx >= m:
                continue
            if ny < 0 or ny >= n:
                continue

            # 다음 위치가 벽이 아닐 경우 이동
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] - 1
                queue.append((nx, ny))
            # 다음 위치가 벽일 경우 wall_queue에 저장
            elif graph[ny][nx] == 1:
                graph[ny][nx] = -(graph[y][x] - 1)
                wall_queue.append((nx, ny))

    # 인접한 벽을 통해서 갈 수 있는 빠른 길 탐색
    # 즉, 벽 한개만을 부순 경우만 확인
    while wall_queue:
        x, y = wall_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이면 패스
            if nx < 0 or nx >= m:
                continue
            if ny < 0 or ny >= n:
                continue

            # 현재 위치가 인접한 벽일 경우에는 양수로 저장했으므로 음수로 변환
            now = graph[y][x] if graph[y][x] < 0 else -graph[y][x]

            # 지나가지 않은 곳이라면 현재까지의 거리 +1
            if graph[ny][nx] == 0:
                graph[ny][nx] = now - 1
                wall_queue.append((nx, ny))
            # 지나갔던 길이지만 벽을 부순 후의 경로가 더 빠를 경우 새로운 거리 등록
            elif graph[ny][nx] < 0:
                if now - 1 > graph[ny][nx]:
                    graph[ny][nx] = now - 1
                    wall_queue.append((nx, ny))

    answer = graph[n - 1][m - 1]
    return -answer if answer < 0 else -1


n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline()[:-1])))

print(solution(graph, n, m))
