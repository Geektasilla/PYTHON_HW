# Python Fundamentals 2025: Домашнее задание 11
# 1. Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

# VAR 1
# text = "My number is 123-456-789"# input()
# print(text)
# result = ''
#
# for tx in text:
#     if tx.isdigit():
#         result += "*"
#     else:
#         result += tx
#
# print(result)

# VAR 2
# text = "My number is 123-456-789"
# print(text)
# result = text
# for i in "0123456789":
#     result = result.replace(i, "*")
# print(result)

# Var 3
# text = "My number is 123-456-789"
# result = ""
# for char in text:
#     if char.isalpha():
#         result += char
#     elif char.isdigit():
#         result += "*"
#     else:
#         result += char
# print(result)

# Var 4
# text = "My number is 123-456-789"
# encoding = text
# print(text)
# for i in "0123456789":
#         encoding = encoding.replace(i,"*")
# print(encoding)
#_______________________________________________________________________________________
# 2. Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
# с указанием их количества.
# Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

# VAR 1
# text = "Programming in python"
# #text = input()
# print("Строка", text)
# text = text.lower()
# collect = 0
# uniq = ""
#
# for tx in text:
#     if tx not in uniq:
#         uniq += tx
#         collect  = text.count(tx)
#         if collect > 1:
#             print(f"Символ '{tx}' встречается {collect} раз(a)")

#_______________________________________________________________________________________
# 3. Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
#
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# words = text.split()
# a = ""
# num = 0
# for word in words:
#     if word.replace(".", "", 1).isdigit():
#         num = 10 * float(word)
#         a += " " + str(num)
#     else:
#         a += " " + word
#
# print(a)















