num = int(input())
count = 0
for i in range(0, num):
    word = input()
    check = 1
    for j in range(0, len(word) - 2):
        if word[j] == word[j + 1]:
            continue
        for k in range(j + 2, len(word)):
            if word[j] == word[k]:
                check = 0
                break
        if check == 0:
            break
    if check == 1:
        count += 1

print(count)