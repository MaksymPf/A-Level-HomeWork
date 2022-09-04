'''
file for checking code
'''
import workers

if __name__ == '__main__':
    worker1 = workers.Developer('Alex', 100, ['Python', 'Java'])
    worker2 = workers.Recruiter('Sofi', 80)
    worker3 = workers.Developer('Max', 70, ['Python'])

    print(worker1)
    print(worker1.work())
    print('For working days I get:', worker1.check_salary(), '\n')

    print(worker2)
    print(worker2.work())
    print('For working days I get:', worker2.check_salary(), '\n')

    print(worker1 == worker3)
    print(worker1 + worker3)

    input('\n\nPress Enter')
