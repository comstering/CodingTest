num = int(input())
count = 1
size = 1
while True:
    if size >= num:
        break
    size += 6 * count
    count += 1
print(count)