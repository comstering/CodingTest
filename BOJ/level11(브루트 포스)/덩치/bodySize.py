num = int(input())
dunList = []
score = [1] * num
for i in range(num):
    x, y = map(int, input().split())
    dunList.append((x, y))
for i in range(num):
    for j in range(num):
        if dunList[i][0] < dunList[j][0] and dunList[i][1] < dunList[j][1]:
            score[i] += 1
score = list(map(str, score))
print(" ".join(score))