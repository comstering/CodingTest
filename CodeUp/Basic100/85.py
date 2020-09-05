h, b, c, s = map(int, input().split())
size = h * b * c * s
print("{0:0.1f} MB".format(size / (8*1024*1024)))