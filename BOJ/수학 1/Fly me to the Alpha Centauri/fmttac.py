import math
num = int(input())

for na in range(0, num):
    x, y = map(int, input().split())
    interval = y - x
    if interval < 4:
        print(interval)
    else:
        n = int(math.sqrt(interval))
        if interval == n ** 2:
            print(2 * n - 1)
        elif n ** 2 < interval <= n ** 2 + n:
            print(2 * n)
        else:
            print(2 * n + 1)
