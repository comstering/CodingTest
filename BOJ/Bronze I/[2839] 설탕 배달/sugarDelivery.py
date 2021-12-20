sugar = int(input())
print(-1 if sugar in [4, 7] else sugar // 5 + sugar % 5 - sugar % 5 // 3 * 2)