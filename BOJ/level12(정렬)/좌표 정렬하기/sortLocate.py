import sys
n = int(sys.stdin.readline())
locate_list = []
for i in range(n):
    locate = tuple(map(int, sys.stdin.readline().split()))
    locate_list.append(locate)

locate_list.sort()

for i in locate_list:
    print(i[0], i[1])