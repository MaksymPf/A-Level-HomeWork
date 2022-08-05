# проверка валидности пароля (трай 2)

print("""
Введите валидный пароль.

Условия валидности следующие:
- Пароль должен иметь длину не менее 6 символов
- Содержать такие буквы: F, K, и D или С
- Не должен содержать цифры 1 и 6
- Если в пароле есть #, то должна быть буква а
""")

password = str(input('\nВведите пароль:'))
length = len(password) > 5
letters = 'F' in password and 'K' in password and 'D' in password or 'C' in password
numb = '1' not in password and '6' not in password

if length and letters and numb:
    print('Валидный пароль')
else:
    print('Невалиднный пароль')

input('\n\npress Enter for exit')
