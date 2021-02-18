n = int(input())
a = []
for i in range(0, n):
    a.append(tuple(map(int, input().split())))
badook = [[0 for i in range(19)] for j in range(19)]
for i in a:
    badook[i[0] - 1][i[1] - 1] = 1
for i in badook:
    for j in i:
        print(j, end=' ')
    print()