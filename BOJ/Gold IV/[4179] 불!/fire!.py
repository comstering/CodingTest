from collections import deque
import sys

def findOut(graph):
    # 이동방향
    dx = [0, 0, -1, 1]  # udlr
    dy = [-1, 1, 0, 0]  # udlr

    # 지훈이 큐, 불 큐
    jQueue, fQueue = deque(), deque()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            # 지훈이 위치 기록
            if graph[i][j] == 'J':
                jQueue.append((j, i))
                graph[i][j] = 1
            # 불의 위치 기록
            if graph[i][j] == 'F':
                # 불의 시작이 여러개일 수 있으므로 큐에 저장
                fQueue.append((j, i))
                graph[i][j] = -1

    while jQueue:
        jx, jy = jQueue.popleft()

        # 지훈이 4방향 모두 탐색
        for i in range(4):
            jnx = jx + dx[i]
            jny = jy + dy[i]

            if jnx < 0 or jnx >= len(graph[0]):
                continue
            if jny < 0 or jny >= len(graph):
                continue
            # 지훈이가 이동 가능할 때만 이동
            if graph[jny][jnx] == '.':
                # 이동 가능할 경우 경과시간 표시
                graph[jny][jnx] = graph[jy][jx] + 1
                jQueue.append((jnx, jny))

    answer = float('inf')

    while fQueue:
        fx, fy = fQueue.popleft()
        # 불 4방향 탐색
        for i in range(4):
            fnx = fx + dx[i]
            fny = fy + dy[i]

            if fnx < 0 or fnx >= len(graph[0]):
                continue
            if fny < 0 or fny >= len(graph):
                continue

            # 벽이 아닐 경우만
            if graph[fny][fnx] != '#':
                # 빈칸일 경우 그냥 검증
                if graph[fny][fnx] == '.':
                    pass
                # 이미 탐색한 곳이라면 넘어감
                elif graph[fny][fnx] < 0:
                    continue
                # 지훈이가 갈 수 있었던 곳이라면 확인
                elif graph[fny][fnx] > 0:
                    # 지훈이가 탈출할 수 있는 가장자리일 때
                    if fnx == 0 or (fnx == len(graph[0]) - 1) or fny == 0 or (fny == len(graph) - 1):
                        # 불이 도착한 시간보다 지훈이가 도착한 시간이 빠르다면 answer과 비교
                        if -graph[fny][fnx] > graph[fy][fx] - 1:
                            # 더 빠른 answer을 저장
                            answer = min(answer, graph[fny][fnx])
                # 다음 탐색 위치에 불의 경과시간 기록
                graph[fny][fnx] = graph[fy][fx] - 1
                # 큐에 다음 탐색위치 넣기
                fQueue.append((fnx, fny))

    # 불이 도착하지 못하는 곳에서의 위치 확인
    for i in graph:
        answer = min(answer,
                     float('inf') if type(i[0]) is not int else float('inf') if i[0] < 0 else i[0],
                     float('inf') if type(i[-1]) is not int else float('inf') if i[-1] < 0 else i[-1])
    for i in range(len(graph[0])):
        answer = min(answer,
                     float('inf') if type(graph[0][i]) is not int else float('inf') if graph[0][i] < 0 else graph[0][i],
                     float('inf') if type(graph[-1][i]) is not int else float('inf') if graph[-1][i] < 0 else graph[-1][i])

    # 만약 지훈이가 탈출할 수 없어서 answer이 inf라면 'IMPOSSIBLE' 반환
    return answer if answer != float('inf') else 'IMPOSSIBLE'


r, c = map(int, sys.stdin.readline().split())

maze = []
for _ in range(r):
    maze.append(list(sys.stdin.readline()[:-1]))

print(findOut(maze))
