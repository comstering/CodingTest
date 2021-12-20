str_num = input()
count = [0] * 10

for i in str_num:
    num = int(i)
    if num == 6:
        num = 6 if count[num] <= count[9] else 9
    elif num == 9:
        num = 9 if count[num] <= count[6] else 6
    count[num] += 1

print(max(count))
