def f(x):
    return x * x
print(f(5))

def f(x):
    return x * x
print(type(f))
# <class 'function'>

def f(x):
    return x * x
a = f
print(a(5)) # 25
print(f(5)) # 25
#_____
def calk1(a):
    return a+a

def calk2(a):
    return a*a

def math(op, x):
    print(op(x))

math(calk1, 5)
# 10
math(calk2, 5)
# 25
#______
def calk1(a, b):
    return a+b

def calk2(a, b):
    return a*b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 5)
# 10
math(calk2, 5, 5)
# 25
#______________

def calk2(a, b):
    return a*b

def math(op, x, y):
    print(op(x, y))

calk1 = lambda a,b: a + b

math(calk1, 5, 25)  # 30

math(lambda a,b: a + b, 5, 25) # 30

#_______________________________________
# Задача 
# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []

# for i in data:
#     if i % 2 == 0:
#         out.append((i, i * i))
# print(out) # [(2, 4), (8, 64), (38, 1444)]

# lambda:

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

    # map()______________________
# Функция map() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с новыми объектами.

list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

    # Задача: 
# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в 
# качестве строки. Как превратить list строк в list чисел?

data = '1 21 3 45 8 15 23 38 2'
print(data) # 1 21 3 45 8 15 23 38 2

# data = data.split()
# print(data) # ['1', '21', '3', '45', '8', '15', '23', '38', '2']

data = list(map(int, data.split()))
print(data) # [1, 21, 3, 45, 8, 15, 23, 38, 2]
#_________
def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# filter ////////////////////
# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True
data = [15, 2, 98, 65, 178, 3, 75]
res = list(filter(lambda x: x % 10 == 5, data))
print(res) # [15, 65, 75]
#____________
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res) # [(2, 4), (8, 64), (38, 1444)]

    # zip() ////////////////////////
# Функция zip() применяется к набору итерируемых объектов и
# возвращает итератор с кортежами из элементов входных данных
# zip([1, 2, 3], ['o', 'd', 't'], ['f', 's', 't'])
# [(1, 'o', 'f'), (2, 'd', 's'), (3, 't', 't')]
# На выходе получаем набор данных, состоящий из элементов 
# соответствующих исходному набору.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
# [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) 
# [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
# Функция zip () пробегает по минимальному входящему набору

    # enumerate() ///////////////////
# Функция enumerate() применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов 
# входных данных

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3')]

        # Файлы //////////////////
# a – открытие для добавления данных.
# Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, 
# то файл будет создан и в него начнётся запись.

# r – открытие для чтения данных
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого 
# не существует, программа выдаст ошибку.

# w – открытие для записи данных.
# Позволяет записывать данные и создавать файл, если его не
# существует. (если есть, удалит и перезапишет новое)

# Миксованные режимы
# w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.

# r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

    # Режим a
colors = ['red', '8976', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # дозапись
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# нет дозаписи, прежнее удаляется

data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
# line 1

# line 2

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
# В случае перезаписи новые данные записываются, 
# а старые удаляются

        # Модуль os //////////////
# Модуль os предоставляет множество функций для работы с 
# операционной системой, причем их поведение, как правило, 
# не зависит от ОС, поэтому программы остаются переносимыми.

# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:

# import os

# os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')

# os.getcwd() # - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# os.path - является вложенным модулем в модуль os и 
# реализует некоторые полезные функции для работы с путями, 
# такие как:
# os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) # 'main.py'

# os.path.abspath(path) - возвращает нормализованный 
# абсолютный путь.
# import os
# print(os.path.abspath('main.py'))
# # 'C:/Users/79190/PycharmProjects/webproject/main.py'


        # Модуль shutil ////////////
# Модуль shutil содержит набор функций высокого уровня для 
# обработки файлов,
# групп файлов, и папок. В частности, доступные здесь функции 
# позволяют # копировать, перемещать и удалять файлы и папки. 
# Часто используется вместе с # модулем os.

# Для того, чтобы начать работать с данным модулем необходимо 
# его импортировать
# в свою программу:

# import shutil
# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое 
# (но не метаданные) файла src в файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src 
# в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все 
# поддиректории; path должен указывать на директорию, а не 
# на символическую ссылку.