from tabulate import tabulate

ERRORS = {0: 'База {0}.db не найдена.\n'
             'Создать Д/Н?\n'
             '-: ',
          1: 'База {0}.db не заполнена.\n'
             'Заполняем базу...',
          2: 'Неверный ввод.'}

NOTIFICATIONS = {0: 'База успешно записана в файл.'}

HEADERS = {'students': ['id', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Телефон', 'Класс'],
           'classes': ['Номер', 'Кабинет', 'Руководитель']}


def menu():
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Удалить запись из базы\n'
          '4. Найти запись в базе\n'
          '0. Выйти из приложения')


def choice_file_print():
    return '''
Введите название база или путь к файлу с базой.
Или нажмите "Enter" для базы по умолчанию - school.db
-: '''


def new_line():
    print()


def print_message(text):
    print(f'\n~~ {text} ~~', end='\n\n')


def errors(code, file_name):
    return ERRORS[code].format(file_name)


def print_errors(code, file_name):
    print(ERRORS[code].format(file_name))


def show_table(data, table):
    headers = HEADERS['students'][1:] + HEADERS['classes'][1:] if table == 'unified' else HEADERS[table]
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))


def print_notifications(code):
    print(NOTIFICATIONS[code])


def fields_menu(text, table, start=0):
    fields = f'Выберите поле для {text}\n'
    for i, field in enumerate(HEADERS[table][start:]):
        fields += f'{i + 1}. {field}\n'
    print(f'{fields}')


def change_menu():
    print('''Введите действие:
    1. Изменить запись
    2. Удалить запись
    0. Выйти в главное меню
    ''')


def show_record(record, table, start=0):
    'Отображает запись'

    if len(record) < len(HEADERS[table]):
        start = 1
    result = list(zip(HEADERS[table][start:], record))
    print(tabulate(result, tablefmt='fancy_grid'))


def print_tables(unified=False):
    last_line = '3. Общая таблица' if unified else ''
    print(f'''Выберите таблицу:
    1. Таблица учеников
    2. Таблица классов
    {last_line}
    ''')
