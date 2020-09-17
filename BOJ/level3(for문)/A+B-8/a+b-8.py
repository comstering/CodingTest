import sys

T = int(sys.stdin.readline())

result = []
while T > 0:
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    result.append((a, b, a + b))
    T -= 1

count = 1

for i in result:
    print("Case #" + str(count) + ": " + str(i[0]) + " + " + str(i[1]) + " = " + str(i[2]))
    count += 1