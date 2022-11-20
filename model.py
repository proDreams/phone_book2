import sqlite3 as sl
from os import path
import user_interface
import user_inputs
from logger import LOG

STUDENT_FIELDS = ['student_id', 'name', 'patronym',
                  'surname', 'birthdate', 'phone', 'class']


def db_connect(file_name):
    'Подключается к базе данных и возвращает объект Connect'

    file = f'{file_name}.db'
    try:
        con = sl.connect(file)
        return con
    except sl.Error as e:
        # TODO записать в log вместо консоли перед продакшеном
        print(f'Ошибка: {e}')


def execute_query(con, query, data=None):
    '''Выполняет запрос к базе.
    Принимает sql запрос и кортеж значений для подстановки в VALUE(?,?) для исключения возможности SQL-инъекции.
    Возвращает объект Cursor.'''

    with con:
        try:
            if data:
                if isinstance(data, list):
                    res = con.executemany(query, data)
                elif isinstance(data, tuple):
                    res = con.execute(query, data)
            else:
                res = con.execute(query)
            return res
        except sl.Error as e:
            # TODO записать в log вместо консоли перед продакшеном
            print(f'Ошибка: {e}')


@LOG
def create_db(file_name):
    'Создаёт базу данных'

    table_name = 'students'
    sql_query = f'''CREATE TABLE IF NOT EXISTS '{table_name}'(
                 student_id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 patronym TEXT NOT NULL,
                 surname TEXT NOT NULL,
                 birthdate TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 class TEXT NOT NULL);'''
    execute_query(db_connect(file_name), sql_query)


@LOG
def get_db(file_name):
    'Возвращает все записи в таблице'

    sql_query = "SELECT * FROM students"
    res = execute_query(db_connect(file_name), sql_query)
    return res


@LOG
def add_student(contact, file_name):
    'Добавляет нового студента'

    sql_query = "INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?)"
    data = [tuple(contact)]
    return execute_query(db_connect(file_name), sql_query, data)


@LOG
def remove_student(s_id, file_name):
    'Удаляет студента'

    sql_query = f"DELETE FROM students WHERE student_id=?"
    data = (str(s_id),)
    execute_query(db_connect(file_name), sql_query, data)


@LOG
def check_file_exist(file_name):
    'Проверяет наличие файла по указанному пути'

    if not path.exists(f'{file_name}.db'):
        if user_inputs.ask_fill_input(0, file_name):
            create_db(file_name)
            return True
        else:
            return False
    else:
        return True


@LOG
def check_table_exist(file_name, table_name):
    'Проверяет, существует ли таблица в базе'

    sql_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    check = execute_query(db_connect(file_name), sql_query).fetchall()
    if not check:
        user_interface.print_errors(1, file_name)
        create_db(file_name)
        user_interface.print_notifications(0)
    return True


@LOG
def search_record(field_ind, query, file_name, compliance=False):
    'Ищет запись в базе по параметру'

    field = STUDENT_FIELDS[int(field_ind) - 1]
    if compliance:
        sql_query = f"SELECT * FROM students WHERE {field}='{query}'; "
    else:
        sql_query = f"SELECT * FROM students WHERE {field} LIKE '%{query}%'; "
    return execute_query(db_connect(file_name), sql_query).fetchall()


@LOG
def check_id(r_id, file_name):
    'Проверяет, есть ли запись в введенным id в базе'

    sql_query = f"SELECT * FROM students WHERE student_id='{r_id}'; "
    return execute_query(db_connect(file_name), sql_query).fetchall()


@LOG
def get_updates(r_id, field_ind, value, file_name):
    'Формирует исправленную запись'

    record = list(*search_record(1, r_id, file_name, compliance=True))
    record[int(field_ind)] = f'>>> {value} <<<'
    return record


@LOG
def change_field(r_id, field_ind, value, file_name):
    'Меняет поле записи'

    field = STUDENT_FIELDS[int(field_ind)]
    sql_query = f"UPDATE students SET {field} = '{value}' WHERE student_id={r_id}"
    execute_query(db_connect(file_name), sql_query)
