from tabulate import tabulate

ERRORS = {0: 'База {0}.db не найдена.\n'
             'Создать Д/Н?\n'
             '-: ',
          1: 'База {0}.db не заполнена.\n'
             'Заполняем базу...',
          2: 'Неверный ввод.'}

NOTIFICATIONS = {0: 'База успешно записана в файл.'}

STUDENT_HEADERS = ['id', 'Имя', 'Отчество', 'Фамилия', 'Дата рождения', 'Телефон', 'Класс']


def menu():
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Найти запись в базе\n'
          '0. Выйти из приложения')


def choice_file_print():
    return '''
Введите название база или путь к файлу с базой.
Или нажмите "Enter" для базы по умолчанию - school.db
-: '''


def new_line():
    print()


def print_message(text):
    print(f'~~ {text} ~~', end='\n\n')


def errors(code, file_name):
    return ERRORS[code].format(file_name)


def print_errors(code):
    print(ERRORS[code])


def show_database(db):
    headers = STUDENT_HEADERS
    print(tabulate(db, headers=headers, tablefmt='fancy_grid'))


def print_notifications(code):
    print(NOTIFICATIONS[code])


def fields_menu(text, start=0):
    fields = f'Выберите поле для {text}\n'
    for i, field in enumerate(STUDENT_HEADERS[start:]):
        fields += f'{i + 1}. {field}\n'
    print(f'{fields}')


def change_menu():
    print('''Введите действие:
    1. Изменить запись
    2. Удалить запись
    0. Выйти в главное меню
    ''')


def show_record(record):
    result = list(zip(STUDENT_HEADERS, record))
    print(tabulate(result, tablefmt='fancy_grid'))
