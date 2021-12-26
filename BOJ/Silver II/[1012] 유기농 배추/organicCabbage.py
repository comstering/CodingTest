import sys

sys.setrecursionlimit(1000000)

def bug(x, y, n, m, c_map):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if c_map[x][y] == 1:
        c_map[x][y] = 0
        # 인접한 곳 전부 체크
        bug(x + 1, y, n, m, c_map)
        bug(x, y + 1, n, m, c_map)
        bug(x - 1, y, n, m, c_map)
        bug(x, y - 1, n, m, c_map)
        return True
    return False


case = int(input())

for _ in range(case):
    m, n, k = map(int, input().split())
    cabbage_map = [[0] * n for _ in range(m)]
    for _ in range(k):
        i, j = map(int, input().split())
        cabbage_map[i][j] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if bug(j, i, n, m, cabbage_map):
                answer += 1
    print(answer)