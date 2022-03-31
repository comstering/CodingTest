import sys
sys.setrecursionlimit(10 ** 6)


def getProg(prog_map, x, y, n, m):
    # 지도 밖이면 0 반환
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    else:
        result = 0
        if prog_map[y][x]:
            # 현재 위치 도착 처리
            prog_map[y][x] = False
            # 개수 + 1
            result += 1
            # 상하좌우 인접한 쓰레기 개수 더하기
            result += getProg(prog_map, x + 1, y, n, m)
            result += getProg(prog_map, x - 1, y, n, m)
            result += getProg(prog_map, x, y + 1, n, m)
            result += getProg(prog_map, x, y - 1, n, m)
        # 결과 반환
        return result


n, m, k = map(int, input().split())
# 음식물 지도 만들기
prog_map = [[False] * m for _ in range(n)]
# 입력받은 위치에 음식물 존재하는 것으로 체크
for _ in range(k):
    r, c = map(int, input().split())
    prog_map[r - 1][c - 1] = True

answer = 0
# 지도의 모든 위치를 돌면서 가장 많은 음식물 개수 구하기
for i in range(n):
    for j in range(m):
        # j, i 위치에서 인접한 음식물 쓰레기 개수 구하기
        prog = getProg(prog_map, j, i, n, m)
        # 기존의 쓰레기 개수보다 많다면 결과 변경
        answer = answer if answer > prog else prog

print(answer)
