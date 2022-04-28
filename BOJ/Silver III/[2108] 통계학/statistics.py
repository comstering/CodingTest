import sys
from collections import Counter
n = int(sys.stdin.readline())
numList = []
for i in range(n):
    numList.append(int(sys.stdin.readline()))
numList.sort()
sys.stdout.write("{0}\n".format(round(sum(numList) / n)))
sys.stdout.write("{0}\n".format(numList[n // 2]))
cnt = Counter(numList)
mod = cnt.most_common(2)
sys.stdout.write("{0}\n".format(mod[0][0] if len(mod) < 2 else mod[0][0] if mod[0][1] != mod[1][1] else mod[1][0]))
sys.stdout.write("{0}\n".format(numList[-1] - numList[0]))
