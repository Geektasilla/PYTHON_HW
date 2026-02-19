# 1. Извлечение дат
# Реализуйте программу, которая должна:
# Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
# Данные:
# text = "The events N 123456 happened on 15/03/2025,
# 01.12.2024 and 09-09-2023.
# Deadline: 28/02/2022."
# Пример вывода:
# 15/03/2025
# 01.12.2024
# 09-09-2023
# 28/02/2022
#
import re
# # Для проверки:
# text = "10/05/2024, затем 25.12.2023 и в конце 01-01-2025."
# text = "Неправильные даты: 15/03-2023 и 01.02/2024. А вот 11-11-2011 - правильная."
# text = "5/12/2023, 05-1/2023, 05.12.23. И еще одна 99.99.9999."
# text = "Начало01-01-2020конец. И еще одна20.02.2022сразу."

#  VAR 1
# text = input()
# text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
# Найдём даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
# found_dates = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}[.]\d{2}[.]\d{4}"
# print(*list(re.findall(found_dates,text)),sep='\n')

# VAR 2
# # text = input()
# text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
# # Найдём даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
# found_dates = r"\d{2}([/.-])\d{2}\1\d{4}"
# # перебираюм найденные даты и вывожу их в цикле
# # re.finditer() возвращает итератор специальных "объектов совпадения" (match objects).
# for dates in re.finditer(found_dates, text):
#     print(dates.group())

# __________________________________________________________________________________________________
# 2. Разделение списка тегов
# Реализуйте программу, которая должна:
# Прочитать строку с тегами, введёнными пользователем.
# Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с
# запятой, слэши или пробелы).
# Удалить лишние пробелы и пустые значения.
# Данные:
# tag_input = "python, data-science / machine-learning; AI neural-networks"
# Пример вывода:
# ['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']

# import re
# # tag_input = input() # "; python, data-science / "
# tag_input = "python, data-science / machine-learning; AI neural-networks"
# # создаю шаблон с разделителями по условию
# pattern = r"[,;/\s]+" # + это одна или более
# # разделяю строки по шаблону
# edited_str = re.split(pattern, tag_input)
# # удаляю пустые значения
# result_str = [ed for ed in edited_str if ed != '' ]
# print(result_str)









