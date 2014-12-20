import datetime
import db
import itertools
import sqlite3

class Post:
    def __init__(self, row):
        self.postid = row['postid']
        self.post = row['post']
        self.time = datetime.datetime.fromtimestamp(row['time'])
        self.day = self.time.date()

    @property
    def timestr(self):
        return self.time.strftime("%I:%M %p")

def add_post(post, userid):
    with db.get_db() as the_db:
        cursor = the_db.cursor()
        cursor.execute("INSERT INTO posts VALUES (NULL, strftime('%s', 'now'), ?, ?)", (post, userid))

def group_posts_by_date(posts):
    dates = {}
    for k, g in itertools.groupby(posts, lambda x: x.day):
        dates[k] = list(g)

    return dates

def get_posts(userid):
    cursor = db.get_db().cursor()
    posts = [
        Post(row)
        for row in cursor.execute(
                "SELECT * FROM posts WHERE creator=? ORDER BY time DESC",
                (userid,)).fetchall()
    ]

    return posts
