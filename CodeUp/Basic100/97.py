badook = []
for i in range(0, 19):
    badook.append(list(map(int, input().split())))
num = int(input())
for i in range(0, num):
    a, b = map(int, input().split())
    for j in range(0, 19):
        for k in range(0, 19):
            if j == a - 1 or k == b - 1:
                if j == a - 1 and k == b - 1:
                    continue
                elif badook[j][k] == 1:
                    badook[j][k] = 0
                else:
                    badook[j][k] = 1
for i in badook:
    for j in i:
        print(j, end=" ")
    print()