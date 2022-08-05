# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внтри функции нужно просто обращаться к правильно составленному словарю.

dict_sizes2 = {'International variants': ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'],
'German size': [36, 38, 40, 42, 44, 46, 48], 'USA size': [8, 10, 12, 14, 16, 18, 20],
'French size': [38, 40, 42, 44, 46, 48, 50], 'GB size': [24, 26, 28, 30, 32, 34, 36]}

print(dict_sizes2['International variants'][0])

size = input('Input size: ')
size = size.upper()

def index():
    count = -1
    index = 0
    for i in dict_sizes2.values():
        for d in i:
            count += 1
            if d == size:
                index = count
    return index          

numb = index()

print('\n')
for key, values in dict_sizes2.items():
    print(key+':', values[numb])

input()