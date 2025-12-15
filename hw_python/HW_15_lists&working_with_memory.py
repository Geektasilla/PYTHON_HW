# 1. Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки,
# содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Данные:
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

# VAR 1
#text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#text_list = input().split(", ") # Hello, Python Programming, World, Advanced Topics, Simple
# for i in reversed(range(len(text_list))):
#     if " " in text_list[i]: # если содержит пробел  TRUE
#         text_list.pop(i) # удаляем
#     else: # если не содержит пробел False,
#         text_list[i] = text_list[i].lower() # переводим в нижний регистр
#
# print(f'Обработанный список:', text_list)

# VAR 2
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# text_list = input().split(", ")# Hello, Python Programming, World, Advanced Topics, Simple
# new_list = []
# for i in text_list:
#     if " " not in i:
#         new_list.append(i.lower())
# print(f'Обработанный список:', new_list)


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

# VAR 1 - с исправлениями
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# discount = int(input("Введите скидку (в процентах): " ))
# print(f'{"Products":<15}{"Old_price":>16}{"New_price":>16}')
#
# for product, price in products:
#     new_price = price * (1 - discount / 100)
#     print(f'{product:<15}'f'{price:>15.2f}$'f'{new_price:>15.2f}$')

# VAR 2 для автоматизации
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
# discount = int(input("Введите скидку (в процентах): " ))
#
# product_max = max(len(products) for product, price in products) + 10
# price_max = max(len(str(price)) for _, price in products) + 10
# new_price_max = max(len(str(new_price)) for new_price in products) + 10
# print(f'{"Products":<{product_max}} {"Price":>{price_max}} {"New_price":>{new_price_max}}')
#
# for product, price in products:
#     new_price = price * (1 - discount / 100)
#     print(f'{product:<{product_max}}'f'{price:>{price_max}.2f}$'f'{new_price:>{new_price_max}.2f}$')















