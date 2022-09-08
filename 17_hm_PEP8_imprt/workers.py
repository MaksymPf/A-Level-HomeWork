'''
classes Developer and Recruiter using as parental class imported Employee
by these classes we can assign a position for employee
'''
from employee import Employee

class Developer(Employee):
    '''
    gets name, salary_per_day and tech_stack(list of programing languages that one developer know)
    comparing developers by tech_stack
    '''
    def __init__(self, name: str, salary_per_day: int, tech_stack: list):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'Developer: {self.name}'

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
        name = (self.name + ' / ' + other.name)
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.salary_per_day, other.salary_per_day)
        return self.__class__(name, tech_stack, salary)

    def work(self):
        return 'I come to the office and start to coding.'


class Recruiter(Employee):
    '''
    gets name and salary_per_day
    class for recruiters
    '''
    def __init__(self, name: str, salary_per_day: int):
        super().__init__(name, salary_per_day)

    def __str__(self):
        return f'Recruiter: {self.name}'

    def work(self):
        return 'I come to the office and start to hiring.'
