# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

gradebook = {'Max S': [6, 5, 7], 'Danil L':[10, 9, 8], 'Alex P':[6, 9, 9]}

print(gradebook)
print('\n')

gb_midle = {}
for student, rate in gradebook.items():
    midle = sum(rate) / len(rate)
    gb_midle[midle] = student

max_s = max(gb_midle.items())
min_s = min(gb_midle.items())

print('Successful student', max_s)
print('Lagging student', min_s)

input()