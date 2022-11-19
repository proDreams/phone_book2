import user_interface
import user_inputs
import model

FILEPATH = ''


def run():
    running = True
    while running:
        user_interface.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('Выберите действие: ')
            match user_choice:
                case '1':
                    db = model.get_db(FILEPATH)
                    user_interface.show_database(db)
                case '2':
                    f_name = input('Введите имя ученика: ')
                    l_name = input('Введите отчество ученика: ')
                    s_name = input('Введите фамилию ученика: ')
                    dob = input('Введите дату рождения: ')
                    phone = input('Введите телефон: ')
                    class_num = input('Введите номер класса: ')
                    contact = [f_name, l_name, s_name, dob, phone, class_num]
                    model.add_student(contact, FILEPATH)
                case '3':
                    find_id = input('Введите id ученика для удаления: ')
                    model.remove_student(find_id, FILEPATH)
                case 'X':
                    running = False


def start():
    global FILEPATH
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
