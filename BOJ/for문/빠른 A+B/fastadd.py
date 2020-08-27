import sys

T = int(sys.stdin.readline())

result = []
while T > 0:
    a, b = sys.stdin.readline().split()
    result.append(int(a) + int(b))
    T -= 1

for i in result:
    print(i)