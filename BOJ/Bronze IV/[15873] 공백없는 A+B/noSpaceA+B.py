num = input()
answer = 0
if num[1] == '0':
    answer = int(num[:2]) + int(num[2:])
else:
    answer = int(num[0]) + int(num[1:])
print(answer)
