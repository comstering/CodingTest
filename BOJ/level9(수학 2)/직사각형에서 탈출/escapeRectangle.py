x, y, w, h = map(int, input().split())
dx = w - x if w - x < x else x
dy = h - y if h - y < y else y
print(dx if dx < dy else dy)