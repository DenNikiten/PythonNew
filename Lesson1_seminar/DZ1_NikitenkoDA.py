    # Задача 2: 
# Найдите сумму цифр трехзначного числа. 

num = int(input("Input a three-digit number: "))

sum = num % 10 + num // 10 % 10 + num // 100

print(f"The sum of the digits of a three-digit number is {sum}")

    # Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int(input("Input the total numbers of cranes: "))

if S % 6 == 0:
    print(f"Petya made {S // 6} cranes")
    print(f"Katya made {S // 6 * 4} cranes")
    print(f"Seryozha made {S // 6} cranes")
else:
    print(f"Petya made {round(S / 6, 2)} cranes")
    print(f"Katya made {round(S / 6 * 4, 2)} cranes")
    print(f"Seryozha made {round(S / 6, 2)} cranes")

    # Задача 6: 
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

num = int(input("Input a six-digit number: "))

num1 = num // 1000
num2 = num % 1000

sum1 = num1 % 10 + num1 // 10 % 10 + num1 // 100
sum2 = num2 % 10 + num2 // 10 % 10 + num2 // 100

if sum1 == sum2:
    print("Congratulate. Lucky ticket!")
else:
    print("This is not lucky ticket! Be strong!")

    # Задача 8: 
# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Input the size n: "))
m = int(input("Input the size m: "))
k = int(input("Input the size k: "))

if k < n * m and (k % n == 0 or k % m == 0):
    print(f"You can break off {k} slices from a chocolate bar of size {n} * {m}")
else:
    print(f"You cannot break off {k} slices from a chocolate bar of size {n} * {m}")

