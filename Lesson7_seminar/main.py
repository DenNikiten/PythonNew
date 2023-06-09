# a, b = map(int, input().split()) # 15 20
# print(a + b) # 35

# Задача №47. 
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

transformation = lambda x: x

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
print(transformed_values)
if values == transformed_values:
    print('ok')
else:
    print('fail')
# [1, 23, 42, 'asdfg']
# ok

    # Задача №49. 
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

def find_farthest_orbit(orbits):
    list_of_elliptical_orbits = [i for i in orbits if i[0] != i[1]]
    list_of_areas = [i[0] * i[1] for i in list_of_elliptical_orbits]
    # max_area_index = list_of_areas.index(max(list_of_areas))
    # return list_of_elliptical_orbits[max_area_index]
    max_area_index = [i for i in range(len(list_of_areas)) if list_of_areas[i] == max(list_of_areas)]
    return list_of_elliptical_orbits[max_area_index[0]]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))

# Задача №51. 
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0
    # return sum(list(map(characteristic, objects))) == 0

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):  # если True
    print('same')
else:
    print('different')



# data = list(map(int, input().split()))
# # одинаковые
# data = [int(i) for i in input().split()]