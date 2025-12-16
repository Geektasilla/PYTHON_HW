# 1. Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

# VAR 1
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# text_list = input().split(", ") # Hello, Python Programming, World, Advanced Topics, Simple
# for i in reversed(range(len(text_list))):
#     if " " in text_list[i]: # если содержит пробел  TRUE
#         text_list.pop(i) # удаляем
#     else: # если не содержит пробел False,
#         text_list[i] = text_list[i].lower() # переводим в нижний регистр
#
# print(f'Обработанный список:', text_list)

# VAR 2
#text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# text_list = input().split(", ")# Hello, Python Programming, World, Advanced Topics, Simple
# print(text_list)
# new_list = []
# for i in text_list:
#     if " " not in i:
#         new_list.append(i.lower())
# print(f'Обработанный список:', new_list)

#________________________________
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# filtered_list = []
# # Итерация по каждой строке
# for text in text_list:
#
# # Проверка на наличие пробела:
# # Если пробел НЕ найден (т.е., строка состоит из одного слова)
# # text.find(' ') возвращает -1, если пробел не найден.
#     if text.find(' ') == -1:
#     # Или более читаемо: if ' ' not in text:
#     # Преобразование в нижний регистр
#     single_word = text.lower()
#
# # Добавление в новый список
#     filtered_list.append(single_word)
# print(f"Обработанный список: {filtered_list}")

#________________________________


# 2. Обновление цен товаров
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару
# и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Данные:
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# Пример вывода:
# Введите скидку (в процентах): 17
#
# Товар          Старая цена       Новая цена
# Laptop            1200.00$          996.00$
# Mouse               25.00$           20.75$
# Keyboard            75.00$           62.25$
# Monitor            200.00$          166.00$

# # VAR 1 - с исправлениями
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# discount = int(input("Введите скидку (в процентах): " ))
# print(f'{"Products":<15}{"Old_price":>16}{"New_price":>16}')
#
#
# for product in products:
#     name = product[0]
#     price = product[1]
#     new_price = price * (1 - discount / 100)
#     rounded_price = round(new_price)
#     product.append(rounded_price)
#
#     print(f'{name:<15}'f'{price:>15.2f}$'f'{new_price:>15.2f}$')
# print(products)

















