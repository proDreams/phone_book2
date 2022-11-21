from tabulate import tabulate

ERRORS = {2: 'Неверный ввод.'}

NOTIFICATIONS = {0: 'База успешно записана в файл.'}

HEADERS = {'students': ['id', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Телефон', 'Класс'],
           'classes': ['Номер', 'Кабинет', 'Руководитель']}


def menu():
    """
    Вывод меню программы
    """
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Удалить запись из базы\n'
          '4. Найти запись в базе\n'
          '0. Выйти из приложения')


def choice_file_print():
    """
    Возврат сообщения о выборе файла
    """
    return '''
Введите название база или путь к файлу с базой.
Или нажмите "Enter" для базы по умолчанию - school.db
: '''


def new_line():
    """
    Вывод пустой строки
    """
    print()


def print_message(text):
    """
    Вывод сообщения
    """
    print(f'\n~~ {text} ~~', end='\n\n')


def errors(code):
    """
    Возврат ошибки
    """
    return ERRORS[code]


def print_errors(code):
    """
    Вывод ошибки
    """
    print(ERRORS[code])


def show_table(data, table):
    """
    Вывод таблицы
    """
    headers = HEADERS['students'][1:] + HEADERS['classes'][1:] if table == 'unified' else HEADERS[table]
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))


def print_notifications(code):
    """
    Вывод оповещения
    """
    print(NOTIFICATIONS[code])


def fields_menu(text, table, start=0):
    """
    Вывод полей таблицы
    """
    fields = f'Выберите поле для {text}\n'
    for i, field in enumerate(HEADERS[table][start:]):
        fields += f'{i + 1}. {field}\n'
    print(f'{fields}')


def change_menu():
    """
    Вывод меню действий над записью
    """
    print('''Введите действие:
    1. Изменить запись
    2. Удалить запись
    0. Выйти в главное меню
    ''')


def show_record(record, table, start=0):
    """
    Вывод записи из таблицы
    """

    if len(record) < len(HEADERS[table]):
        start = 1
    result = list(zip(HEADERS[table][start:], record))
    print(tabulate(result, tablefmt='fancy_grid'))


def print_tables(unified=False):
    """
    Вывод выбора таблицы
    """
    last_line = '3. Общая таблица' if unified else ''
    print(f'''Выберите таблицу:
    1. Таблица учеников
    2. Таблица классов
    {last_line}
    ''')
