import sqlite3

con = sqlite3.connect("db.sqlite")

cur = con.cursor()

query_1 = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    date INTEGER,
    done BOOLEAN NOT NULL DEFAULT 0
);
'''
cur.execute(query_1)
con.close()


