n = int(input())

space1 = []

for i in range(n):
    space1.append(input())

space2 = [''.join(i) for i in zip(*space1)]

horizontal = 0
vertical = 0

for i in range(n):
    for j in space1[i].split('X'):
        if '..' in j:
            horizontal += 1
    for j in space2[i].split('X'):
        if '..' in j:
            vertical += 1

print(horizontal, vertical)