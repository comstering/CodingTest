remainder = []
count = 0
while count < 10:
    remainder.append(int(input()) % 42)
    count += 1
setting = set(remainder)
print(len(setting))