import sys
sys.setrecursionlimit(10 ** 6)


def getProg(prog_map, x, y, n, m):
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    else:
        result = 0
        if prog_map[y][x]:
            prog_map[y][x] = False
            result += 1
            result += getProg(prog_map, x + 1, y, n, m)
            result += getProg(prog_map, x - 1, y, n, m)
            result += getProg(prog_map, x, y + 1, n, m)
            result += getProg(prog_map, x, y - 1, n, m)
        return result


n, m, k = map(int, input().split())
prog_map = [[False] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    prog_map[r - 1][c - 1] = True

answer = 0
for i in range(n):
    for j in range(m):
        prog = getProg(prog_map, j, i, n, m)
        answer = answer if answer > prog else prog

print(answer)
