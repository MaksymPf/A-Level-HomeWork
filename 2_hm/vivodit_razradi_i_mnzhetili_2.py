# Ввести число, вывести его разряды и множители

numb = input('Input some big number: ')

for i in range(len(numb)):
    print(numb[i], end=' ')
    print('1'+'0'*(len(numb)-(i+1)))


input('\n\npress Enter for exit')