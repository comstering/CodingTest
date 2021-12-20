array = []
for i in range(1, 10001):
    strnum = str(i)
    if i > 10000:
        break
    for j in strnum:
        i += int(j)
    array.append(i)
array.sort()
array = set(array)
array = list(array)
for i in range(1, 10001):
    for j in array:
        if i == j:
            break
        if i < j:
            print(i)
            break