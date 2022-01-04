money = int(input())
money = 1000 - money

change_list = [500, 100, 50, 10, 5, 1]
coin = 0

for i in change_list:
    coin += money // i
    money %= i

print(coin)