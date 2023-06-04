import mysql.connector


class Lesson_2:
    mydb = ""
    q = ""

    host = "localhost"
    port = "3306"
    user = "root"
    password = ""
    database = ""

    def getConnect(self):
        if self.database == "":
            return mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password)
        else:
            return mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                           database=self.database)

    def __init__(self, database):
        self.createDB(database)

        self.q = self.mydb.cursor()

    def create(self, sql):
        try:
            self.q.execute(sql)
        except Exception:
            print("Создать не получилось")

    def insert(self, sql, params):
        try:
            self.q.execute(sql, params)
            self.mydb.commit()
        except Exception:
            print("Добавить записи не получилось")

    def close(self):
        self.q.close()
        self.mydb.close()

    def createDB(self, name):
        self.mydb = self.getConnect()
        self.q = self.mydb.cursor()
        self.create("CREATE DATABASE IF NOT EXISTS " + name)
        self.database = name
        self.mydb = self.getConnect()


# sql = "SHOW DATABASES"

# for el in q:
#     print(el)
#     connection.commit()
# except Exception:
#     print("База уже создана")

if __name__ == "__main__":
    lesson2 = Lesson_2("ex5")

    lesson2.create("CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INTEGER(3), date_of_birth DATE)")

    users = (
        'Oleg',
        '34',
        '1988-11-25'
    )

    lesson2.insert("INSERT INTO users (name, age, date_of_birth) VALUES (%s, %s, %s)", users)

    lesson2.close()