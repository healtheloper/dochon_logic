import sys

input = sys.stdin.readline

price = int(input())
money = 1000-price

coin_type = [500, 100, 50, 10, 5, 1]
coin_count = 0

for coin in coin_type:
    coin_count += money // coin
    money %= coin

print(coin_count)