    # Урок 3. Функции, рекурсия, алгоритмы

def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    # print(summa)
    return summa # завершает работу функции
    # print("Stop")

a = sum_numbers(5)
print(a)

# ______________
def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    # print(summa)
    return summa # завершает работу функции
    # print("Stop")

a = sum_numbers(5)
print(a)
# Hello
# 15

# ______________
def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    # print(summa)
    return summa # завершает работу функции
    # print("Stop")

a = sum_numbers(5, 'gsfagf')
print(a)
# gsfagf
# 15

# ___________________________________
def sum_str(*args): # * все аргументы
    res = ""
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
# qel
# print(sum_str(1, 8, 9)) - нельзя

# _______________________________
import modul1

print(modul1.max1(5, 9))
# 9

# ______________
from modul1 import max1
print(max1(10, 9))
# 10

# _______________
from modul1 import *
print(max1(12, 1))
# 12

# _____________
import modul1 as m1

print(m1.max1(3, 15))
# 15

# ______________
    # Рекурсия____________________________

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# __________________ Быстрая сортировка_________
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,1,7,9,6,8,15,25]))
# [1, 5, 6, 7, 8, 9, 14, 15, 25]

# _______ Сортировка слиянием_____________
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

list1 = [1,5,6,32,9,45,3,7,98]
merge_sort(list1)
print(list1)
# [1, 5, 6, 32, 3, 9, 45, 7, 98]


