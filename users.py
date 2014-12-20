import sqlite3
import db
import bcrypt

def add_user(username, password):
    with db.get_db() as the_db:
        cursor = the_db.cursor()
        res = cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if res.fetchone() is None:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, hashed))
            return True
        else:
            return False

def check_login(username, password):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        hashed = user["password"].encode('utf-8')
        return bcrypt.hashpw(password.encode('utf-8'), hashed) == hashed
    else:
        return False

def get_userid(username):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    return user["userid"]
