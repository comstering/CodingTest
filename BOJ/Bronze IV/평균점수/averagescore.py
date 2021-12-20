count = 0
sum = 0

while count < 5:
    score = int(input())
    if score < 40:
        score = 40

    sum += score
    count += 1


average = sum // 5

print(average)