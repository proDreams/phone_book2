import sqlite3 as sl
from os import path
import user_interface
import user_inputs


STUDENT_FIELDS = ['student_id', 'name', 'patronym', 'surname', 'birthdate', 'phone', 'class']


def create_db(file_name):
    db = sl.connect(f'{file_name}.db')
    db.execute('CREATE TABLE IF NOT EXISTS {}('
               'student_id INTEGER PRIMARY KEY, '
               'name TEXT NOT NULL, '
               'patronym TEXT NOT NULL, '
               'surname TEXT NOT NULL, '
               'birthdate TEXT NOT NULL, '
               'phone TEXT NOT NULL, '
               'class TEXT NOT NULL)'.format('students'))
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
    if not path.exists(f'{file_name}.db'):
        if user_inputs.ask_fill_input(0, file_name):
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
        user_interface.print_errors(1)
        create_db(file_name)
        user_interface.print_notifications(0)
    return True


def search_record(field_ind, query, file_name, compliance=False):
    """
    Ищет запись в базе по параметру
    """
    field = STUDENT_FIELDS[int(field_ind)-1]
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    if compliance:
        cur.execute(f"SELECT * FROM students WHERE {field}='{query}'; ")
    else:
        cur.execute(f"SELECT * FROM students WHERE {field} LIKE '%{query}%'; ")
    results = cur.fetchall()
    db.close()
    return results


def check_id(r_id, file_name):
    '''
    Проверяет, есть ли запись в введенным id в базе
    '''
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute(f"SELECT * FROM students WHERE student_id='{r_id}'; ")
    results = cur.fetchall()
    db.close()
    return results


def get_updates(r_id, field_ind, value, file_name):
    """
    Формирует исправленную запись
    """
    record = list(*search_record(1, r_id, file_name, compliance=True))
    record[int(field_ind)] = f'>>> {value} <<<'
    return record


def change_field(r_id, field_ind, value, file_name):
    """
    Меняет поле записи
    """
    field = STUDENT_FIELDS[int(field_ind)]
    db = sl.connect(f'{file_name}.db')
    cur = db.cursor()
    cur.execute(f"UPDATE students SET {field} = '{value}' WHERE student_id={r_id}")
    db.commit()
    db.close()
