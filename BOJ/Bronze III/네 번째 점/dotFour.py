dotList = []
for i in range(3):
    dotList.append(list(map(int, input().split())))
xList = []
yList = []
for i in dotList:
    x, y = i
    xList.append(x)
    yList.append(y)
xList.sort()
yList.sort()
num1 = xList[0] if xList.count(xList[0]) != 2 else xList[2]
num2 = yList[0] if yList.count(yList[0]) != 2 else yList[2]
print(num1, num2)