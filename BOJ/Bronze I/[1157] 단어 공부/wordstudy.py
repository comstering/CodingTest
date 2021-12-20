word = input().upper()
setting = list(set(word))
a = list(map(word.count, setting))
if a.count(max(a)) != 1:
    print("?")
else:
    print(setting[a.index(max(a))])