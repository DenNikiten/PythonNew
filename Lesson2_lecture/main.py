
    #____________ Списки_______________

list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 4]
print(list_1)
# [1, 2, 3, 4]

print(*list_1) # * - убираем скобочки, будет перечисление значений
# 1 2 3 4

for i in list_1:
    print(i)
# 1
# 2
# 3
# 4

print(len(list_1))
# 4

print(list_1[0])
# 1

list_1 = [1, 2, 6, 8]
print(list_1[-1])
# 8
# list_1[-2] - 6

list_1 = [1, 5]
print(list_1)
# [1, 5]
list_1.append(8)
print(list_1)
# [1, 5, 8]
list_1.append(85)
print(list_1)
# [1, 5, 8, 85]

list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)
# []
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]

    # Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]
# pop удаляет и возвращает удаленный элемент

    # Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]

    # Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
list_1.insert(2, 11) # 
print(list_1) # [12, 7, 11, -1, 21, 0]

# 10:20

    # Срез списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]

    #____________ Кортежи_______________

t = ()

print(type(t))
# <class 'tuple'>

t = (1)
print(type(t))
# <class 'int'>

t = (1, ) # (1, 2, 3,) - запятая
print(type(t))
# <class 'tuple'>

v = [1, 8, 9]
print(v)
# [1, 8, 9]
print(type(v))
# <class 'list'>

v = tuple(v) # convert in courtage
print(v)
# (1, 8, 9)
print(type(v))

# v = list(v) # convert in list
# print(v)
# # [1, 8, 9]

# a, b = 1, 2
# a = b = 1

a,b,c = v
print(a, b, c)
# 1 8 9 - независимые переменные

    # Отличие кортежа от списка
t = (1, 2, 3, 5,)
print(t[1])

for i in t:
    print(i)
# or
for i in range(len(t)):
    print(t[i])

# t[0] = 2
# # TypeError: 'tuple' object does not support item assignment

# в кортеже мы не можем изменять элементы

        #___________ Словари______________
d = {}
d = dict()

d['q'] = 'qwerty'
print(d)
# {'q': 'qwerty'}

d['w'] = 'werty'
print(d)
# {'q': 'qwerty', 'w': 'werty'}

print(d['q'])
# qwerty

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'
print(dictionary['left']) # ←
print(dictionary['up'])
dictionary['left'] = '⇐' # ⇐
print(dictionary['left'])
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

dictionary[895] = 9445
print(dictionary)
# {'up': '↑', 'down': '↓', 'right': '→', 895: 9445}
# можем списки использовать списки, словари, множества

print(dictionary.items())
# dict_items([('up', '↑'), ('down', '↓'), ('right', '→'), (895, 9445)])

for (k,v) in dictionary.items():
    print(k, v)
# up ↑
# down ↓
# right →
# 895 9445

        #___________ Множества___________
# хранятся только уникальные значения 
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'blue', 'green'}
colors.add('red')
print(colors) # {'red', 'blue', 'green'}
colors.add('gray')
print(colors) # {'gray', 'red', 'blue', 'green'}
colors.remove('red')
print(colors) # {'green', 'gray', 'blue'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # проверяет есть ли значение, есть - удаляет
#  нет - пропускает
print(colors)
colors.clear() # set() - пустое множество
print(colors)

v = set()
print(type(v))
# <class 'set'>
print(type(colors))
# <class 'set'>

    # Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5} - пересечение 
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

    # Неизменяемое или замороженное множество(frozenset) 
# — множество, с которым 
# # не будут работать методы удаления и добавления.

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)
# frozenset({1, 2, 3, 5, 8})

    #_____ List Comprehension_________________
# «генератора списка»

# List comprehension — это упрощенный подход к созданию списка, 
# который задействует цикл for, а также инструкции if-else 
# для определения того, что в итоге окажется в финальном списке.

# # Простая ситуация — список:
# list_1 = [exp for item in iterable]

# # Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

    #___ Задача: Создать список, состоящий из четных чисел_______
# в диапазоне от 1 до 100.

# 1. 
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)

# List comprehension
list_1 = [i for i in range(1, 101)]
print(list_1)

# 2. Добавить условие (только чётные числа)

list_1 = [i for i in range(1, 101) if i % 2 == 0]
print(list_1)

#  решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. 
# Например, умножить значение на 2.

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)
# [0, 4, 8, 12, 16]

  #_________ Профилирование и отладка__________________
# Самые распространенные ошибки:

    # SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
#     if number_first > number_second # !!!!!
# print(number_first)
# # Отсутствие :

    # IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов

    # TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

    # ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

    # KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

    # NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует

    # ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения
# text = '555'
# print(int(text))
# можно перевести