n = int(input())
strList = []
for i in range(n):
    strList.append(input())
strList = list(set(strList))
strList.sort()
strList = sorted(strList, key=lambda x: len(x))
for i in strList:
    print(i)