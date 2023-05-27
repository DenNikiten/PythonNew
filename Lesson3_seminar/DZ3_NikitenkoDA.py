    # Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input("Input a numbers of elements in the arrya: "))
list_1 = [int(i) for i in range(1, n+1)]
print(list_1)
count = 0
x = int(input("Input a number: "))
for i in range(len(list_1)):    
    if list_1[i] == x:
        count += 1
print(count)

    # Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input("Input a numbers of elements in the arrya: "))
list_1 = [int(i) for i in range(1, n+1)]
print(list_1)
x = int(input("Input a number: "))
flag = True
while flag:
    if x < list_1[0]:
        print(f"The closest element to a given number of {x} is {list_1[0]}")
        flag = False
    elif x == list_1[0]:
        print(f"The closest element to a given number of {x} is {list_1[1]}")
        flag = False
    elif x > list_1[n-1]:
        print(f"The closest element to a given number of {x} is {list_1[n-1]}")
        flag = False
    elif x == list_1[n-1]:
        print(f"The closest element to a given number of {x} is {list_1[n-2]}")
        flag = False
    for i in range(len(list_1)): 
        if flag == True:    
            if x == list_1[i]:    
                print(f"The closest element to a given number of {x} is {list_1[i-1]} and {list_1[i+1]}")
                flag = False    

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

# Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова. # Будем считать, что на вход подается 
# только одно слово, которое содержит либо только
# английские, либо только русские буквы.

scrabble = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, 
           "N": 1, "S": 1, "T": 1, "R": 1, "D": 2, "G": 2,
           "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4,
           "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8,
           "Q": 10, "Z": 10, "А": 1, "В": 1, "Е": 1, "И": 1,
           "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1, "Д": 2,
           "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2, "Б": 3,
            "Г": 3, "Ё": 3, "Ь": 3, "Я": 3, "Й": 4, "Ы": 4, 
            "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, 
            "Э": 8, "Ю": 8, "Ф": 10, "Щ": 10, "Ъ": 10}

list_1 = list((str(input("Input a Russian or English word: "))).upper())
cost_word = 0
for i in range(len(list_1)):    
    cost_word += scrabble[list_1[i]]    
print(cost_word)


