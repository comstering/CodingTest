case = int(input())

for i in range(case):
    word1, word2 = input().split()
    print(f"{word1} & {word2} are{'' if ''.join(sorted(word1)) == ''.join(sorted(word2)) else ' NOT'} anagrams.")
