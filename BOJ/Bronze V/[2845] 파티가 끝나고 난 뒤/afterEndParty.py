l, p = map(int, input().split())
news = list(map(int, input().split()))

result = list(map(lambda x : x - (l * p), news))
for i in result:
    print(i, end=' ')