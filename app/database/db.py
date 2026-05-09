import sqlite3


conn = sqlite3.connect("database.db",check_same_thread=False)

# CREATING DATABASE
def create_user_table():
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users(
                       user_id TEXT PRIMARY KEY,
                       full_name TEXT,
                       email TEXT UNIQUE,
                       hashed_password TEXT,
                       role TEXT,
                       created_at TEXT,
                       updated_at TEXT
                   )
                   """)
    conn.commit()

def create_tasks_table():
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks(
                       task_id TEXT PRIMARY KEY,
                       user_id TEXT,
                       project_name TEXT,
                       task_name TEXT,
                       description TEXT,
                       priority TEXT,
                       status TEXT,
                       created_at TEXT,
                       due_date TEXT,
                       updated_at TEXT
                   )
                   """)
    conn.commit()

# INSERT USERS DATA

def insert_user(user_id,full_name,email,hashed_password,role,created_at,updated_at):
    cursor = conn.cursor()

    cursor.execute("""
                       INSERT INTO users(user_id,full_name,email,hashed_password,role,created_at,updated_at)
                       VALUES (?,?,?,?,?,?,?)
                   """,(user_id,full_name,email,hashed_password,role,created_at,updated_at))
    conn.commit()

def insert_task(task_id,user_id,project_name,task_name,description,priority,status,created_at,due_date,updated_at):
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO tasks(task_id,user_id,task_name,description,priority,status,created_at,due_date,updated_at)
                   VALUES (?,?,?,?,?,?,?,?,?)
                   """,(task_id,user_id,project_name,task_name,description,priority,status,created_at,due_date,updated_at))
    conn.commit()
    
# SEARCH DATA

def locate_email(email):
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT * FROM users WHERE email = ?
                   """,(email,))
    user_account = cursor.fetchone()
    return user_account
