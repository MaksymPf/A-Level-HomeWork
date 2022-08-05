# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

import re

f = 'Little_Red-Cap_short.txt'
file = open(f, 'r', encoding='utf-8')

words_list = list(re.findall(r'\b\w+\b', file.read())) # удаление всех знаков препинания и создание списка
words_set = set(words_list) # переделал в множество

print(words_list)
print('\n\n', words_set, '\n\n')

count = 0

for a in words_set:
    count -= count
    for b in words_list:
        if a == b:
            count += 1
        else:
            pass
    print('\t', count, a)    

file.close()

input()