# Python Fundamentals 2025: Домашнее задание 39
# 1. Фигуры и площади
# Создайте абстрактный класс Shape.
# В классе должен быть метод area(), который возвращает площадь фигуры.
# Реализуйте два класса:
# Circle, который принимает радиус.
# Rectangle, который принимает ширину и высоту.
# Пример использования
# shapes = [Circle(3), Rectangle(4, 5)]
# for shape in shapes:
#     print(f"Area: {shape.area():.2f}")

# 2.Проверка размеров фигур
# Доработайте фигуры:
# Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
# Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.

# from abc import ABC, abstractmethod
# import math
#
#
# class InvalidSizeError(Exception):
#     """An exception thrown when attempting to create a shape with a negative or zero size."""
#     pass
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         if radius <= 0:
#             raise InvalidSizeError('Values must be greater than zero.')
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         if width <= 0 or height <= 0:
#             raise InvalidSizeError('Values must be greater than zero.')
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# # Первая отладка
# # shapes = [Circle(3), Rectangle(4, 5)]
# # for shape in shapes:
# #     print(f"Area: {shape.area():.2f}")
#

# # Вторая отладка
# rad = [3, -5, 10, 0, 7]
# for r in rad:
#     try:
#         c = Circle(r)
#         print(f"Circle with radius: {r}. Area: {c.area():.2f}")
#     except InvalidSizeError as e:
#         print(f"Radius {r} not suitable: {e}")














