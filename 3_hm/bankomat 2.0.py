# Банкомат выдает сумму максимально возможными купюрами

amount = int(input('Input amount: '))
banknotes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in banknotes:
    par = amount // i
    amount %= i
    if par:
        print(i,'x', par)

input()