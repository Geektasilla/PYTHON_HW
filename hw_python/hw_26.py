# Python Fundamentals 2025: Домашнее задание 26

# 1.Список файлов и папок
# Напишите программу, которая принимает путь к директории
# через аргумент командной строки и выводит:
# Отдельно список папок
# Отдельно список файлов
# Пример запуска
# python script.py /home/user/documents
# Пример вывода
# Содержимое директории '/home/user/documents':
# Папки:
# - folder1
# - folder2
# Файлы:
# - file1.txt
# - file2.txt
# - notes.docx

# # 1. Импортировать необходимые модули (sys, os)
# import os
# import sys
# # 2. Получить путь к директории из аргументов командной строки (sys.argv)
# if len(sys.argv) == 2:
#     directory_path = sys.argv[1]
# else:
#     directory_path = input("Введите путь к директории: ")
#
# # # 3. Проверить, существует ли указанный путь (os.path.exists)
# if os.path.isdir(directory_path):
#     print(f"Директория '{directory_path}' существует.")
#
#     # 4. Если путь существует, получить список содержимого директории (os.listdir)
#     try:
#         contents = os.listdir(directory_path)
#     except OSError:
#         print("Ошибка доступа к директории.")
#         sys.exit(1)
#
#     # 5. Создать два пустых списка: один для папок, другой для файлов
#     folders = []
#     files = []
#     # 6. Перебрать элементы содержимого директории
#     # 7. Для каждого элемента проверить, является ли он папкой (os.path.isdir)
#     for item in contents:
#         item_path = os.path.join(directory_path, item)
#         # 8. Если это папка, добавить ее в список папок
#         if os.path.isdir(item_path):
#             folders.append(item)
#             # 9. Если это файл, добавить его в список файлов
#         elif os.path.isfile(item_path):
#             files.append(item)
#
#     # 10. Вывести отсортированный список папок
#     print("Папки:")
#     if folders:
#         for folder in sorted(folders):
#             print(f"- {folder}")
#     else:
#         print("- (пусто)")
#
#     # 11. Вывести отсортированный список файлов
#     print("Файлы:")
#     if files:
#         for file in sorted(files):
#             print(f"- {file}")
#     else:
#         print("- (пусто)")
#
# # 12. Если путь не существует или это не директория, вывести сообщение об ошибке
# else:
#     print(f"Ошибка: Путь '{directory_path}' не существует или не является директорией.")
#

#____________________________________________________
# 2.Поиск и удаление файлов с указанным расширением
# Напишите программу, которая:
# Принимает путь к директории и расширение файлов через аргумент командной строки.
# Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
# Спрашивает у пользователя, хочет ли он удалить найденные файлы.
# Если пользователь подтверждает, удаляет их.
# Пример запуска:
# python script.py /home/user/PycharmProjects/project1 .log
# Пример вывода
# Найдены файлы с расширением '.log':
# - logs/error.log
# - logs/system.log
# - logs/backup/old.log
# - logs/backup/debug.log
# Вы хотите удалить эти файлы? (y/n): y
# Удаление завершено.

# Импортировать необходимые модули (sys, os)
import sys
import os

#1. Принять путь к директории и расширение файлов через аргумент командной строки.
# В списке sys.argv под индексом 0 всегда идет имя самого скрипта, а под индексами 1, 2 и далее — те данные, которые ввел пользователь.
    # 2. Проверяем, передал ли пользователь нужное количество аргументов
    # sys.argv[0] - имя скрипта, [1] - путь, [2] - расширение
# if len(sys.argv) == 3:
#     directory_path = sys.argv[1]
#     extension = sys.argv[2]
# else:
#     directory_path = input("Введите путь к директории: ")
#     extension = input("Введите необходимое расширение файлов: ")
#
# # 3. Проверить, существует ли указанный путь (os.path.exists)
# if os.path.isdir(directory_path):
#     print(f"Директория {directory_path} существует")
# else:
#     print(f"Директория {directory_path} не существует")
#     sys.exit(1)
#
# # 4. Если путь существует, рекурсивно искать файлы с этим расширением во всех вложенных папках. (os.walk(path))
# found_files = []
# for root, dirs, files in os.walk(directory_path):
#     for file in files:
#         if file.endswith(extension):
#             found_files.append(os.path.join(root, file))
#
#
# # Спрашивает у пользователя, хочет ли он удалить найденные файлы. (os.path.isfile(path))
# if found_files:
#     print(f"Найдены файлы с расширением '{extension}':")
#     for file in found_files:
#         print(f"- {file}")
#     question = input(f"Удалить все файлы с расширением {extension}? (ДА/НЕТ): ")
#
# # Если пользователь подтверждает, удаляет их.(os.remove(path))
#     question = question.upper()
#     if question == "ДА":
#         for file in found_files:
#             if os.path.isfile(file):
#                 os.remove(file)
#                 # print(f"Файл {file} удален")
#             else:
#                 print(f"Файл {file} не найден")
#         print("Файлы успешно удалены")
#     else:
#         print("Файлы не удалены")
# else:
#     print(f"Файлов с расширением в директории нет")
#     sys.exit(1)
