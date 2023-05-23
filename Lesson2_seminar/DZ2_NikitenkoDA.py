    # Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input("Input a number of coins n: "))

tail = 0
head = 0
for i in range(n):
    num = int(input("Input a number of coin where 0-tail and 1-head: "))
    while num != 0 and num != 1:
        num = int(input("Wrong! Input a number of coin 0 or 1: "))
    if num == 0:
        tail += 1
    else:
        head += 1

if tail > head:
    print(f"{head} head coins to be turned over to get {n} tails coins")
elif tail < head:
    print(f"{tail} tail coins to be turned over to get {n} heads coins")
else:
    print("The number of coins are equal")

    # Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("Input the sum of two numbers X and Y: "))
P = int(input("Input the product of two numbers X and Y: "))

discriminant = (-S) ** 2 - 4 * P

X = (S + discriminant**0.5) / 2
Y = S - X

print(f"The sum of {S} and the product of {P} are numbers {int(X)} and {int(Y)}")

    # Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

num = int(input("Input a number: "))

i = 0
res = ""
flag = True
while flag:
    x = 2 ** i
    if x > num: 
        flag = False
    else:
        res = res + str(x) + " "
        i += 1
print(res)


