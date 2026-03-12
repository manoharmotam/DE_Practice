import sqlite3

def get_db():
    return sqlite3.connect("veeam.db", check_same_thread=False)

def init_db():
    db = get_db()
    with open("schema.sql") as f:
        db.executescript(f.read())
    db.commit()
