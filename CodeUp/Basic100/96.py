a = []
for i in range(0, int(input())):
    a.append(tuple(map(int, input().split())))
for i in range(0, 19):
    for j in range(0, 19):
        check = 0
        for k in a:
            if (i + 1, j + 1) == k:
                check = 1
                print("1", end=" ")
                break
        if check == 1:
            continue
        print("0", end=" ")
    print()