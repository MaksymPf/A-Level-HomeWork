# Создать структуру данных для студентов из имен и фамилий, можно случайных. 
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
#   студентов, которые учатся в двух и более группах
#   студентов, которые не учатся на фронтенде
#   студентов, которые изучают Python или Java

students_dict ={
'python' : {'Max', 'Huyaks', 'Alex', 'John Cena'},
'frontend' : {'Danil', 'Huyaks', 'Vetal', 'Max'},
'fullstack' : {'Alex', 'Denis', 'Uborshica', 'Vetal'},
'java' : {'Carl', 'Lera', 'John Cena', 'Danil'},
}

def two_group():
    '''func find students who learn in two or more groups'''
    all_stud = []
    good_stud = []
    for stud in students_dict.values():
        for i in stud:
            if i not in all_stud:
                all_stud.append(i)
            else:
                good_stud.append(i)
    return all_stud, good_stud

all_s, good_s = two_group()

# don't learn FrontEnd            
no_frontend = list((students_dict['python'] | students_dict['fullstack'] | students_dict['java'])- students_dict['frontend'])

# learning Python or Java
pyth_or_java = list(students_dict['python'] | students_dict['java'])

print('All Students:', all_s, '\n')
print('Learning in two or more groups:', good_s)
print('Don\'t learn FrontEnd:', no_frontend)
print('Learning Python or Java:', pyth_or_java)

input()