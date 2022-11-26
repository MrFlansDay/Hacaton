import sqlite3
import hashlib


def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()


with sqlite3.connect("database.db") as db:
    cursor = db.cursor()

    # query = """CREATE TABLE IF NOT EXISTS users (
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # login text,
    # password text,
    # admin bool
    # )"""
    # cursor.execute(query)
    #
    # cursor.execute("INSERT INTO users(login, password) VALUES ('1', '2')")
    #
    # cursor.execute("SELECT * FROM users")
    # print(cursor.fetchall())


def registration():
    login = input("Login: ")
    password = input("Password: ")

    try:
        db1 = sqlite3.connect("database.db")
        cursor1 = db1.cursor()

        db1.create_function("md5", 1, md5sum)

        cursor1.execute("SELECT login FROM users WHERE login = ?", [login])
        if cursor1.fetchone() is None:
            cursor1.execute("INSERT INTO users(login, password) VALUES (?, md5(?))", [login, password])
            db1.commit()
        else:
            print("Такой пользователь уже существует")
            registration()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor1.close()
        db1.close()


def log_in():
    login = input("Login: ")
    password = input("Password: ")

    try:
        db1 = sqlite3.connect("database.db")
        cursor1 = db1.cursor()

        db1.create_function("md5", 1, md5sum)

        cursor1.execute("SELECT login FROM users WHERE login = ?", [login])
        if cursor1.fetchone() is None:
            print("Такого пользователя не существует")
        else:
            cursor1.execute("SELECT password FROM users WHERE login = ? AND password = md5(?)", [login, password])
            if cursor1.fetchone() is None:
                print("Пароль неверный")
            else:
                start(login)
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor1.close()
        db1.close()


def start(login):
    return



