    # Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать 
# программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из одного слова, если во 
# фразе несколько слов, то они разделяются дефисами. Фразы 
# отделяются друг от друга пробелами. Стихотворение Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

poem = input("Input the phrases of the poem: ").lower().split()

poem_phrase = []
list_1 = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
for i in range(len(poem)):
    count = 0
    for j in list(poem[i]):       
        if j in list_1:
            count += 1            
    poem_phrase.append(count)

if len(set(poem_phrase)) == 1 and 0 not in set(poem_phrase):
        print("Парам пам-пам")
else:
    print("Пам парам")

# Задача 36: 
# Напишите функцию 
# print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы 
# num_rows и num_columns указывают число строк и столбцов 
# таблицы, которые должны быть распечатаны. Нумерация строк и 
# столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции 
# умножения.
# Ввод: print_operation_table(lambda x, y: x * y) 

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):        
        for j in range(1, num_columns+1):            
            print(operation(i, j), end="  ")
        print()

print_operation_table(lambda x, y: x * y)