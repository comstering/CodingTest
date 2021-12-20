scores = []
for i in range(5):
    score = int(input())
    score = 40 if score < 40 else score
    scores.append(score)
print(sum(scores) // 5)