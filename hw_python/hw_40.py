# 1. Электронное письмо
# Реализуйте класс Email, который представляет электронное письмо.
# Каждое письмо должно содержать:
# sender — адрес отправителя
# recipient — адрес получателя
# subject — тема письма
# body — текст письма
# date — дата отправки
# Класс должен поддерживать:
# Сравнение писем по дате
# Преобразование письма в строку
# Получение длины текста письма
# Проверку на наличие текста в письме или не состоит ли текст только из пробелов
from operator import ifloordiv

from prompt_toolkit.contrib.telnet import TelnetServer


# Пример использования:
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)

# Пример вывода:
# From: alice@example.com
# To: bob@example.com
# Subject: Meeting
# - Let's meet at 10am -
# From: bob@example.com
# From: bob@example.com
# To: alice@example.com
# Subject: Report
# -  -
# Length: 18
# Length: 18
# Has text: True
# Is newer: True

# from datetime import  datetime
#
# class Email:
#     """
#     Класс для представления электронного письма.
#     """
#     def __init__(self, sender, recipient, subject, body, date):
#         """
#         Инициализирует объект Email.
#
#         :param sender: Адрес отправителя.
#         :param recipient: Адрес получателя.
#         :param subject: Тема письма.
#         :param body: Текст письма.
#         :param date: Дата отправки (объект datetime).
#         """
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body
#         self.date = date
#
#     def __str__(self):
#         """
#         Возвращает строковое представление письма.
#         """
#         return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n- {self.body} -"
#
#     def __len__(self):
#         """
#         Возвращает длинну текста письма.
#         """
#         return len(self.body)
#
#     def __bool__(self):
#         """
#         Проверяете, содержит ли письмо текст ( не пустое и не только пробелы)
#         :return:
#         """
#         return bool(self.body and not self.body.isspace())
#
#     def __lt__(self, other):
#         """
#         :param other: Объект для сравнения (ожидается экземпляр Email).
#         :return: True, если дата текущего письма раньше, иначе False.
#         Возвращает NotImplemented, если типы несовместимы.
#         """
#         if isinstance(other, Email):
#             return self.date < other.date
#         return NotImplemented
#
#     def __gt__(self, other):
#         """
#         Сравнивает текущее письмо с другим по дате (оператор >).
#         :param other: Объект для сравнения.
#         :return: True, если дата текущего письма позже, иначе False.
#         """
#         if isinstance(other, Email):
#             return self.date > other.date
#         return NotImplemented
#
#
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e2)
# print("Length_e1:", len(e1))
# print("Length_e2:", len(e2))
# print("Has text_e1:", bool(e1))
# print("Has text_e2:", bool(e2))
# print("Is newer:", e2 > e1)
#_______________________________
# 2. Класс для работы с деньгами
# Создайте класс Money, в котором можно:
# складывать и вычитать объекты через операторы + и -
# выводить объект как строку в виде "$<amount>"
# при сложении и вычитании возвращается новый объект
# если вычитание приводит к отрицательному значению — вернуть 0
# Пример использования:
# money1 = Money(100)
# money2 = Money(50)
# print(money1 + money2)
# print(money1 + money2)
# print(money1 - money2)
# print(money2 - money1)
# Пример вывода:
# $150
# $50
# $0

# # Создайте класс Money
# class Money:
#     """
#     Класс для работы с деньгами.
#     """
#     def __init__(self, amount):
#         """
#         Инициализирует обьект Money.
#         :param amount: Сумма денег.
#         """
#         self.amount = amount
#
#     # выводить объект как строку в виде "$<amount>"
#     def __str__(self):
#         """
#         Возвращает строковое представление суммы в формате "$<amount>".
#         """
#         return f"${self.amount}"
#
#     # при сложении возвращается новый объект
#     def __add__(self, other):
#         """
#         Складывает две денежные суммы
#         :param other:
#         :return: Возвращает новый обьект Money.
#         """
#         if isinstance(other, Money):
#             return Money(self.amount + other.amount)
#         return NotImplemented
#     # при вычитании возвращается новый объект
#
#     def __sub__(self, other):
#         """
#         Вычитает одну денежную сумму из другой.
#         Если результат отрицательный, возвращает Money(0).
#         Возвращает новый объект Money.
#         """
#         if isinstance(other, Money):
#             result = self.amount - other.amount
#             return Money(result if result >= 0 else 0)
#         return NotImplemented
#
# money1 = Money(100)
# money2 = Money(50)
# print(money1 + money2)
# print(money1 - money2)
# print(money2 - money1)

