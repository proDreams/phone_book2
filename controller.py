import user_interface
import user_inputs
import model

FILEPATH = ''


def run():
    running = True
    while running:
        user_interface.new_line()
        user_interface.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('-: ').lower()
            match user_choice:
                case '1':
                    db = model.get_db(FILEPATH)
                    user_interface.show_database(db)
                case '2':
                    contact = user_inputs.get_student_input()
                    model.add_student(contact, FILEPATH)
                case '3':
                    find_id = input('Введите id ученика для удаления: ')
                    model.remove_student(find_id, FILEPATH)
                case '4':
                    user_interface.search_menu()
                    search_choice = input('-: ').lower()

                case 'x':
                    running = False


def start():
    global FILEPATH
    user_interface.hello_message()
    while True:
        FILEPATH = user_inputs.choice_file_input()
        if FILEPATH == '':
            FILEPATH = 'school'
            model.create_db(FILEPATH)
            break
        elif model.check_file_exist(FILEPATH):
            break
    model.check_table_exist(FILEPATH)
    run()
