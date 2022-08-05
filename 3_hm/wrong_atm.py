# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры

amount = int(input('Input amount: '))
banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
par = 0

for i in banknotes:
    if amount > (i * 10):
        while par < 10:
            amount -= i
            par += 1
        print(i, 'x', par)
        par -= 10
    elif amount >= i:
        while amount >= i:
            amount -= i
            par += 1
        print(i, 'x', par)
        par -= 10

print('\nThank you. You lost:', amount, 'uah')

input()