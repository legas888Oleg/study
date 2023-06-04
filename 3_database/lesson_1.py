import sqlite3 as sql

# Создание и подключене к БД
connection = sql.connect('test.sqlite')
# Создане курсора для работы с БД
q = connection.cursor()

try:
    q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, password varchar)''')
    connection.commit()
except Exception:
    print("Таблица уже создана")

user_name = input("Введите ваше имя: ")
user_password = input("Введите пароль: ")

print("Список пользователей:\n")
q.execute("INSERT INTO user (name, password) VALUES ('%s', '%s')"%(user_name, user_password))
connection.commit()

q.execute("SELECT * FROM user")
row = q.fetchone()

while row is not None:
    print("Имя:", row[1], "| Пароль:", row[2])
    row = q.fetchone()

# Отключение от базы данных
q.close()
connection.close()