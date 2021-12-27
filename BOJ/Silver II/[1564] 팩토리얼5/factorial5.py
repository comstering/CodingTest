num = int(input())

fac_num = 1
for i in reversed(range(num)):
    fac_num *= i + 1
    while fac_num % 10 == 0:
        fac_num //= 10
    fac_num %= 1000000000000

print(f'{fac_num % 100000:0>5}')