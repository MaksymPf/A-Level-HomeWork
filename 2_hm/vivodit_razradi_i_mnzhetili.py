# Ввести число, вывести его разряды и множители

numb = int(input('Input some big number: '))
rank = 1

while numb > rank:
    factor = (numb // rank) % 10
    print (factor, rank)
    rank *= 10

input('\n\npress Enter for exit')