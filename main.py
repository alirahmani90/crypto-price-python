import cryptocompare
import os
coins = ['BTC','ETH']

price_irt = []
price_usd = []

while True:
    for coin in coins:
        price_usd.append(cryptocompare.get_price(coin,currency='USD')[coin]['USD'])
        price_irt.append(cryptocompare.get_price(coin,currency='IRR')[coin]['IRR']/10)
    x = 0
    os.system('cls')
    for coin in coins:
        print(f"{coin} price : {price_usd[x]} (USD)")
        print(f"{coin} price : {price_irt[x]} (Toman)\n")
        x += 1
    # print(price_usd)    


# print(cryptocompare.get_price('BTC',currency='USD')['BTC']['USD'])