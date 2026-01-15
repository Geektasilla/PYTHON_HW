# 1.Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь
# с подсчётом количества каждой буквы,игнорируя регистр.
# Данные:
# text = "Programming is fun!"
#Пример вывода:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

# Var 1
# def conversion_dictionary_with_count_of_letters(text):
#     res = list(text.lower())
#     res = {i: res.count(i) for i in res if i.isalpha()}
#     return res
#
# text = input() # jhjg!##@$%#^___08977
# # text = "Programming is fun!"
# print(conversion_dictionary_with_count_of_letters(text))

#Var 2
# def conversion_dictionary_with_count_of_letters(text):
#     res = {i: text.lower().count(i) for i in list(text.lower()) if i.isalpha()}
#     return res
#
# text = input() # jhjg!##@$%#^___08977
# # text = "Programming is fun!"
# print(conversion_dictionary_with_count_of_letters(text))


# Var 3
# from collections import Counter
# def conversion_dictionary_with_count_of_letters(text):
#     counter = Counter(text.lower())
#     counter = {k: v for k, v in counter.items() if k.isalpha()}
#     return counter
#
# text = "Programming is fun!"
# print(conversion_dictionary_with_count_of_letters(text))


#________________________________________________________________________________________________

# 2. Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
# Пример вывода:
# {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}

# from collections import defaultdict
#
# def group_students_by_faculty(students):
#     name_dict = defaultdict(list)
#     for name, classes in students:
#         name_dict[name].append(classes)
#     return dict(name_dict)
#
# students = [
#     ("class1", "Alice"),
#     ("class2", "Bob"),
#     ("class1", "Charlie"),
#     ("class3", "Daisy")
# ]
#
# print(group_students_by_faculty(students))


