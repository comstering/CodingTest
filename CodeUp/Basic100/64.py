a, b, c = map(int, input().split())
d = a if a < b else b if b < c else c
d = d if d < c else c
print(d)