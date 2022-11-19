from tabulate import tabulate

ERRORS = {0: 'База {0}.db не найдена.\n'
             'Создать Д/Н?\n'
             '-: ',
          1: 'База {0}.db не заполнена.\n'
             'Заполняем базу...',
          2: 'Неверный ввод.'}

NOTIFICATIONS = {0: 'База успешно записана в файл.'}


def menu():
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Удалить запись из базы\n'
          'X. Выйти из приложения')


def choice_file_print():
    return '''
Введите название база или путь к файлу с базой.
Или нажмите "Enter" для базы по умолчанию - school.db
-: '''


def new_line():
    print()


def hello_message():
    print('Добро пожаловать в менеджер баз данных!')


def errors(code, file_name):
    return ERRORS[code].format(file_name)


def print_errors(code):
    print(ERRORS[code])


def show_database(db):
    headers = ['id', 'Имя', 'Отчество', 'Фамилия', 'Дата рождения', 'Телефон', 'Класс']
    print(tabulate(db, headers=headers, tablefmt='fancy_grid'))


def print_notifications(code):
    print(NOTIFICATIONS[code])
