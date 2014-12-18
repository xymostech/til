import sqlite3
import db

def add_user(username, password):
    with db.get_db() as the_db:
        cursor = the_db.cursor()
        cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
        the_db.commit()

def check_login(username, password):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        real_password = user["password"]
        return real_password == password
    else:
        return False

def get_userid(username):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    return user["userid"]
