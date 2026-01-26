# Python Fundamentals 2025: Домашнее задание 25
from typing import Union

# 1. Деление без ошибок
# Напишите функцию, которая выполняет деление двух чисел, введенных пользователем,
# и обрабатывает возможные ошибки.
# Пример вывода:
# Введите делимое: 345
# Введите делитель: 5a
# Ошибка: Введено некорректное число.
from typing import Union

# def division_of_two_numbers(divident: float, divider: float) -> float:
#     """
#      Функция, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
#
#     :param divident, divider: целое или вещественное число
#     :return: возвращает частное двух чисел в виде вещественного числа
#     """
#     if divider == 0:
#         raise ZeroDivisionError("Делить на ноль нельзя.")
#     return divident / divider
#
# while True:
#     try:
#         divident =  float(input("Введите делимое: "))
#         divider = float(input("Введите делитель: "))
#         result = division_of_two_numbers(divident, divider)
#         print(f"Результат деления: {result}")
#         break
#     except ValueError:
#         print("Ошибка: Введено некорректное число.")
#     except ZeroDivisionError as e:
#         print(f"Ошибка: {e}. Попробуйте еще раз.")


# 2. Логирование ошибок
# Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
# Пример вывода:
# 2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

# import logging
#
# def division_of_two_numbers(divident: float, divider: float) -> float:
#     """
#      Функция, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
#
#     :param divident, divider: целое или вещественное число
#     :return: возвращает частное двух чисел в виде вещественного числа
#     """
#
#     logging.basicConfig(
#         filename="log.txt",
#         format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
#         level=logging.DEBUG,
#         encoding = 'utf-8'
#     )
#
#     if divider == 0:
#         raise ZeroDivisionError("Делить на ноль нельзя.")
#     return divident / divider
#
# while True:
#     try:
#         divident =  float(input("Введите делимое: "))
#         divider = float(input("Введите делитель: "))
#         result = division_of_two_numbers(divident, divider)
#         print(f"Результат деления: {result}")
#         break
#     except ValueError:
#         logging.error("Ошибка: Введено некорректное число.")
#         print("Ошибка: Введено некорректное число.")
#     except ZeroDivisionError as e:
#         logging.error(f"Ошибка: {e}. Попробуйте еще раз.")
#         print(f"Ошибка: {e}. Попробуйте еще раз.")