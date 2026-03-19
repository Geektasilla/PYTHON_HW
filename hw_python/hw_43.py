# 1.Добавление товаров
# Создайте программу, которая подключается к MongoDB и:
# выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# # очищает коллекцию перед началом
# # добавляет 3 товара с полями: name, price, stock
# # выводит сообщение о количестве добавленных товаров
# #
# # Пример вывода:
# # 3 products inserted
# #
# from pymongo import MongoClient
# # подключаемся к MongoDB
# client = MongoClient('mongodb://ich_editor:verystrongpassword'
#                      '@mongo.itcareerhub.de/?readPreference=primary'
#                      '&ssl=false&authMechanism=DEFAULT&authSource=ich_edit'
#                      )
# # выбираем базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# db = client.ich_edit
# collection = db.products_101025_ptm_VBoichenko
# # очищаем коллекцию перед началом
# collection.delete_many({})
# # добавляем 3 товара с полями: name, price, stock
# products = [
#     {'name': 'Mouse', 'price': 60.99, 'stock': 100},
#     {'name': 'Tablet', 'price': 1000.85, 'stock': 50},
#     {'name': 'Laptop', 'price': 1500.50, 'stock': 20}
# ]
#
# result = collection.insert_many(products)
#
# # считаем количество добавленных товаров
# total_count = len(result.inserted_ids)
# выводит сообщение о количестве добавленных товаров
# print(f"{total_count} products inserted")
#_________________
# 2.Увеличение цен
# Продолжите предыдущую задачу. Теперь программа должна:
# увеличить цену всех товаров на 20%
# вывести количество обновлённых записей
# затем вывести список всех товаров с новыми ценами
#
# Пример вывода:
# Prices updated for 3 products.
# Updated products:
# - Pen - $1.80
# - Notebook - $4.79
# - Backpack - $30.00

# from pymongo import MongoClient
# # подключаемся к MongoDB
# client = MongoClient('mongodb://ich_editor:verystrongpassword'
#                      '@mongo.itcareerhub.de/?readPreference=primary'
#                      '&ssl=false&authMechanism=DEFAULT&authSource=ich_edit'
#                      )
# # выбираем базу ich_edit и коллекцию products_<your_group>_<your_full_name>
# db = client.ich_edit
# collection = db.products_101025_ptm_VBoichenko
#
# # увеличить цену всех товаров на 20%
# update_result = collection.update_many({}, {'$mul': {'price': 1.2}})
# # вывести количество обновлённых записей
# print(f'Prices updated for {update_result.modified_count} products.')
# # затем вывести список всех товаров с новыми ценами
# print('Updated products:')
# for product in collection.find():
#     print(f"- {product['name']} - ${product['price']:.2f}")




