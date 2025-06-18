import sqlite3
from datetime import datetime
from tabulate import tabulate
from faker import Faker


fake = Faker()
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

def add_task(description):
    today = datetime.today().strftime('%Y%m%d')
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    query_add = '''
        INSERT INTO tasks(description, date, done) VALUES (?, ?, ?)'''
    
    cur.execute(query_add, (description, today, 0))
    con.commit()
    con.close()

def get_all_tasks():
    try:
        con = sqlite3.connect("db.sqlite")
        cur = con.cursor()
        cur.execute ('''
            SELECT*
            FROM tasks ;
        ''')
        results = cur.fetchall()
        con.close()
        if not results:
            print("No tasks found")
        
        table = []
        for row in results:
            id, desc, date, done = row
            formatted_date = datetime.strptime(str(date), '%Y%m%d').strftime('%Y-%m-%d')
            status = "✅" if done else "❌"
            table.append([id, desc, formatted_date, status])

        print(tabulate(table, headers=["ID", "Description", "Date", "Done"], tablefmt="fancy_grid"))
    except  sqlite3.OperationalError as error:
        if "no such table" in str(error):
            print("No tasks found") 

def delete_task(task_id):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute('''
        DELETE FROM tasks WHERE id = ?
''', (task_id,))
    con.commit()
    con.close()

def mark_done(task_id):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute('''
        UPDATE tasks SET done = 1 WHERE id = ?
    ''', (task_id,))
    con.commit()
    con.close()


def get_task_description(task_id):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute('''
    SELECT description FROM tasks WHERE id = ? 
    ''', (task_id,))
    result = cur.fetchone()
    con.close()
    return result[0] if result else None

def get_unmark_task():
    try:
        con = sqlite3.connect("db.sqlite")
        cur = con.cursor()
        cur.execute('''
        SELECT id, description FROM tasks WHERE done = 0 ORDER BY date 
        ''')
        un_tasks = cur.fetchall()
        con.close()
        if not un_tasks:
            return None
        table = []
        for id, desc in un_tasks:
            table.append([id, desc])
        return tabulate(table, headers=["ID", "Task"], tablefmt="fancy_grid")
    except  sqlite3.OperationalError as error:
        if "no such table" in str(error):
            print("No tasks found") 

def edit_task(task_id, new_description):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute('''
    UPDATE tasks SET description = ? WHERE id = ?
    ''', (new_description, task_id))
    con.commit()
    con.close()

def generate_fake_tasks(count):
    for _ in range(count):
        tasks = fake.sentence(nb_words = 5)
        add_task(tasks)

def delete_all():
    # USE only for tests
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute('''
        DROP TABLE tasks
''')
    con.commit()
