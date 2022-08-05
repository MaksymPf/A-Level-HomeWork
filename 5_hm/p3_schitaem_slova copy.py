# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

import re

f = 'Little_Red-Cap_short.txt'
file = open(f, 'r', encoding='utf-8')

words_list = list(re.findall(r'\b\w+\b', file.read())) # удаление всех знаков препинания и создание списка
words_set = set(words_list) # переделал в множество

print(words_list, '\n\n')

#if words_tuple[10] in words_list:
#    print('DA')
#else:
#    print('NO')
#print(words_tuple[10], {words_list.count(words_tuple[10])})

def hui(word):
    counter = word, (words_list.count(word))
    return counter

print(list(map(hui, words_set)))

file.close()

input()