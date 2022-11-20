import user_interface

FLAG = {'yes': ['y', 'ye', 'yes', '', 'да', 'д'],
        'no': ['n', 'no', 'not', 'н', 'не', 'нет']}


def choice_file_input():
    return input(user_interface.choice_file_print())


def confirm_choice(text):
    user_choice = input(f"{text}\n-: ").lower()
    if user_choice in FLAG['yes']:
        return True
    elif user_choice in FLAG['no']:
        return False
    else:
        user_interface.print_errors(2)
        return False


def ask_fill_input(code, file_name):
    return confirm_choice(user_interface.errors(code, file_name))
    # user_choice = input(user_interface.errors(code, file_name)).lower()
    # if user_choice in FLAG['yes']:
    #     return True
    # elif user_choice in FLAG['no']:
    #     return False
    # else:
    #     user_interface.print_errors(2)
    #     return False


def get_student_input():
    return map(lambda x: input(f'{x} ученика: '), user_interface.STUDENT_HEADERS[1:])


def get_random_input(text):
    return input(f'Введите {text}: ')
