num = int(input())
for i in range(1, num + 1):
    print('X' if i == 3 or i == 6 or i == 9 else i, end=" ")