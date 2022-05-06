import heapq


n = int(input())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

queue = []
# 시작 좌표 방문처리
maze[0][0] = -1
# 우선순위 큐에 시작좌표 넣기
# 흰방이 먼저 계산되어야하므로 (-좌표값, 좌표)
heapq.heappush(queue, (-maze[0][0], (0, 0)))

# 이동방향
dx = [0, 0, -1, 1]  # udlr
dy = [-1, 1, 0, 0]  # udlr

while queue:
    # 우선순위, 좌표
    v, (x, y) = heapq.heappop(queue)

    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 밖일 경우 패스
        if nx < 0 or nx >= n:
            continue
        if ny < 0 or ny >= n:
            continue

        # 검은 방일 경우
        if maze[ny][nx] == 0:
            # 현재 위치의 우선순위값 +1
            # 흰 방보다 늦은 탐색을 위해서
            maze[ny][nx] = -(v + 1)
            # 새로운 우선순위로 큐에 넣기
            heapq.heappush(queue, (-maze[ny][nx], (nx, ny)))
        # 흰 방일 경우
        elif maze[ny][nx] == 1:
            # 현재 위치의 우선순위 그대로 넣기
            # 흰 방일 경우에는 검은 방보다 빠른 탐새을 위해 그대로 넣기
            maze[ny][nx] = maze[y][x]
            # 큐에 넣기
            heapq.heappush(queue, (-maze[ny][nx], (nx, ny)))

# 최종 끝방의 위치값을 양수로 전환 후 -1 하기
print(-maze[-1][-1] - 1)
for i in maze:
    print(i)
