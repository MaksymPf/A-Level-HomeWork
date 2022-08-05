# Пргорамма выводит сама себя задом на перед

import sys
filename = sys.argv[0]

f = open(filename, 'r', encoding='utf-8')
for line in reversed(list(f)):
    print(line, end='') #если написать print(line[::-1]) - то будет совсем задом на перед
f.close()


input()