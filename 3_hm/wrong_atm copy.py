# Банкомат выдает суммy мелкими, но не больше 10 штук каждой мелкой купюры

amount = int(input('Input amount: '))
banknotes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
par = 0

if amount <= 19000:
    for i in banknotes:
        if amount > i:
            while (par < 10) and (amount >= i):
                amount -= i
                par += 1
            print(i, 'x', par)
            par -= 10
    print('\nThank you. You lost', amount, 'uah')
else:
    print('\nSorry. I dont have so much money(')

input()