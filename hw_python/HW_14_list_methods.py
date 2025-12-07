# 1.Число в конце
# Напишите программу, которая создает новый список.
# В него необходимо добавить только те строки из исходного списка,
# в которых цифры находятся только в конце.
# Данные:
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# Пример вывода:
# # Строки с цифрами только в конце: ['apple23', 'grape3']
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]


# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# new_strings = []
# for s in strings:
#     left = s.rstrip("0123456789")
#     tail = s[len(left):]
#
#     if left.isalpha() and tail.isdigit():
#         new_strings.append(s)
# print(f'Строки с цифрами только в конце: {new_strings}')

#___________________
# 2.Удаление кратных
# Напишите программу, которая удаляет из списка все значения,
# кратные числу, которое вводится пользователем.
# Данные:
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# Пример вывода:
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]

# Var 1
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# input_num = int(input("Введите число для удаления кратных ему элементов: "))
# for num in numbers[::-1]:
#     if num % input_num == 0:
#         numbers.remove(num)
# print(f'Список без кратных значений: {numbers}')

# VAR 2
# List comprehension
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# input_num = int(input("Введите число для удаления кратных ему элементов: "))
# new_list = [num for num in numbers if num % input_num != 0]
# print(f'Список без кратных значений: {new_list}')

#_________________
# 3.Порядок четных
# Напишите программу, которая формирует новый список чисел.
# Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Данные:
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]

#numbers = [5, 2, 3, 8, 4, 1, 2, 7]
##numbers = list(map(int, input().split()))# 52384127 # 2 вариант ввода
# collect = []
# for c in numbers:
#     if c % 2 == 0:
#         collect.append(c)
#
# collect.sort(reverse=True)
#
# st = 0
# new_num = []
# for n in numbers:
#     new_num.append(collect.pop(0) if n % 2 == 0 else n)
# print(new_num)
#

# print(*new_num, sep=",")
## print(",".join(map(str, new_num))) 2 вариант вывода ко второму варианту ввода








