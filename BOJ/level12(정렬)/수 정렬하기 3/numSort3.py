import sys
n = int(sys.stdin.readline())
countList = [0] * 10001
for i in range(n):
    countList[int(sys.stdin.readline())] += 1
for i in range(len(countList)):
    if countList[i] != 0:
        for j in range(countList[i]):
            sys.stdout.write("{0}\n".format(i))