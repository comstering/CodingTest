n, m = map(int, input().split())
cardList = []
for i in range(n):
    cardList.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    if answer < min(cardList[i]):
        answer = min(cardList[i])

print(answer)