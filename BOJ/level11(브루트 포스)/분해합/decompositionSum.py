num = int(input())
for i in range(num):
    su = i + sum(map(int, str(i)))
    if su == num:
        print(i)
        exit()
print(0)