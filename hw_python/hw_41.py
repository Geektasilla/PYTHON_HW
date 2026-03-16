# Python Fundamentals 2025: Домашнее задание 41
# 1. Список всех стран
# Используя базу данных world, выведи названия всех стран из таблицы country.
# Каждое название должно отображаться с новой строки и иметь номер.
# Пример вывода:
# 1. Aruba
# 2. Afghanistan
# 3. Angola
# ...
# 239. Zimbabwe

# import pymysql
#
# config = {
#     'host': 'ich-db.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'world'
# }
#
# with pymysql.connect(**config) as connection:
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT Name FROM country")
#         countries = cursor.fetchall()
#         # print(countries)
#         for c, country in enumerate(countries, 1):
#             print(f"{c}. {country[0]}")


# _________________________
# 2. Города выбранной страны
# Добавьте к предыдущей программе возможность выбора страны.
# Пользователь должен ввести название страны.
# Далее выведите все города этой страны и их
# численность населения.
# Пример вывода:
# Введите страну: Germany
# Berlin — 3386667
# Hamburg — 1704735
# Munich [München] — 1194560
# ...

# import pymysql
#
# config = {
#     'host': 'ich-db.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'world'
# }
#
# with pymysql.connect(**config) as connection:
#     with connection.cursor() as cursor:
#         country = input("Введите страну: ")
#
#         cursor.execute("""
#             SELECT city.Name, city.Population
#             FROM city
#             JOIN country
#             ON country.Code = city.CountryCode
#             WHERE country.Name = %s
#             """,(country,))
#
#         countries = cursor.fetchall()
#         if len(countries) == 0:
#             print("Error: value not found")
#         else:
#             for name, Population in countries:
#                 print(f"{name} - {Population}")