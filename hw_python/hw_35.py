# Домашнее задание
# 1. Счётчик экземпляров
# Создайте класс User, представляющий пользователя.
# ● При создании должны указываться логин (username) и пароль (password).
# ● У класса должно быть поле total_users, хранящее общее количество
# созданных пользователей.
# ● При каждом создании нового объекта User, счётчик должен увеличиваться.
# ● Добавьте метод get_total(), возвращающий количество пользователей.
# ● Проверьте, что счётчик работает.
# Пример вывода:
# Total users: 2

# class User:
#     total_users = 0
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         User.total_users += 1
#
#     @classmethod
#     def get_total(cls):
#         return f'Total users: {cls.total_users}'
#
# user1 = User('Bob','12345')
# user2 = User('Alex','1bvhbA5')
# user3 = User('Boris','A_145_2010_like')
# user4 = User('','')
# print(User.get_total())

#________________________________
# 2. Проверка данных пользователя
# Доработайте класс User.
# ● Добавьте валидации полей при создании.
# ● Имя должно быть непустой строкой.
# ● Пароль должен быть строкой длиной не менее 5 символов.
# ● Если данные некорректны — выбрасывайте ValueError.
# ● Добавьте строковое представление объекта.
# ● Проверьте работу класса с разными значениями. (как отдельная задача)
# Пример вывода:
# User: alice
# ...
# ValueError: Invalid password: 'qwe'.
# Пример вызова:
# user1 = User("alice", "secret")
# user2 = User("bob", "qwe")

# class User:
#     total_users = 0
#     def __init__(self, username, password):
#         if not isinstance(username, str) or len(username) <= 0:
#             raise ValueError (f"Invalid username. {username}. The name must not be an empty string")
#         if len(password) < 5:
#             raise ValueError(f"Invalid password: {password}. The password must be longer than 5 characters")
#
#         self.username = username
#         self.password = password
#         User.total_users += 1
#
#     def __str__(self):
#         return f"User: {self.username}"
#     @classmethod
#     def test_options(cls, username, password):
#         try:
#             new_user = cls(username,password)
#             return str(new_user)
#         except ValueError as e:
#             return f"ValueError: {e}"
#
# user1 = User.test_options("alice", "secret")
# print(user1)
# user2 = User.test_options("bob", "qwe")
# print(user2)






