# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# n = int(input("Input a numbers of elements in the arrya: "))
# list_1 = [int(i) for i in input().split()]
# print(list_1)
# count = 0
# x = int(input("Input a number: "))
# for el in list_1:    
#     if el == x:
#         count += 1
# print(count)

# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# n = int(input("Input a numbers of elements in the arrya: "))
# array = [int(i) for i in input().split()]
# x = int(input("Input a number: "))
# print(array)
# count = x - array[0]
# numbers = array[0]
# if count < 0:
#     count *= (-1)
# for el in range(1, n):    
#     temp = x - array[el]
#     if temp < 0:
#         temp *= (-1)
#     if count > temp:
#         count = temp
#         numbers = array[el]
# print(numbers)
# or
# n = int(input("Input a numbers of elements in the arrya: "))
# array = [int(i) for i in input().split()]
# x = int(input("Input a number: "))
# print(array)
# count = abs(x - array[0])
# numbers = array[0]
# for el in range(1, n):    
#     temp = abs(x - array[el])    
#     if count > temp:
#         count = temp
#         numbers = array[el]
# print(numbers)


# Задача 20: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом 
# очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# values = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1, 
#            "D, G, Д, К, Л, М, П, У": 2, 
#            "B, C, M, P, Б, Г, Ё, Ь, Я": 3, 
#            "F, H, V, W, Y, Й, Ы": 4, 
#            "K, Ж, З, Х, Ц, Ч": 5, 
#            "J, X, Ш, Э, Ю": 8, 
#            "Q, Z, Ф, Щ, Ъ": 10, }

# word = input("Input a word: ").upper()
# result = 0
# for i in word:
#     for key in values:
#         if i in key:
#             result += values[key]
# print(result)


                    # Seminar4
    # Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# line = input("Input a line: ").split()
# result = {}
# for i in line:
#     if i in result:
#         print(f'{i}_{result[i]}', end=" ")
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1


      # Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним 
# пробелом. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# array = [str(i) for i in input().upper().split()]
# array1 = set(array)
# array = list(array1)
# count = 0
# for i in array:
#     count += 1
# print(count-1)
# or
# text = len(set(input("Input a text: ").upper().split()))
# print(text)

        # Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

n = int(input())
max_number = n # В1 - П1
while n != 0 or n > 0: # В1 - П2
      n = int(input())
      if max_number < n: # В2 - П2
            max_number = n # В2 - П3
print(max_number) # В2 - П4

