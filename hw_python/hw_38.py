# Python Fundamentals 2025: Домашнее задание 38
# 1. Банковский счёт
# Создайте класс BankAccount, описывающий банковский счёт.
# Объект должен хранить имя владельца и текущий баланс.
from threading import active_count

# Реализуйте методы:
# пополнение счёта
# снятие средств
# отображение баланса

# При попытке снять больше, чем есть на счёте, операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
# Пример вывода:
# Current balance: 150
# Error: Amount must be positive.
# Current balance: 150
# Error: Not enough funds.
# Current balance: 150
#_________________
# 2.История операций
# Доработайте класс BankAccount.
# Каждая операция пополнения и снятия должна сохраняться в историю
# История должна быть доступна через property history только для чтения.
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).
# Пример вывода:
# Current balance: 50
# Operation history:
# Deposit: 150
# Withdraw: 100


# class BankAccount:
#     def __init__(self, balance, owner):
#         self._owner = owner
#         self.__balance = balance
#         # создаю хранилище для истории и только для чтения
#         self.__history = []
#     # отображение баланса
#     def display_balance(self):
#         print(f"Current balance: {self.__balance}")
#     # пополнение депозита
#     def add_to_balance(self, amount):
#         if amount > 0:
#             self.__balance = amount + self.__balance
#             # добавляю в историю
#             self.__history.append(f'Deposit: {amount}')
#         else:
#             print("Error: Amount must be positive.")
#     # снятие наличных
#     def withdraw_cash(self, amount):
#         if amount <= 0:
#             print("Error: Amount must be positive.")
#         else:
#             if amount <= self.__balance:
#                 self.__balance = self.__balance - amount
#                 self.__history.append(f'Withdraw: {amount}')
#             else:
#                 print('Error: Not enough funds.')
#     @property
#     def history(self):
#         return self.__history
#
# # Создаю счет с балансом
# account = BankAccount(150, 'Lorenzo')
# # Выполняю проверку
# account.display_balance()
# account.withdraw_cash(-60)
# account.display_balance()
# account.withdraw_cash(200)
# account.add_to_balance(100)
# account.withdraw_cash(50)
# print("Operation history:")
# for operation in account.history:
#     print(operation)

