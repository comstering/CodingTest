a = input()
b = len(a)
for i in a:
    b -= 1
    c = int(i) * (10**b)
    print('[{0}]'.format(c))