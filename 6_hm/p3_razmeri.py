# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внтри функции нужно просто обращаться к правильно составленному словарю.

dict_sizes = {'XXS': ['German size 36', 'USA size 8', 'French size 38', 'GB size 24'],
'XS': ['German size 38', 'USA size 10', 'French size 40', 'GB size 26'],
'S': ['German size 40', 'USA size 12', 'French size 42', 'GB size 28'],
'M': ['German size 42', 'USA size 14', 'French size 44', 'GB size 30'],
'L': ['German size 44', 'USA size 16', 'French size 46', 'GB size 32'],
'XL': ['German size 46', 'USA size 18', 'French size 48', 'GB size 34'],
'XXL': ['German size 48', 'USA size 20', 'French size 50', 'GB size 36'],
}

def count():
    for i in dict_sizes[size]:
        print(i)
    return

size = input('Input size: ')
size = size.upper()

print('\nFor size', size, 'international variants:')
count()

input('\nPress Enter to o check how works other part of code')

# Вриант по сложнее (на мой взгляд)
dict_sizes2 = {'International variants': ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'],
'German size': [36, 38, 40, 42, 44, 46, 48], 'USA size': [8, 10, 12, 14, 16, 18, 20],
'French size': [38, 40, 42, 44, 46, 48, 50], 'GB size': [24, 26, 28, 30, 32, 34, 36]}

#print(dict_sizes2['International variants'][0])

size = input('\n\nInput size: ')
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