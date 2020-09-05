mapping = []
for i in range(0, 10):
    mapping.append(list(map(int, input().split())))
a = 1
check = 0
for i in range(1, 11):
    for j in range(a, 11):
        if mapping[i][j] == 2:
            check = 1
        mapping[i][j] = 9
        if mapping[i][j + 1] == 1 or check == 1:
            break
        a += 1
    if check == 1 or mapping[i + 1][a] == 1:
        break
for i in mapping:
    for j in i:
        print(j, end=" ")
    print()