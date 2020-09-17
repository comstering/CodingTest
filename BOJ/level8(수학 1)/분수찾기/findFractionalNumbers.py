x = int(input())
line = 1
# [1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1], [5/1, 4/2, 3/3, 2/4, 1/5]
# 한 라인마다 분자: +1, 분모: -1 or 분자: -1, 분모: +1
while x > line:    # 라인 구하기
    x -= line
    line += 1
if line % 2 == 0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x
print(str(a) + "/" + str(b))