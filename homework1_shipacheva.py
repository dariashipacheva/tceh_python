import sys

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

while True:
    users_input_1 = input_function ('Введите значение двоичного числа 101001 в десятичной системе:')
    if users_input_1 == '41':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_2 = input_function ('Введите знак для переноса строки:')
    if users_input_2 == '/n':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_3 = input_function ('Какой оператор в Python "не такой как все"?')
    if users_input_3 == 'for':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')        

while True:
    users_input_4 = input_function ('"get there" not in "we got there together" - True or False?')
    if users_input_4 == 'True':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_5 = input_function ('Как будет выглядеть результирующая строка "{surname}, {name}".format(name = "Maria", surname = "Ivanova"):')
    if users_input_5 == 'Ivanova, Maria':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_6 = input_function ('Результат функции len("Лавировали, лавировали, да не вылавировали"):')
    if users_input_6 == '42':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_7 = input_function ('Какой знак целочисленного деления в Python 2?')
    if (users_input_7 == '/' or users_input_7 == '//'):
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')

while True:
    users_input_8 = input_function ('Какого типа будет результирующее число в операции "1+2.0"?')
    if users_input_8 == 'float':
        print ('Верно!')
        break
    else:
        print ('Ошибка! Попробуйте еще раз')