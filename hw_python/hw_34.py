# Python Fundamentals 2025: Домашнее задание 34

# Класс Rectangle
# Создайте класс Rectangle, который описывает прямоугольник.
# У каждого объекта должны быть два поля: width и height.
# Добавьте метод get_area(), который возвращает площадь прямоугольника.
# Создайте объект прямоугольника с произвольными значениями.
# Выведите его площадь.
# Измените ширину и высоту.
# Выведите новую площадь.
# Пример вывода:
# Площадь: 20
# Новая площадь: 35


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#
# result = Rectangle(4,5)
# area = result.get_area()
# print("Area:", area)
# result.width = 5
# result.height = 7
# new_area = result.get_area()
# print("New area:", new_area)
#_______________________________________________________________________________________________
# 2.Класс Counter
# Реализуйте класс Counter, который представляет собой простой счётчик.
# Счётчик должен начинаться с нуля.
# Предусмотрите методы для увеличения и уменьшения значения на единицу,
# при этом при каждой операции должно отображаться новое значение счётчика.
# Добавьте метод, возвращающий текущий результат.
# Проверьте работу счётчика, выполнив несколько операций.
# Пример вывода:
# Значение увеличено, текущее: 1
# Значение увеличено, текущее: 2
# Значение увеличено, текущее: 3
# Значение уменьшено, текущее: 2
# Текущее значение: 2

# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1
#         print(f"Value increased, current: {self.value}")
#     def decrement(self):
#         self.value -= 1
#         print(f"Value reduced, current: {self.value}")
#     def get_current(self):
#         return self.value
#
#
# result = Counter()
# result.increment()
# result.increment()
# result.increment()
# result.decrement()
# print("Current value:", result.get_current())









