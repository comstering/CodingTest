from collections import deque


def getDay(graph):
    # 이동하는 방향
    dx = [0, 0, 1, -1]  # udrl
    dy = [-1, 1, 0, 0]  # udrl
    queue = deque()
    # 현재 익은 상태의 토마토가 있는 위치 큐에 저장
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        # 현재 위치
        y, x = queue.popleft()
        # 상하좌우 토마토 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖이라면 패스
            if nx < 0 or nx >= len(graph[0]):
                continue
            if ny < 0 or ny >= len(graph):
                continue
            # 이미 익었거나 들어있지 않은 칸이라면 패스
            if graph[ny][nx] != 0:
                continue
            # 다음 토마토가 익은 시간: 현재 토마토가 익은 시간 +1
            graph[ny][nx] = graph[y][x] + 1
            # 다음 토마토 위치 큐에 append
            queue.append((ny, nx))

    answer = 0
    for i in graph:
        if 0 in i:
            answer = -1
            break
        # 시작을 1로 시작했으므로 결과는 -1을 해주어야함
        m = max(i) - 1
        answer = max(answer, m)
    return answer


m, n = map(int, input().split())

box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
print(getDay(box))
