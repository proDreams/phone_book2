import sqlite3 as sl
import user_interface
import user_inputs
from logger import LOG

TABLES = {
    '1': 'students',
    '2': 'classes',
    '3': 'unified'
}

FIELDS = {
    'students': ['id', 'surname', 'name', 'patronym',
                 'birthdate', 'phone', 'class'],
    'classes': ['id', 'room', 'teacher']
}

COLUMNS_SQL = {
    'students': """id INTEGER PRIMARY KEY,
                 surname TEXT NOT NULL,
                 name TEXT NOT NULL,
                 patronym TEXT NOT NULL,
                 birthdate TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 class TEXT NOT NULL""",

    'classes': """ id TEXT PRIMARY KEY,
                 room TEXT NOT NULL,
                 teacher TEXT NOT NULL"""
}

con = None


def db_connect(file):
    """
    Подключается к базе данных и возвращает объект Connect
    """

    global con

    try:
        con = sl.connect(file)
    except sl.Error as e:
        # TODO записать в log вместо консоли перед продакшеном
        print(f'Ошибка: {e}')


def execute_query(query, data=None):
    """
    Выполняет запрос к базе.
    Принимает sql запрос и кортеж значений для подстановки в VALUE(?,?) для исключения возможности SQL-инъекции.
    Возвращает объект Cursor.
    """

    try:
        with con:
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
        if str(e) == "UNIQUE constraint failed: classes.id":
            user_interface.print_message('Такой класс уже есть в базе')
        else:
            print(f'Ошибка: {e}')


@LOG
def create_table(table_name='students'):
    """
    Создаёт таблицу в базе данных
    """
    columns = COLUMNS_SQL[table_name]
    sql_query = f'''CREATE TABLE IF NOT EXISTS '{table_name}'(
                 {columns});'''
    execute_query(sql_query)


@LOG
def get_data(table):
    """
    Возвращает все записи в таблице
    """

    if table == 'students' or table == 'unified':
        order_by = 'surname'
    elif table == 'classes':
        order_by = 'id'
    sql_query = "SELECT * FROM {table} ORDER BY {order_by}".format(
        table=table, order_by=order_by)
    if table == 'unified':
        sql_query = """SELECT l.surname, l.name, l.patronym, l.birthdate, l.phone, l.class, r.room, r.teacher
                        FROM students l
                        LEFT JOIN classes r
                        ON l.class = r.id
                        ORDER BY {order_by};""".format(order_by=order_by)
    res = execute_query(sql_query)
    return res


@LOG
def add_record(table, data):
    """
    Добавляет новую запись
    """

    columns = {
        'students': 'NULL, ?, ?, ?, ?, ?, ?',
        'classes': '?, ?, ?'
    }
    sql_query = f"INSERT INTO {table} VALUES({columns[table]})"
    return execute_query(sql_query, data)


@LOG
def remove_record(s_id, table):
    """
    Удаляет запись
    """

    sql_query = f"DELETE FROM {table} WHERE id=?"
    data = (str(s_id),)
    execute_query(sql_query, data)


@LOG
def check_table_exist(table_name):
    """
    Проверяет, существует ли таблица в базе
    """
    data = (table_name,)
    sql_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
    return execute_query(sql_query, data).fetchall()


@LOG
def search_record(field_ind, query, table, compliance=False):
    """
    Ищет запись в базе по параметру
    """

    field = FIELDS[table][int(field_ind) - 1]
    if compliance:
        sql_query = f"SELECT * FROM {table} WHERE {field}='{query}'; "
    else:
        sql_query = f"SELECT * FROM {table} WHERE {field} LIKE '%{query}%'; "
    return execute_query(sql_query).fetchall()


@LOG
def check_id(r_id, table):
    """
    Проверяет, есть ли запись в введенным id в базе
    """

    data = (str(r_id),)
    sql_query = f"SELECT * FROM {table} WHERE id=?; "
    return execute_query(sql_query, data).fetchall()


@LOG
def get_updates(r_id, field_ind, value, table):
    """
    Формирует исправленную запись
    """

    record = list(*search_record(1, r_id, table, compliance=True))
    record[int(field_ind)] = f'>>> {value} <<<'
    return record


@LOG
def change_field(r_id, field_ind, value, table):
    """
    Меняет поле записи
    """

    data = (str(value), str(r_id),)
    field = FIELDS[table][int(field_ind)]
    sql_query = f"UPDATE {table} SET {field} = ? WHERE id=?"
    execute_query(sql_query, data)
