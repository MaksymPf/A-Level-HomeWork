# fizz buzz

print('\tПривет!\n\tВведи три числа:\n')
first_numb = int(input('первое:\t'))
second_numb = int(input('второе:\t'))
third_numb = int(input('третье:\t'))

for i in range(1, (third_numb+1)):
    if i % first_numb == 0 and i % second_numb == 0:
        print('FB', end=' ')
    elif i % first_numb == 0:
        print('F', end=' ')
    elif i % second_numb == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')

input('\n\npress Enter for exit')
