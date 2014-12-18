import sqlite3
from flask import g, _app_ctx_stack

class FakeG:
    def in_app_ctx(self):
        return _app_ctx_stack.top is not None

    def __getattr__(self, key):
        if self.in_app_ctx():
            return getattr(g, key, None)
        else:
            return None

    def __setattr__(self, key, value):
        if self.in_app_ctx():
            setattr(g, key, value)
        return self

gg = FakeG()

DATABASE = "db.sqlite"

def get_db():
    db = gg._database
    if db is None:
        db = gg._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def cleanup_db(exception):
    db = gg._database
    if db is not None:
        db.close()
