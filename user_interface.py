from tabulate import tabulate

ERRORS = {0: 'База не найдена.\n'
             'Создать?',
          1: 'База не заполнена.\n'
             'Заполнить?',
          2: 'Неверный ввод.'}

NOTIFICATIONS = {0: 'База успешно записана в файл.'}


def menu():
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Удалить запись из базы\n'
          'X. Выйти из приложения')


def choice_file_print():
    print('- Введите название база или путь к файлу с базой\n'
          '- Или нажмите "Enter" для базы по умолчанию.\n')


def errors(code):
    print(ERRORS[code])


def show_database(db):
    headers = ['id', 'Имя', 'Отчество', 'Фамилия', 'Дата рождения', 'Телефон', 'Класс']
    print(tabulate(db, headers=headers, tablefmt='fancy_grid'))


def print_notifications(code):
    print(NOTIFICATIONS[code])
