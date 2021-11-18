def solution(n, line):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    mv_types = ['U', 'D', 'L', 'R']
    for i in line:
        idx = mv_types.index(i)
        x += dx[idx]
        y += dy[idx]
        x = x if x > 0 else 1
        y = y if y > 0 else 1

    return x, y


n = int(input())
line = list(input().split())
print(solution(n, line))