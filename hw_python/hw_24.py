# Python Fundamentals 2025: Домашнее задание 24
# 1. Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
# Данные:
# (num) = 43197
# Пример вывода: 24
# отделяю последнюю цифру (N % 10) и прибавляю её к сумме цифр оставшегося числа (N // 10).
#
# def founded_sum_all_numbers_in_num(num: int)->int:
#     """
#     Рекурсивно находит сумму всех цифр числа.
#     :param num: целые числа.
#     :return: Сумма всех чисел в виде целого числа.
#     """
#     if num == 0:
#         return 0
#     return num % 10 + founded_sum_all_numbers_in_num(num // 10)
#
#
# print(founded_sum_all_numbers_in_num(43197))
from typing import Union


# 2.Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
# Данные:
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# Пример вывода:28

# from typing import List, Union
# def founded_sum_nested_numbers(data:list[Union[int,list]])->int:
#     """
#     рекурсивно суммирует все числа во вложенных списках.
#     :param data: список который может содержать целые числа и другие вложенные списки с целыми числами.
#     :return: Сумма всех чисел во вложенных списках в виде целого числа.
#     """
#     total = 0
#     for item in data:
#         if isinstance(item, List):
#             total += founded_sum_nested_numbers(item)
#         else:
#             total += item
#     return total

# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# nested_numbers = [0, [0, 0], [0, [0, 0]], 0]
# nested_numbers = [5]
# nested_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nested_numbers = [[[[[[55]]]]]]
# nested_numbers = [-1, [-2, -3], [-4, [-5, -6]], -7]
# result = founded_sum_nested_numbers(nested_numbers)
# print(result)


