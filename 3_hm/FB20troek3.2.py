# fizz buzz для 20 троек чисел и импорт файла

f = '20troek.txt'
file = open(f, 'r', encoding='utf-8')
new_file = open('new_file_FizzBuzz.txt', 'w', encoding='utf-8')

for lines in file:
    num_list = list(map(int, lines.split()))  #разделяем обьекты в строке по пробелам с помощью lines.split()
    fizz, buzz, end = num_list
    for i in range(1, (end+1)):
        if i % fizz == 0 and i % buzz == 0:
            new_file.write('FB ')
        elif i % fizz == 0:
            new_file.write('F ')
        elif i % buzz == 0:
            new_file.write('B ')
        else:
            new_file.write(str(i))
            new_file.write(' ') #чтобы был пробел после значения i
    new_file.write('\n')
file.close()
new_file.close()

print('Читаю, что получилось в новом файле!')
new_file = open('new_file_FizzBuzz.txt', 'r', encoding='utf-8')
print(new_file.read())
new_file.close()

input('\n\npress Enter for exit')