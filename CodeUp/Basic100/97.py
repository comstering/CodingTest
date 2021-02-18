# 바둑판 입력
badook = []
for i in range(0, 19):
    badook.append(list(map(int, input().split())))
# 십자 뒤집기 좌표 입력
num = int(input())
cross = []
for i in range(0, num):
    cross.append(tuple(map(int, input().split())))
# 십자 뒤집기 진행
for i in cross:
    badook[i[0] - 1] = [int(not b) for b in badook[i[0] - 1]]
    for j in badook:
        j[i[1] - 1] = int(not j[i[1] - 1])
# 바둑판 출력
for i in badook:
    for j in i:
        print(j, end=" ")
    print()