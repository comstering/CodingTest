text = input()
crypto = input()

count = 0

tmp = 1
for i, j in zip(reversed(crypto), range(len(crypto))):
    idx = text.find(i)
    count = (count + tmp * (idx + 1)) % 900528
    tmp = tmp * len(text) % 900528

print(count)