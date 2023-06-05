    # Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

list_1 = []
a1 = int(input("Input a first elemet: "))
d = int(input("Input a difference of the elemets: "))
n = int(input("Input a number of elements: "))
for i in range(1, n+1):    
    an = a1 + (i-1) * d
    list_1.append(an)
print(list_1)

    # Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

list_1 = [int(i) for i in input("Input a array elements: ").split()]
list_2 = []
min_value = int(input("Input a min value: "))
max_value = int(input("Input a max value: "))
for i in range(len(list_1)):
    if min_value <= list_1[i] <= max_value:
        list_2.append(i)
print(list_2)