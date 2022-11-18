from tabulate import tabulate


def menu():
    print('Выберите действие:\n'
          '1. Отобразить базу\n'
          '2. Добавить запись в базу\n'
          '3. Удалить запись из базы\n'
          'X. Выйти из приложения')


def show_database(db):
    headers = ['id', 'Имя', 'Отчество', 'Фамилия', 'Дата рождения', 'Телефон', 'Класс']
    print(tabulate(db, headers=headers, tablefmt='fancy_grid'))
