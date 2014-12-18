import db
import sqlite3
import datetime

class Post:
    def __init__(self, row):
        self.postid = row['postid']
        self.post = row['post']
        self.time = datetime.datetime.fromtimestamp(row['time']).isoformat()

def add_post(post, userid):
    with db.get_db() as the_db:
        cursor = the_db.cursor()
        cursor.execute("INSERT INTO posts VALUES (NULL, strftime('%s', 'now'), ?, ?)", (post, userid))
        the_db.commit()

def get_posts(userid):
    cursor = db.get_db().cursor()
    return [
        Post(row)
        for row in cursor.execute(
                "SELECT * FROM posts WHERE creator=?", (userid,)).fetchall()
    ]
