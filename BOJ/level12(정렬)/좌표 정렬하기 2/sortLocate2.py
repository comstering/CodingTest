import sys
n = int(sys.stdin.readline())

locate_list = []
for i in range(n):
    locate = tuple(map(int, sys.stdin.readline().split()))
    locate_list.append(locate)

locationList = sorted(locate_list, key=lambda x: (x[1], x[0]))

for i in locationList:
    print(i[0], i[1])