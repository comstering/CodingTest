h, w = map(int, input().split())
a = []
for i in range(0, h):
    a.append([0]*w)
n = int(input())
for i in range(0, n):
    l, d, x, y = map(int, input().split())
    for j in range(0, h):
        for k in range(0, w):
            if d == 0:
                if j == x - 1 and y - 1 <= k < y + l - 1:
                    a[j][k] = 1
            if d == 1:
                if x - 1 <= j < x + l - 1 and k == y - 1:
                    a[j][k] = 1
for i in a:
    for j in i:
        print(j, end=" ")
    print()