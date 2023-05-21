# создаем виртуальное окружение
# python -m venv .папка

# запускаем ctrl F5, либо run

a = 3
print(a, 8, 6)

a = 1.89
print(a, 8, 6)

n = "adssd"
n1 = 'dgfs'
print(n, n1)

n = 5
print(type(n))
# тип

n = 'fr\'fg'
print(n)
# fr'fg

n = 'fr"jhgsjh"fg'
print(n)
# fr"jhgsjh"fg

print(5, 1)
print(5, 5)
print(5, 3)
""" комментирование
print(5, 1)
print(5, 5)
print(5, 3)
"""

a = 5
b = 5.89
c = "hello"
print(a, ' - ', b, ' - ', c)
# 5  -  5.89  -  hello

print(f"{a} - {b} - {c}")
# 5 - 5.89 - hello

print("{} - {} - {}".format(a,b,c))
# 5 - 5.89 - hello

# print("Input first string: ")
# a = input()
# print(a)

# b = input("Input first string: ")
# print(b)

# print("Input first string: ")
# a = input()
# b = input("Input first string: ")
# print(a, ' + ', b, ' = ', a + b)

# c = 5.59
# print(c)
# # 5.59
# print(type(c))

# n = int(c)
# print(type(n))
# print(n)
# # 5

# c = 5.59
# print(c)
# # 5.59
# print(type(c))
# c = str(c)
# print(type(c))
# print(c)
# print(c + "dsds")
# # 5.59dsds


# c = 1
# print(c)
# print(type(c))
# # <class 'int'>
# c = bool(c)
# print(c)
# print(type(c))
# # <class 'bool'>

# print("Input first string: ")
# a = int(input())
# b = int(input("Input first string: "))
# print(a, ' + ', b, ' = ', a + b)

# a = 5.89666
# b = 6.333
# print(round(a*b, 2)) 
# # 37.34
# # round(1.5689, 2)

# i++ C#

iter = 2
iter += 3
iter %= 5
iter **= 5
print(iter)

a = 1 < 4 and 5 > 2
print(a)
# True

a = 1 < 3 < 5 < 10 
print(a) 
# True

# if condition1 and condition2: 
#     # operator

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')

n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa) 
# 9

i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print("Пожалуй")
    print("хватит ")
print(i)
# break выводит из программы, дальше она не продолжается
# 3

# #  на замену break метод флажка flag = True
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7 9
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20

for i in range(5):
    print(i)

a = "qwerty"
print(a[2])
# e

for i in 'qwerty':
    print(i)
# q
# w
# e
# r
# t
# y

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

# Команды для работы со строками:

text = 'СъЕШЬ ещё этих МяГкИх французских булок'

print(len(text))
print(len(text))
# Определить количество символов в строке
# 39

print('ещё' in text) # True
print('этих' in text)

print(text.lower()) # съешь ещё этих мягких французских булок
print(text.lower())

print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.upper())

print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
print(text.replace('МяГкИх', 'СОЧНЫХ')) # СъЕШЬ ещё этих СОЧНЫХ французских булок 

#  Срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к // т.к. индексация с нуля, минус ставим 1
print(text[-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл // шаг 6
print(text[::6]) # сеикакл
print(text[2:9] + text[-5] + text[:2]) # ешь ещёбсъ