n, m = map(int, input().split())

num_list = [1] * m

idx = m - 1
while True:
    for i in num_list:
        print(i, end=' ')
    print()
    if num_list[0] == n:
        break
    while True:
        if num_list[idx] == n:
            idx -= 1
        else:
            break

    num_list[idx] += 1

    for i in range(idx + 1, m):
        num_list[i] = num_list[idx]
    idx = m - 1