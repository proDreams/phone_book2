import sqlite3 as sl
from os import path
import user_interface
import user_inputs


STUDENT_FIELDS = ['student_id', 'name', 'patronym',
                  'surname', 'birthdate', 'phone', 'class']


def db_connect(file_name):
    file = f'{file_name}.db'
    try:
        con = sl.connect(file)
        return con
    except sl.Error as e:
        # TODO записать в log вместо консоли перед продакшеном
        print(f'Ошибка: {e}')


def execute_query(con, query, data=None):
    with con:
        try:
            if data:
                res = con.executemany(query, data)
            else:
                res = con.execute(query)
            return res
        except sl.Error as e:
            # TODO записать в log вместо консоли перед продакшеном
            print(f'Ошибка: {e}')


def create_db(file_name):
    table_name = 'students'
    sql_query = f'''CREATE TABLE IF NOT EXISTS {table_name}(
                 student_id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 patronym TEXT NOT NULL,
                 surname TEXT NOT NULL,
                 birthdate TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 class TEXT NOT NULL);'''
    execute_query(db_connect(file_name), sql_query)


def get_db(file_name):
    sql_query = "SELECT * FROM students"
    return execute_query(db_connect(file_name), sql_query)


def add_student(contact, file_name):
    # TODO а может лучше пробовать создавать базу только один раз при запуске?
    create_db(file_name)
    sql_query = "INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?)"
    data = [tuple(contact)]
    return execute_query(db_connect(file_name), sql_query, data)


def remove_student(s_id, file_name):
    sql_query = f"DELETE FROM students WHERE student_id={s_id}"
    execute_query(db_connect(file_name), sql_query)


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
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='students'; ")
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

    if compliance:
        sql_query = f"SELECT * FROM students WHERE {field}='{query}'; "
    else:
        sql_query = f"SELECT * FROM students WHERE {field} LIKE '%{query}%'; "
    return execute_query(db_connect(file_name), sql_query).fetchall()


def check_id(r_id, file_name):
    '''
    Проверяет, есть ли запись в введенным id в базе
    '''
    sql_query = f"SELECT * FROM students WHERE student_id='{r_id}'; "
    return execute_query(db_connect(file_name), sql_query).fetchall()


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
    sql_query = f"UPDATE students SET {field} = '{value}' WHERE student_id={r_id}"
    execute_query(db_connect(file_name), sql_query)
