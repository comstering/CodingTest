a = int(input())
b = int(input())
c = int(input())

number = str(a * b * c)
count = 0

while count < 10:
    print(number.count(str(count)))
    count += 1
