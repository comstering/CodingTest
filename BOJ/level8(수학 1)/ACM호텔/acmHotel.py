num = int(input())
for i in range(0, num):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0:
        floor = H
        room -= 1
    floor *= 100
    print(floor + room)