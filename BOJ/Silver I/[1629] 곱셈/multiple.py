import sys


a, b, c = map(int, sys.stdin.readline().split())

idx = 0
result = 1
tmp = a
for i in map(int, reversed(str(bin(b))[2:])):
    if idx == 0:
        tmp = tmp % c
    else:
        tmp = (tmp * tmp) % c

    if tmp == 1:
        break
    if i == 1:
        result = (result * tmp) % c
    idx += 1

print(result)
