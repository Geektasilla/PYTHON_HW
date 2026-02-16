# Python Fundamentals 2025: Домашнее задание 30

# 1. Анализ курсов студентов
# Реализовать программу, которая должна:
# Прочитать файл student_courses.json, содержащий:
# имя,
# дату рождения (birth_date) в формате дд.мм.гггг,
# дату поступления (enrollment_date) в том же формате,
# список курсов.
#
# Вычислить:
# Общее количество студентов.
# Средний возраст на момент поступления.
# Количество студентов на каждом курсе.
# Сохранить отчёт в JSON-файл student_courses_report.json.
# Данные:
# [
#   {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
#   {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
#   {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
#   {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
#   {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
#   {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
#   {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
#   {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
#   {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
#   ...
# ]
#
# Пример вывода (student_courses_report.json):
# {
#     "total_students": 100,
#     "average_enrollment_age": 27.9,
#     "students_per_course": {
#         "Art": 21,
#         "Biology": 18,
#         "Business": 28,
#         "Chemistry": 16,
#         "Economics": 23,
#         "History": 9,
#         "Linguistics": 23,
#         "Math": 23,
#         "Philosophy": 19,
#         "Physics": 19
#     }
# }

#SOLUTION:

import json
# 1. Reading a file. Creating a function.
def students_data(file_name):
    # Opening a file and reading it
    with open(file_name, "r",encoding="utf-8") as f:
        data = json.load(f)
    return data

# Total numbers of students
students = students_data("student_courses.json")
print(f"Total numbers of students: {len(students)}")

# 2. Average age at admission
from datetime import datetime
# Creating a function.
def average_age(students):
    total_age = 0
    for student in students:
        # Converting a date from string to datetime
        birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
        enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
        # Calculating the age
        age = enrollment_date - birth_date
        # Converting days to years
        total_age += age.days / 365.25
    return total_age / len(students)

average_age = average_age(students)
print(f"Average age at admission: {average_age:.1f} years")

# 3. Number of students per course
from collections import Counter
# Creating a function.
def students_counter(students):
    all_courses = []
    for student in students:
        # add list of courses to the list of all courses
        # .extend(iterable) — добавляет элементы из последовательности. Он "распаковывает" переданную последовательность и добавляет её содержимое.
        all_courses.extend(student["courses"])
    return Counter(all_courses)

students_per_course = students_counter(students)
print(f"Number of students per course:{students_per_course}")

# 4. Save the report in JSON-файл student_courses_report.json.
import json
report = {
    "total_students": len(students),
    "average_enrollment_age": average_age,
    "students_per_course": students_per_course
}
with open("student_courses_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)




