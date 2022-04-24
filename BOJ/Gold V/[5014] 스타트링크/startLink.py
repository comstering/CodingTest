from collections import deque


f, s, g, u, d = map(int, input().split())

# 방문 확인
visited = [False] * (f + 1)

def solution(s):
    queue = deque()
    # 현재 층 queue에 넣기
    queue.append((s, 0))
    visited[s] = True

    while queue:
        # queue popleft
        now, result = queue.popleft()
        # 목적지 층인지 확인
        if now == g:
            return result
        # 상승 / 하락 전부 탐색
        for i in range(2):
            nx = now
            # 상승일 때
            if i == 0:
                nx += u
            # 하락일 때
            elif i == 1:
                nx -= d

            # 움직일 위치가 건물 층 범위 밖일 경우
            if nx not in range(1, f + 1):
                continue
            # 움직일 위치가 이미 방문했던 곳일 경우
            if visited[nx]:
                continue
            # 움직일 위치 방문 처리
            visited[nx] = True

            # 다음 위치 queue에 넣기
            queue.append((nx, result + 1))

    # 가능한 모든 층을 들어갔지만 결과가 도출되지 않았을 경우
    return 'use the stairs'


print(solution(s))
