case = int(input())
for i in range(0, case):
    repeat, word = input().split()
    for j in list(word):
        print(j * int(repeat), end="")
    print()