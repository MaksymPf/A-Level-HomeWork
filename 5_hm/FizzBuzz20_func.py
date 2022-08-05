# fizz buzz для 20 троек чисел и импорт файла
# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!
# Скорее всего будет далеко от идеала(((

def open_files(file_r_name, file_w_name):
    '''открывает файлы'''
    file = open(file_r_name, 'r', encoding='utf-8')
    new_file = open(file_w_name, 'w', encoding='utf-8')
    return file, new_file

def count(file, new_file):
    '''считает Fizz Buzz'''
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

def close_files(file, new_file):
    '''закрывает файлы'''
    file.close()
    new_file.close()

def read_new_file():
    '''Читает новый файл с FizzBuzz'''
    print('Читаю, что получилось в новом файле!\n')
    new_file = open('new_file_FizzBuzz.txt', 'r', encoding='utf-8')
    print(new_file.read())
    new_file.close()

def main():
    file, new_file = open_files('20troek.txt', 'new_file_FizzBuzz.txt')
    count(file, new_file)
    close_files(file, new_file)
    read_new_file()

main()

input('\n\npress Enter for exit')