'''
file for checking code
'''
import traceback
import employee 

from employee import datetime as dt


def main():
    name1 = employee.Employee('John', 20, 'cartonka@gmail.com')


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
        log_message = f'{dt.datetime.now()} \n {traceback.format_exc()}'
        print(log_message)
        with open ('loggs.txt', 'a+') as fp:
            fp.write(log_message + '\n\n')
    else:
        print('Email successfully added!')

input()
