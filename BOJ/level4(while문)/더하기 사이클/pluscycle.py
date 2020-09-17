num = input()

if len(num) == 1:
    num = '0' + num
count = 0

compare = num

while True:
    count += 1
    a = int(compare[0]) + int(compare[1])
    a = str(a)
    if len(a) == 1:
        a = '0' + a
    compare = compare[1] + a[1]
    if compare == num:
        break

print(count)