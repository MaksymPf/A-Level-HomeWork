# Банкомат выдает сумму максимально возможными купюрами

amount = int(input('Input amount: '))
bill = 0

if amount:
    bill = amount // 1000
    if bill:
        print(bill, 'x 1000')
    amount %= 1000
    if amount:
        bill = amount // 500
        if bill:
            print(bill, 'x 500')
        amount %= 500
        if amount:
            bill = amount // 200
            if bill:
                print(bill, 'x 200')
            amount %= 200
            if amount:
                bill = amount // 100
                if bill:
                    print(bill, 'x 100')
                amount %= 100
                if amount:
                    bill = amount // 50
                    if bill:
                        print(bill, 'x 50')
                    amount %= 50
                    if amount:
                        bill = amount // 20
                        if bill:
                            print(bill, 'x 20')
                        amount %= 20
                        if amount:
                            bill = amount // 10
                            if bill:
                                print(bill, 'x 10')
                            amount %= 10
                            if amount:
                                bill = amount // 5
                                if bill:
                                    print(bill, 'x 5')
                                amount %= 5
                                if amount:
                                    bill = amount // 2
                                    if bill:
                                        print(bill, 'x 2')
                                    amount %= 2
                                    if amount:
                                        bill = amount // 1
                                        print(bill, 'x 1')
                                        amount %= 1
else:
    print("Is it so difficult to use numbers???")




input()