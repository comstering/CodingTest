T = int(input())

result = []
while T > 0:
    a, b = input().split()
    result.append(int(a) + int(b))
    T -= 1

for i in result:
    print(i)