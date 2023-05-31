    # Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого 
# множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Input a number of elements in the first set: "))
set_of_values1 = set(int(i) for i in input("Input a elements: ").split())
m = int(input("Input a number of elements in the second set: "))
set_of_values2 = set(int(i) for i in input("Input a elements: ").split())
result = sorted(set_of_values1.union(set_of_values2))
print(result)

    # Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только 
# по окружности. Таким образом, у каждого куста есть ровно два 
# соседних. Всего на грядке растет N кустов.

# Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод – на i-ом 
# кусте выросло ai  ягод.

# В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один 
# заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. 

# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

bush = int(input("Input a numbers of bushes: "))
num_of_bush = [int(i) for i in range(1, bush+1)]

sum = 0
flag = True
while flag:
    bush_el = int(input("Input a number of bush element: "))
    if bush_el == 1:
        sum += num_of_bush[0] + num_of_bush[1] + num_of_bush[-1]
        flag = False
    elif bush_el == bush:
        sum += num_of_bush[len(num_of_bush)-1] + num_of_bush[len(num_of_bush)-2] + num_of_bush[0]
        flag = False    
    for i in range(len(num_of_bush)):
        if flag == True:
            if bush_el == num_of_bush[i-1]:
                sum += num_of_bush[i-1] + num_of_bush[i] + num_of_bush[i-2]
                flag = False
print(sum)