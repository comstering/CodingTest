num = int(input())
for na in range(0, num):
    k = int(input())
    n = int(input())
    base = []
    for i in range(0, n):
        base.append(i + 1)
    apart = []
    for i in range(0, k):
        floor = []
        for j in range(0, n):
            if i == 0:
                floor.append((base[j] * (base[j] + 1)) // 2)
            else:
                summary = 0
                for k in range(0, j + 1):
                    summary += apart[i - 1][k]
                floor.append(summary)
        apart.append(floor)
    print(apart[-1][-1])