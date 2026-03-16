# Домашнее задание
# 1. Создание базы
# Напишите программу, которая:
# ● создаёт базу данных notes_app_<your_group>_<your_full_name>
# ● выбирает эту базу через USE notes_app
# ● выводит сообщение о результате
# Пример вывода:
# Database 'notes_app' created or already exists.
#
# import pymysql
#
# config = {'host': 'ich-edit.edu.itcareerhub.de',
#           'user': 'ich1',
#           'password': 'ich1_password_ilovedbs'
#           }
#
# connection = pymysql.connect(**config)
# try:
#     with connection.cursor() as cursor:
#         # Создание новой базы данных (если ещё не существует)
#         notes_app = 'notes_app_101025_ptm_Viktoriia_Boichenko'
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {notes_app}")
#         cursor.execute(f"USE {notes_app}")
#         if connection.open:
#             print(f"Database {notes_app} created or already exists")
#
# except pymysql.MySQLError as e:
#     print (f"{e}")
#
# connection.close()
#
# _______________
# 2. Добавление заметок
# Продолжите предыдущую программу:
# ● создайте таблицу notes с полями: id, title, content
# ● вставьте одну заметку в таблицу
# ● выполните commit() после вставки
# ● выведите все заметки используя DictCursor
# Пример вывода:
# Note added: Shopping list
#
# import pymysql
# from pymysql.cursors import DictCursor  # импорт класса
#
# config = {
#     'host': 'ich-edit.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'ich1_password_ilovedbs',
#     'cursorclass': DictCursor  # ссылка на класс
#     }
#
# connection = pymysql.connect(**config)
# try:
#     with connection.cursor() as cursor:
#         # Создание новой базы данных (если ещё не существует)
#         notes_app = 'notes_app_101025_ptm_Viktoriia_Boichenko'
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {notes_app}")
#         cursor.execute(f"USE {notes_app}")
#         cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(255),
#         content TEXT
#         )
#         """)
#         cursor.execute(
#             "INSERT INTO notes (title, content) VALUES(%s, %s)",
#             ("Shopping list","Milk, Bread, Eggs")
#         )
#         connection.commit()
#
#         cursor.execute("SELECT * FROM notes")
#         notes = cursor.fetchall()
#         for note in notes:
#             print(f"Note added: {note['title']}")
#
#
#         if connection.open:
#             print(f"Database {notes_app} created or already exists")
#
# except pymysql.MySQLError as e:
#     print (f"{e}")
#
# connection.close()