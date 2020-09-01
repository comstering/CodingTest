a = int(input())
score = list(map(int, input().split()))
summary = 0
for i in score:
    summary += i/max(score)*100
print(summary/a)