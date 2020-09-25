n = 1260    # 주어야할 거스름돈
count = 0

coinList = [500, 100, 50, 10]    # 동전 리스트

for coin in coinList:
    count += n // coin
    n %= coin

print(count)