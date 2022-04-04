prices = [98, 47.09, 54, 32.80, 75.25, 29, 36.50, 87, 41.70, 26]

for i in prices:
    rub, kop = f'{i:.2f}'.split('.')
    print(f'{rub} руб {kop} коп,', end = ' ')

print(id(prices))

prices.sort()
print(id(prices))
print(prices)

prices_1 = sorted(prices, reverse=True)
print(prices_1)

max_list = prices_1 [:5]
print(max_list)