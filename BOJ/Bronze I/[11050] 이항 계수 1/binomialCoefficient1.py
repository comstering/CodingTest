n, k = map(int, input().split())

result = 1

for i in range(n, n - k, -1):
    result *= i

for i in range(0, k):
    result //= i + 1
print(result)
