def checkWord(word):
    spells = []
    set_spells = set(word)
    for i in word:
        if len(spells) > 0:
            if spells[-1] == i:
                continue
        spells.append(i)
    return 1 if len(spells) == len(set_spells) else 0


num = int(input())
count = 0
for i in range(num):
    word = input()
    count += checkWord(word)

print(count)
