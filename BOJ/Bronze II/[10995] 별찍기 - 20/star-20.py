n = int(input())

for i in range(n):
    print(' ' if i % 2 else '', end='')
    for j in range(n):
        print('*', end=' ')
    print()