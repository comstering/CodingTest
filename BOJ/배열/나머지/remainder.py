value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
remainder = []

for i in value:
    value[i] = int(input())
    remainder.append(value[i] % 42)

setting = set(remainder)
print(len(setting))

