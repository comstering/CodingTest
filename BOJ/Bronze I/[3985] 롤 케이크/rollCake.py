l = int(input())
n = int(input())

cake = [True] * l
guessPiece = 0
realPiece = 0
guess = 0
real = 0
for i in range(n):
    p, k = map(int, input().split())
    if guessPiece < k - p:
        guessPiece = k - p
        guess = i + 1
    count = 0
    for j in range(p, k + 1):
        if cake[j - 1]:
            cake[j - 1] = False
            count += 1
    if count > realPiece:
        realPiece = count
        real = i + 1

print(guess)
print(real)
