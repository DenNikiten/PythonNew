# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# num = int(input("Input a number: "))
# i = 0
# while 2 ** i <= num:
#     print(2 ** i, end=" ")
#     i += 1
# # 1 2 4

# print("Denis", "Hello", "Al", sep=", ")
# # Denis, Hello, Al

        #_________ Урок 3. Списки и словари_______
    
    #____ Списки____
#  можно хранить несколько типов данных. 
# Работает дольше массива, т.к. разные данные

        # Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# numList = [1, 1, 2, 0, -1, 3, 4, 4]
# numList = set(numList)
# print(len(numList))
# # {0, 1, 2, 3, 4, -1}
# # 6

# # n = input().split()
# # # 6 15 78 98
# # print(n)
# # # ['6', '15', '78', '98'] 

# n = [int(i) for i in input().split()]
# # 1 1 5 5 3 3 3
# n = set(n)
# # {1, 3, 5} - числа в списке
# print(len(n))
# # 3


        # Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3

# list_1 = [int(i) for i in input().split()]
# step = int(input("Input a number of steps: ")) # сдвиг
# result_list = [list_1[i - step] for i in range(len(list_1))]
# print(result_list)
# # or
# list_1 = [int(i) for i in input().split()]
# step = int(input("Input a number of steps: ")) # сдвиг
# step = step % len(list_1)
# result_list = list()
# for i in range(len(list_1)):
#     result_list.append(list_1[i - step])
# print(result_list)

    # Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_1 = [1, 2, 3, -1.457, "Hello"]
print(list_1[3])

#  key: value
age = [{'Anna': 35, 'Andr': 33}, {'Ivan': 55}]
print(age[1]['Ivan'])

example = {"V": {"V": 54}} # вложенный словарь 
# не может быть {"V": 55, "V": 54}
print(example["V"]["V"])
# json


dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
          {"VIII": "S007"}]
values = set()
for item in dict_1:
    values.add(list(item.values())[0]) # [0] берем каждое значение
print(values)
# {'S001', 'S005', 'S007', 'S009', 'S002'}

dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
          {"VIII": "S007"}]
values = set()
for item in dict_1:
    for key in item:
        values.add(item[key])
print(values)
# {'S002', 'S007', 'S009', 'S001', 'S005'}

    # Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_1 = [int(i) for i in input("Input a numbers: ").split()]
print(list_1)
count = 0
for i in range(len(list_1) - 1):
    if list_1[i+1] > list_1[i]:
        count += 1
print(count)




 
