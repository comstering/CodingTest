count = 0
array = []
max = 0
while count < 9:
    array.append(int(input()))
    if max < array[count]:
        max = array[count]
    count += 1

print(max, end=" ")
print(array.index(max) + 1)