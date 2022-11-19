import sqlite3 as sl
from os import path
import user_interface
import user_inputs


def create_db(file_name):
    db = sl.connect(f'{file_name}.db')
    db.execute('CREATE TABLE IF NOT EXISTS {}('
               'student_id INTEGER PRIMARY KEY, '
               'name TEXT NOT NULL, '
               'patronym TEXT NOT NULL, '
               'surname TEXT NOT NULL, '
               'birthdate TEXT NOT NULL, '
               'phone TEXT NOT NULL, '
               'grade TEXT NOT NULL)'.format('students'))
    db.commit()
    db.close()


def get_db(file_name):
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    db.close()
    return rows


def add_student(contact, file_name):
    create_db(file_name)
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute("INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?)", tuple(value for value in contact))
    db.commit()
    db.close()


def remove_student(s_id, file_name):
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute(f"DELETE FROM students WHERE student_id={s_id}")
    db.commit()
    db.close()


def check_file_exist(file_name):
    """
    Проверяет наличие файла по указанному пути
    """
    if not path.exists(file_name):
        if user_inputs.ask_fill_input(0):
            create_db(file_name)
            return True
        else:
            return False
    else:
        return True


def check_table_exist(file_name):
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'; ")
    check = cur.fetchall()
    db.close()
    if not check:
        if user_inputs.ask_fill_input():
            create_db(file_name)
            user_interface.print_notifications(0)
            return True
        else:
            return False
    else:
        return True
