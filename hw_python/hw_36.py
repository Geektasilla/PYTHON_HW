# Домашнее задание
# 1. Класс Person
# Создайте класс Person, представляющий человека.
# ● Каждый человек должен иметь имя.
# ● Добавьте метод introduce(), который выводит приветствие с именем.
# Пример вывода:
# Hello, my name is Alice.
from idlelib.configdialog import VarTrace

#Var 1
# class Person:
#     @staticmethod #  сначала ставлю инспектора по проверке валидности данных))))
#     def validate_name(name):
#         if not name.strip(): #  если после удаления всех пробелов ничего не осталось
#             raise ValueError('Поле не может быть пустым. Необходимо указать имя')
#
#     def __init__(self, name):
#         self.validate_name(name)
#         self.name = name
#
#     def introduce(self):
#         print(f'Hello, my name is {self.name}')
#
# person1 = Person('Bob')
# person1.introduce()
# person2 = Person('Tom_124') # так как сейчас могут быть в имени и цифры как у детей Илона Маска например или никнейм если такимх имен много
# person2.introduce()
# person3 = Person('Viktoriia-Mariella')
# person3.introduce()
# try:
#     person4 = Person('')
#     person4.introduce()
# except ValueError as e:
#     print(f'Ошибка: {e}')

#Var 2 ( если подумать и упростить)
# class Person:
#     def __init__(self, name):
#         if not name.strip():  # если после удаления всех пробелов ничего не осталось
#             raise ValueError('Поле не может быть пустым. Необходимо указать имя')
#         self.name = name
#
#     def introduce(self):
#         print(f'Hello, my name is {self.name}')
#
# person1 = Person('Bob')
# person1.introduce()
# person2 = Person('Tom_124') # так как сейчас могут быть в имени и цифры как у детей Илона Маска например или никнейм если такимх имен много
# person2.introduce()
# person3 = Person('Viktoriia-Mariella')
# person3.introduce()
# try:
#     person4 = Person('')
#     person4.introduce()
# except ValueError as e:
#     print(f'Ошибка: {e}')
# ________________
# 2. Класс Student
# На основе класса Person создайте класс Student.
# ● Студент должен иметь имя и номер курса.
# ● Метод introduce() должен сначала выводить базовое приветствие, а затем
# строку: I'm on course <номер_курса>.
# Пример вывода:
# Hello, my name is Alice.
# I'm on course 2.

# class Person:
#     def __init__(self, name):
#         if not name.strip():  # если после удаления всех пробелов ничего не осталось
#             raise ValueError('Поле не может быть пустым. Необходимо указать имя')
#         if len(name) < 2:
#             raise ValueError("Недопустимый размер имени")
#         self.name = name
#
#     def introduce(self):
#         return f'Hello, my name is {self.name}'
#
# class Student(Person):
#     def __init__(self, name, course_number):
#         super().__init__(name)
#         self.course_number = course_number
#         self.validate_student()
#
#     def validate_student(self):
#         if not isinstance(self.course_number, int) or self.course_number <= 0:
#             raise ValueError('Курс должен быть целым положительным числом')
#
#     def introduce(self):
#         result = super().introduce()
#         return f"{result}\nI'm on course {self.course_number}."
#
#     @classmethod
#     def test_options(cls, name, course_number):
#         try:
#             object = cls(name, course_number)
#             return object.introduce()
#         except ValueError as e:
#             return f'Ошибка: {e}'
#
# print(Student.test_options('Bob',2))
# print(Student.test_options('Bob-Martin',22))
# print(Student.test_options('',0))
# print(Student.test_options('B',2222222222222222222222222222222222))
# print(Student.test_options('Bob124',5))
# print(Student.test_options('Alise',''))
# print(Student.test_options('',''))

# _______________________________
# 3. Класс Teacher и список людей
# На основе класса Person создайте класс Teacher.
# ● У преподавателя есть имя и предмет.
# ● Метод introduce() должен выводить имя и предмет.
# ● Метод introduce() должен выводить строку: Hello, I am professor <имя>.
# My subject is <предмет>.
# ● Создайте список, в котором будут Student и Teacher, и вызовите у всех метод
# introduce().
# Пример вывода:
# Hello, my name is Alice.
# I'm on course 2.
# Hello, I am professor Bob.
# My subject is Mathematics

# class Person:
#     def __init__(self, name):
#         if not name.strip():  # если после удаления всех пробелов ничего не осталось
#             raise ValueError('Поле не может быть пустым. Необходимо указать имя')
#         if len(name) < 2:
#             raise ValueError("Недопустимый размер имени")
#         self.name = name
#
#     def introduce(self):
#         return f'Hello, my name is {self.name}'
#
# class Student(Person):
#     def __init__(self, name, course_number):
#         super().__init__(name)
#         self.course_number = course_number
#         self.validate_student()
#
#     def validate_student(self):
#         if not isinstance(self.course_number, int) or self.course_number <= 0:
#             raise ValueError('Курс должен быть целым положительным числом')
#
#     def introduce(self):
#         result = super().introduce()
#         return f"{result}\nI'm on course {self.course_number}."
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         if not subject.strip() or len(subject) < 3:
#             raise ValueError('Название предмета слишком короткое или отсутствует')
#         self.subject = subject
#
#     def introduce(self):
#         return f"Hello, I am professor {self.name}.\nMy subject is {self.subject}."
#
#
# # ● Создайте список, в котором будут Student и Teacher, и вызовите у всех метод
# # introduce().
# uni_members = [
#     Student('Alise',1),
#     Teacher('Bob','Mathematics'),
#     Student('Jim',2),
#     Teacher('Lukas','German')
#     ]
#
# for members in uni_members:
#     print(members.introduce())








