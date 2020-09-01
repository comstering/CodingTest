a = int(input())
test = []
count = 0
while count < a:
    test.append(input())
    count += 1
for i in test:
    score = 0
    one = 0
    for j in i:
        if j == 'O':
            one += 1
        else:
            one = 0
        score += one
    print(score)
