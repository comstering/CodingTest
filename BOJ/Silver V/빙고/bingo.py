bingo = [list(map(int, input().split())) for i in range(5)]
num_list = []
for i in range(5):
    num_list.extend(list(map(int, input().split())))

count = 0
for i in num_list:
    bingo_count = 0
    count += 1
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == i:
                bingo[j][k] = 0
                break

    # 가로 체크
    for v in bingo:
        if len(set(v)) == 1:
            bingo_count += 1

    # 세로 체크
    for ci in range(5):
        len_count = 0
        for cj in range(5):
            if bingo[cj][ci] != 0:
                break
            len_count += 1
        if len_count == 5:
            bingo_count += 1

    # 대각선 체크
    len_count = 0
    for ci in range(5):
        if bingo[ci][ci] != 0:
            break
        len_count += 1
    if len_count == 5:
        bingo_count += 1

    len_count = 0
    for ci in range(5):
        if bingo[ci][-ci - 1] != 0:
            break
        len_count += 1
    if len_count == 5:
        bingo_count += 1

    if bingo_count >= 3:
        break

print(count)
