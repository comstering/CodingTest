from collections import deque


def stone(a, b, c):
    # 전체 합 구하기
    total = a + b + c
    # 전체 합이 3으로 나누어떨어지지 않으면 0반환
    if total % 3 != 0:
        return 0

    # 돌의 순서쌍 체크리스트
    visited = [[False] * total for _ in range(total)]
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        # 현재 3 돌의 상태 확인
        z = total - x - y
        # 3 돌의 상태가 모두 동일하면 1반환
        if x == y == z:
            return 1

        # 나올 수 있는 경우의 돌 반복
        for i, j in (x, y), (x, z), (y, z):
            # 문제 요구사항
            # 작은돌 X, 큰 돌 Y
            # X = X + X, Y = Y - X
            if i < j:
                j -= i
                i += i
            elif i > j:
                i -= j
                j += j
            # 같을 경우 패스
            else:
                continue

            # 새로운 3 돌 구하기
            k = total - i - j
            # 3 돌 중 가장 큰 돌과 가장 작은 돌 구하기
            X = min(i, j, k)
            Y = max(i, j, k)
            # 해당 돌 쌍이 기존에 체크했던 돌 쌍이 아니면 queue에 append
            if not visited[X][Y]:
                queue.append((X, Y))
                # 돌 쌍 체크 처리
                visited[X][Y] = True
    # 모든 탐색이 끝났음에도 완성이 되지 않았다면 0반환
    return 0


a, b, c = map(int, input().split())
print(stone(a, b, c))
