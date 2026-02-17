# 1. План по дням недели
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели,
# пока пользователь нажимает 'Enter'.
# Данные:
# # Расписание дел на неделю
# weekly_schedule = {
#     "Monday": ["Gym", "Work", "Read book"],
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#     "Friday": ["Work", "Dinner with friends"],
#     "Saturday": ["Hiking", "Rest"],
#     "Sunday": ["Family time", "Rest"]
# }
# Пример ввода:
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана:
# Tuesday: Meeting, Work, Study Python
# ...
# Нажмите 'Enter' для получения плана:
# Sunday: Family time, Rest
# Нажмите 'Enter' для получения плана:
# Monday: Gym, Work, Read book
# Нажмите 'Enter' для получения плана: q
# ...

##SOLUTION:
# weekly_schedule = {
#     "Monday": ["Gym", "Work", "Read book"],
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#     "Friday": ["Work", "Dinner with friends"],
#     "Saturday": ["Hiking", "Rest"],
#     "Sunday": ["Family time", "Rest"]
# }
# import itertools
#
# day_cycler = itertools.cycle(weekly_schedule)
# try:
#     while True:
#         user_input = input("press 'Enter' to get the plan or input 'end' to quit: ")
#         user_input = user_input.strip().lower()
#         if user_input == "end":
#             print("Program finished.")
#             break
#         if user_input != '':
#             continue
#         day = next(day_cycler)
#         print(f"{day}: {', '.join(weekly_schedule[day])}")
#
# except (KeyboardInterrupt, EOFError):
#     pass
# finally:
#     print("\nProgram finished.")

# #_______________________________________________________________________________________________________________________
# 2. Объединение списков продуктов
# Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
# содержащий все продукты в нижнем регистре.
# Выведите содержимое генератора.
# Данные:
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
# Пример вывода:
# apple
# banana
# orange
# carrot
# tomato
# cucumber
# milk
# cheese
# yogurt

##SOLUTION:
# VARIANT 1
# import itertools
# def combine_products(*args):
#     """Combines multiple lists of products into a single generator of lowercase names.
#         :param args: A variable number of lists containing product names.
#         :return: A generator that yields each product name in lowercase.
#         """
#     merged = itertools.chain.from_iterable(args)
#     return (product.lower() for product in merged)
#
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
#
# combined_products = combine_products(fruits, vegetables, dairy)
#
# for product in combined_products:
#     print(product)


# VARIANT 2
# def combine_products(*args):
#     """
#     A function that takes several lists of product names and returns a generator
#     containing all products in lowercase.
#
#     :param args: Several lists, where each list contains product names as strings.
#     :return: A generator that yields each product name in lowercase.
#     """
#     for product_list in args:
#         for product in product_list:
#             yield product.lower()
#
#
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
#
# combined_products = combine_products(fruits, vegetables, dairy)
#
# for product in combined_products:
#     print(product)


# #_______________________________________________________________________________________________________________________
# 3. Комбинации одежды
# Напишите функцию, которая принимает списки типов одежды, цветов и размеров,
# а затем генерирует все возможные комбинации
# в формате "Clothe - Color - Size".
# Данные:
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
# Пример вывода:
# T-shirt - Red - S
# T-shirt - Red - M
# T-shirt - Red - L
# T-shirt - Blue - S
# ...
# Jacket - Black - L
#

##SOLUTION:
# VARIANT 1
# import itertools
# def generate_cloth_combinations(clothes, colors, sizes):
#     """
#     A function that takes lists of clothing types, colors, and sizes, and then generates all possible combinations
#     :param args: Several lists, where each list of clothing types, colors, and sizes, as strings.
#     :return: generates all possible combinations in the format “Clothing - Color - Size”.
#     """
#     return ("-".join(comb) for comb in itertools.product(clothes, colors, sizes))
#
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
#
# result_combinations = generate_cloth_combinations(clothes, colors, sizes)
# for combinations in result_combinations:
#     print(combinations)


# VARIANT 2 (with generators)
# def generate_combinations(clothes, colors, sizes):
#     """
#     A function that takes lists of clothing types, colors, and sizes, and then generates all possible combinations
#     :param args: Several lists, where each list of clothing types, colors, and sizes, as strings.
#     :return: generates all possible combinations in the format “Clothing - Color - Size”.
#     """
#     num_clothes = len(clothes)
#     for item, cloth in enumerate(clothes):
#         for color in colors:
#             for size in sizes:
#                 yield f"{cloth} - {color} - {size}"
#             # Добавляем разделитель, ТОЛЬКО если это НЕ последний тип одежды
#         if item < num_clothes - 1:
#             yield "..."
#
#
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
#
# result_combinations = generate_combinations(clothes, colors, sizes)
# for combinations in result_combinations:
#     print(combinations)
