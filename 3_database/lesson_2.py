import mysql.connector

# Создание и подключене к БД
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="example"
)

# sql = "CREATE DATABASE example"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"
sql = "SHOW TABLES"
# Создане курсора для работы с БД

q = mydb.cursor()

# try:
q.execute(sql)

for el in q:
    print(el)
#     connection.commit()
# except Exception:
#     print("База уже создана")
#
# user_name = input("Введите ваше имя: ")
# user_password = input("Введите пароль: ")
#
# print("Список пользователей:\n")
# q.execute("INSERT INTO user (name, password) VALUES ('%s', '%s')"%(user_name, user_password))
# connection.commit()
#
# q.execute("SELECT * FROM user")
# row = q.fetchone()
#
# while row is not None:
#     print("Имя:", row[1], "| Пароль:", row[2])
#     row = q.fetchone()
#
# # Отключение от базы данных
q.close()
mydb.close()