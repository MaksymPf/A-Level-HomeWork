# 1. Створити клас Employee.
# 2. Конструктор __int__(self) має приймати наступні аргументи: ім’я, ЗП за один робочий день.
# 3. Створити метод work(self, …) який повертає строку “I come to the office.”
# 4. Створити класи Recruiter та Developer, які наслідують клас Employee.
# 5. Перевизначити методи work  в класах R та D, щоб вони повертали значення:
#       “I come to the office and start to coding.” - для Developer
#       “I come to the office and start to hiring.” - для Recruiter
# 6. Перевизначити методи  __str__, щоб вони повертали строку: “Посада: Ім’я”
# 7. Зробити можливим порівнювати Employee по рівню ЗП.
# 8. Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.
# 9. ** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до поточного дня, не враховуючи вихідні дні.
# 10. Додати в конструктор __int__(self) класу Developer атрибут tech_stack (список з назвами технологій).
# 11. Для класу Developer зробити порівняння за кількістю технологій.
# 12. Зробити можливим операцію додавання об’єктів класу Developer. Результатом має бути новий об’єкт
# В якому name = name1 + ‘ ’ + name2, a tech_stack - список з технологій двох об’єктів (тільки унікальні значення), ЗП - більша з двох.

import datetime

class Employee:
    def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        return 'I come to the office.'
    
    def check_salary(self):
        now = datetime.date.today()
        holidays = {datetime.date(now.year, 8, 24)}
        businessdays = 0 

        for i in range(1, 32):
            thisdate = datetime.date(now.year, now.month, i)

            if thisdate == now:
                break
            elif thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6 
                businessdays += 1

        return self.salary_per_day * businessdays

    # def check_salary(self, days: int):
    #     return self.salary_per_day * days

    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day

    def __le__(self, other):
        return self.salary_per_day <= other.salary_per_day

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day

    def __ge__(self, other):
        return self.salary_per_day >= other.salary_per_day

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

    def __ne__(self, other):
        return self.salary_per_day != other.salary_per_day


class Developer(Employee):
    def __init__(self, name: str, salary_per_day: int, tech_stack: list):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'Developer: {self.name}'

    def work(self):
        return 'I come to the office and start to coding.'

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __le__(self, other):
        return self.tech_stack <= other.tech_stack

    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

    def __ge__(self, other):
        return self.tech_stack >= other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.tech_stack

    def __ne__(self, other):
        return self.tech_stack != other.tech_stack
    
    def __add__(self, other):
        name = f'{self.name} / {other.name}'
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.salary_per_day, other.salary_per_day)
        return Developer(name, tech_stack, salary)


class Recruiter(Employee):
    def __init__(self, name: str, salary_per_day: int):
        super().__init__(name, salary_per_day)

    def __str__(self):
        return f'Recruiter: {self.name}'

    def work(self):
        return 'I come to the office and start to hiring.'


worker1 = Developer('Alex', 100, ['Python', 'Java'])
worker2 = Recruiter('Sofi', 80)
worker3 = Developer('Max', 70, ['Python'])

print(worker1)
print(worker1.work())
print('For working days I get:', worker1.check_salary(), '\n')

print(worker2)
print(worker2.work())
print('For working days I get:', worker2.check_salary(), '\n')

#print(worker1 > worker2)  # don't work anymore
print(worker1 == worker3)
print(worker1 + worker3)

input('\n\nPress Enter')
