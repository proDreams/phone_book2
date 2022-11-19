import user_interface

FLAG = {'yes': ['y', 'ye', 'yes', ''],
        'no': ['n', 'no', 'not']}


def choice_file_input():
    user_interface.choice_file_print()
    return input()


def ask_fill_input(code):
    user_interface.errors(code)
    user_choice = input()
    if user_choice in FLAG['yes']:
        return True
    elif user_choice in FLAG['no']:
        return False
    else:
        user_interface.errors(2)
        return False
