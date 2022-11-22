import user_interface

FLAG = {'yes': ['y', 'ye', 'yes', '', 'да', 'д'],
        'no': ['n', 'no', 'not', 'н', 'не', 'нет']}


def choice_file_input():
    """
    Ввод файла для использования
    """
    return input(user_interface.choice_file_print())


def confirm_choice(text):
    """
    Ввод подтверждения действия
    """
    user_choice = input(f"{text}\n: ").lower()
    if user_choice in FLAG['yes']:
        return True
    elif user_choice in FLAG['no']:
        return False
    else:
        user_interface.print_errors(2)
        return False


def ask_fill_input(code):
    """
    Возврат подтверждения действия
    """
    return confirm_choice(user_interface.errors(code))


def get_data_input(table):
    """
    Возврат полученных данных
    """
    headers = {
        'students': ['ученика', user_interface.HEADERS['students'][1:]],
        'classes': ['класса', user_interface.HEADERS['classes']]
    }
    return tuple(map(lambda x: input(f'{x} {headers[table][0]}: '), headers[table][1]))


def get_random_input(text):
    """
    Возврат данных от пользователя
    """
    return input(f'Введите {text}: ')
