# Python Fundamentals 2025: Домашнее задание 29

# 1. Генератор Фибоначчи
# Создайте генератор, который генерирует последовательность Фибоначчи бесконечно,
# возвращая по одному числу за раз.
# Последовательность Фибоначчи — это ряд чисел, где каждое следующее число равно сумме двух предыдущих.
# Начинается с 0 и 1.
# Пример вывода:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# SOLUTION:
#VAR 1
# def generator_fibonacci():
#     """
#     Creates an infinite generator for the Fibonacci sequence.
#     :return: A generator that sequentially returns (yields) the Fibonacci numbers.
#     """
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# num_res = generator_fibonacci()
# for _ in range(10):
#     print(next(num_res))

# VAR 2 (for input with check)
# def generator_fibonacci(N):
#     """
#     Generates the first N numbers of the Fibonacci sequence.
#     :param N: The number of numbers to generate.
#     :return: A generator that yields the Fibonacci numbers.
#     """
#     a, b = 0, 1
#     for _ in range(N):
#         yield a
#         a, b = b, a + b
# while True:
#     try:
#         input_numbers = int(input("Enter the number of Fibonacci numbers: "))
#         break
#     except ValueError:
#         print("ValueError: please enter an integer.")
#
# num_res = generator_fibonacci(input_numbers)
# for num in num_res:
#     print(num)

#_________________________________________________________________________________________________________________________
# 2. Генератор уникальных элементов
# Создайте генератор, который принимает список элементов и выдаёт только уникальные значения,
# сохраняя порядок их появления в исходном списке.
# Данные:
# data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
# Пример вывода:
# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# SOLUTION:
#VAR 1
# def unique_generator(data):
#     unique_set = set()
#     for element in data:
#         if element not in unique_set:
#             unique_set.add(element)
#             yield element
#
# data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
# unique_gen = unique_generator(data)
# for element in unique_gen:
#     print(element)


#VAR 2
# def unique_generator(data):
#     unique_set = set()
#     for element in data:
#         # Check for uniqueness by both value and type
#         if (element, type(element)) not in unique_set:
#             unique_set.add((element, type(element)))
#             yield element
#
# #data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
# #data = [1, ")))", 1.0, "world", 1]
# #data = [1, ")))", 1.0, "world", 1, True]
# unique_gen = unique_generator(data)
# for element in unique_gen:
#     print(element)