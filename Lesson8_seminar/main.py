# DZ7

# text = input("Input the phrases of the poem: ").lower().split()
# vowels = 'ауоыиэяюёе'
# result = set()
# for word in text:
#     count = 0
#     for i in word:
#         if i in vowels:
#             count += 1
#     result.add(count)

# if len(result) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#     for i in range(2, num_rows + 1):
#         print(i, end=' \t')        
#         for j in range(2, num_columns + 1):            
#             print(operation(i, j), end=' \t')
#         print()

# print_operation_table(lambda x, y: x * y)

# .split()- принимает строку и возвращает список 
# .join() - принимает список и возвращает строку

# or

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):        
#         for j in range(1, num_columns+1):            
#             print(operation(i, j), end=" \t")
#         print()

# print_operation_table(lambda x, y: x * y)


#_______Seminar_____________

# database = open('data.txt', 'r', encoding='utf-8')
# print(database.readlines())

# or

# with open('data.txt', 'r', encoding='utf-8') as database:
#     print(database.readlines())

# with open('data.txt', 'a', encoding='utf-8') as database:
#     database.write('\nРаф Рфа')

# with open('data.txt', 'w', encoding='utf-8') as database:
#     database.write('Ivan;Ivanov;799999999999\n')





