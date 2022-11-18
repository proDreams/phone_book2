def menu():
    print('Выберите действие:\n'
          '1. Отобразить книгу\n'
          '2. Добавить строку в книгу\n'
          'X. Выйти из приложения')


def show_database(db):
    for i in db:
        print(*i)

