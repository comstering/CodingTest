n, m = map(int, input().split())

# input
lamp = []
for _ in range(n):
    row = list(map(bool, map(int, list(input()))))
    lamp.append(row)

k = int(input())

# count same row
same_row = [0] * n
for i in range(n):
    for j in range(n):
        if lamp[i] == lamp[j]:
            same_row[i] += 1

# result answer
answer = 0
for i in range(n):
    off_count = lamp[i].count(False)
    if off_count <= k and (k - off_count) % 2 == 0:
        answer = same_row[i] if same_row[i] > answer else answer

print(answer)