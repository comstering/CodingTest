import sys
n = int(sys.stdin.readline())

buildings = []

for _ in range(n):
    buildings.append(int(sys.stdin.readline()))

count = 0
next_buildings = []
for i in range(1, n):
    next_buildings.append((buildings.pop(), i))
    while next_buildings:
        if next_buildings[-1][0] < buildings[-1]:
            next_buildings.pop()
        else:
            break

    if next_buildings:
        count += i - next_buildings[-1][1]
    else:
        count += i

print(count)
