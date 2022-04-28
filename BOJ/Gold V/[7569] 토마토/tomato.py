from collections import deque
import sys


def getDay(graph):
    # 이동하는 방향
    # 같은 층 상하좌우, 위층 아래층
    dx = [0, 0, 1, -1, 0, 0]  # udrlfb
    dy = [-1, 1, 0, 0, 0, 0]  # udrlfb
    dz = [0, 0, 0, 0, -1, 1]  # udrlfb

    queue = deque()
    # 현재 익은 상태의 토마토가 있는 위치 큐에 저장
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i][j])):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        # 현재 위치
        z, y, x = queue.popleft()
        # 토마토 탐색
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 범위 밖이라면 패스
            if nx < 0 or nx >= len(graph[0][0]):
                continue
            if ny < 0 or ny >= len(graph[0]):
                continue
            if nz < 0 or nz >= len(graph):
                continue
            # 이미 익었거나 들어있지 않은 칸이라면 패스
            if graph[nz][ny][nx] != 0:
                continue
            # 다음 토마토가 익은 시간: 현재 토마토가 익은 시간 +1
            graph[nz][ny][nx] = graph[z][y][x] + 1
            # 다음 토마토 위치 큐에 append
            queue.append((nz, ny, nx))

    answer = 0
    for i in graph:
        for j in i:
            if 0 in j:
                answer = -1
                break
            # 시작을 1로 시작했으므로 결과는 -1을 해주어야함
            m = max(j) - 1
            answer = max(answer, m)
        if answer == -1:
            break
    return answer


m, n, h = map(int, sys.stdin.readline().split())

boxes = []
for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, sys.stdin.readline().split())))
    boxes.append(box)

print(getDay(boxes))
