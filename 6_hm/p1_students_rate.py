# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

gradebook = {'Max S': [6, 5, 7], 'Danil L':[10, 9, 8], 'Alex P':[6, 9, 9]}

print(gradebook)
print('\n')

gb_midle = {}
for student, rate in gradebook.items():
    midle = sum(rate) / len(rate)
    gb_midle[student] = midle
# новый список с средними значениями оценок

max_s = max(gb_midle.values()) # лучшая средняя оценка
min_s = min(gb_midle.values()) # худшая средняя оценка

for student1, rate1 in gb_midle.items():
    if rate1 == max_s:
        print('Successful student:', student1, 'with average score:', rate1)

for student1, rate1 in gb_midle.items():       
    if rate1 == min_s:
        print('Lagging student', student1, 'with average score:', rate1)

input()