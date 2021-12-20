n, k = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

i = 0
count = 0
while True:
    count += 1
    i = a[i]
    if i == k:
        break
    if count > n:
        count = -1
        break

print(count)
