# выяснение являеться ли год высокосным

print('Тут определиться являеться ли год високосным')
print('\nВведите год:')
year = int(input())

if year % 4 == 0 and year % 400 == 0:
    print('\nЭтот год високосный')
elif year % 100 == 0:
    print('\nЭтот год НЕвисокосный')
elif year % 4 == 0:
    print('\nЭтот год високосный')

input('\n\nPress Enter for exit')

