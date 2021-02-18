h, w = map(int, input().split())
a = [[0 for i in range(w)] for j in range(h)]
n = int(input())
for i in range(0, n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        a[x - 1][y - 1:y + l - 1] = [1 for j in range(l)]
    if d == 1:
        for j in range(x - 1, x + l - 1):
            a[j][y - 1] = 1
for i in a:
    for j in i:
        print(j, end=" ")
    print()