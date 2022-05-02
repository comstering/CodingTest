l = int(input())
a = input()

r = 31
m = 1234567891

num = 0
result = 0
for i in a:
    result += (ord(i) - 96) * (r ** num)
    num += 1
    result %= m
print(result)
