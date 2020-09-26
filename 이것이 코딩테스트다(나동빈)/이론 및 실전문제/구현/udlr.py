def solution(n, line):
    x, y = 1, 1
    for i in line:
        if i == 'R':
            x += 1
        elif i == 'L':
            x -= 1
        elif i == 'U':
            y -= 1
        elif i == 'D':
            y += 1
        if x < 1:
            x = 1
        if y < 1:
            y = 1
        if x > n:
            x = n
        if y > n:
            y = n
    return y, x


n = int(input())
line = list(input().split())
print(solution(n, line))