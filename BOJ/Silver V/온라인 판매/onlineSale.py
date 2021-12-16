n, m = map(int, input().split())

p = []
for i in range(m):
    p.append(int(input()))

p.sort()

answer = [0, 0]
for i in range(len(p)):
    result = p[i] * (len(p) - i if len(p) - i <= n else n)
    if result > answer[1]:
        answer[0] = p[i]
        answer[1] = result

print(" ".join(map(str, answer)))