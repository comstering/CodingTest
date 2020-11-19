import sys
n = int(sys.stdin.readline())
locationList = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    locationList.append((x, y))

num = len(locationList)

for i in range(n - 1):
    for j in range(i + 1, n):
        if locationList[i][0] > locationList[j][0] or (locationList[i][0] == locationList[j][0] and locationList[i][1] > locationList[j][1]):
            locationList[i], locationList[j] = locationList[j], locationList[i]

for i in locationList:
    sys.stdout.write("{0} {1}\n".format(i[0], i[1]))