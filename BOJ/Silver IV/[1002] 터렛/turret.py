import math
num = int(input())
for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    interval = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and y1 == y2:    # 중심이 같을 때
        if r1 == r2:    # 반지름이 같을 때
            print(-1)
        else:    # 반지름이 다를 때
            print(0)
    else:    # 중심이 다를 때
        if interval == r1 + r2 or interval == abs(r1 - r2):    # 외접하거나 내접할 때
            print(1)
        elif interval > r1 + r2 or interval < abs(r1 - r2):    # 접하지 않거나 원 안에 포함할 때
            print(0)
        elif interval < r1 + r2:    # 겹칠 때
            print(2)