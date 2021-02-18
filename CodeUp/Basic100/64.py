a, b, c = map(int, input().split())
z = a if a < b else b
print(c if c < z else z)