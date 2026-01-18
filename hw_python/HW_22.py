# Python Fundamentals 2025: Домашнее задание 22
#
# 1. Выбор заказов
# У вас есть список заказов.
# Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая: Отбирает заказы дороже 500.
# Создаёт список названий отобранных продуктов в алфавитном порядке.
# Возвращает итоговый список названий.
#
# Данные:
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
#
# Пример вывода: ['Chair', 'Laptop']
from itertools import product


# def order_selection(orders):
#     expensive_orders = [order["product"] for order in orders if order["price"] > 500]
#     return sorted(expensive_orders)
# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
# ]
# print(order_selection(orders))

#_______________________________________________________________________________________________________________________________________
# 2. Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
#
# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
#
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
# def total_sales_count(*args):
#     sales_keys = {}
#     res = {sal[0]: sal[1] * sal[2] for sal in sales if sal[0] not in sales_keys}
#     return res
#
# sales = [
#     ("Laptop", 5, 1200),
#     ("Mouse", 50, 20),
#     ("Keyboard", 30, 50),
#     ("Monitor", 10, 300),
#     ("Chair", 20, 800)
# ]
# sorted_sales = dict(sorted(total_sales_count(sales).items(), key=lambda x: x[1], reverse=True))
# print(sorted_sales)

#_______________________________________________________________________________________________________________________________________






