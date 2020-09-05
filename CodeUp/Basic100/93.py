input()
array = [0] * 23
for i in map(int, input().split()):
    array[i - 1] += 1
for i in array:
    print(i, end=" ")
