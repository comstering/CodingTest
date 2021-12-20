def facto(n):
    if n == 1 or n == 0:
        return 1
    return n * facto(n - 1)


num = int(input())
print(facto(num))