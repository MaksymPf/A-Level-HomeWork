'''
file for parental class Employee
'''

import datetime

class Employee:
    '''
    gets name of employee and salary per one working day
    comparing employees by salary
    method check_salary can count all salary for this month
    '''

    def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day

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

    def __str__(self):
        return f'Employee: {self.name}'

    def work(self):
        return 'I come to the office.'
    
    def check_salary(self):
        '''counting amount of salary for this month using module datatime and self.salary_per_day'''
        now = datetime.date.today()
        holidays = {datetime.date(now.year, 8, 24)}
        business_days = 0

        for i in range(1, 32):
            this_date = datetime.date(now.year, now.month, i)
            if this_date == now:
                break
            elif this_date.weekday() < 5 and this_date not in holidays: # Monday == 0, Sunday == 6
                business_days += 1

        return self.salary_per_day * business_days
