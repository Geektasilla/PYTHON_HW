# Python Fundamentals 2025: Домашнее задание 27

# 1. Фильтрация по ключевому слову
# Напишите программу, которая ищет в файле все строки,
# содержащие указанное пользователем слово, и сохраняет их в новый файл.
# Имя нового файла формируется как <keyword>_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.

# import os
#
# file_name = input("Введите имя файла для поиска: ")
# key_word = input(" Введите ключевое слово: ")
#
# # Проверяем путь к файлу
# if not os.path.isfile(file_name):
#     print(f"Файл {file_name} не существует")
#     # Если файл существует, читаем его
# else:
#     #print(f"Файл {file_name} существует")
#     with open(file_name, "r", encoding="utf-8") as f:
#         lines = f.readlines()
#
#         result = [line.lower() for line in lines if key_word in line.lower()]
#         # и сохраняет их в новый файл
#         if result:
#             new_file_name = f"{key_word}_{file_name}"
#             with open(new_file_name, "w", encoding="utf-8") as new_f:
#                 new_f.writelines(result)
#                 print(f"Строки, содержащие '{key_word}', сохранены в {new_file_name}.")
#
#         # Если совпадения не найдены, новый файл не создаётся.
#         else:
#             print(f"Строки, содержащие '{key_word}', не найдены.")

#_______________________________
# 2. Поиск и удаление дубликатов
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# Имя нового файла формируется как unique_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Исходный порядок строк должен сохраниться.
# Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

# import os
#
# # 1. Requesting a file name.
# file_name = input("Input file name: ")
# # 2. File reading and error handling.
# try:
#     lines_list = []
#     with open(file_name, "r", encoding="utf-8") as file:
#         print("File opened")
#         for line in file:
#             lines_list.append(line.strip())
# except FileNotFoundError:
#     print(f"Error: file '{file_name}' not found")
# else:
#     print("File read successfully. Removing duplicates...")
#     # 3. Deleting duplicates.
#     unique_lines = []
#     founded_lines = set() # quick check
#     for line in lines_list:
#         if line not in founded_lines:
#             unique_lines.append(line)
#             founded_lines.add(line)
#
#     # 4. Creating a new file name.
#     directory_path = os.path.dirname(file_name)
#     original_basename = os.path.basename(file_name)
#     new_basename = f"unique_{original_basename}"
#     new_file_name = os.path.join(directory_path, new_basename)
#     # 5. Writing unique lines to the new file.
#     with open(new_file_name, "w", encoding="utf-8" ) as new_file:
#         for line in unique_lines:
#             new_file.write(line + '\n')
#
#     # 6. Printing the final message.
#     print(f"Duplicates removed. Unique lines saved in {new_file_name}")
#


