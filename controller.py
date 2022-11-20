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
                    user_interface.print_message('Введите данные')
                    contact = user_inputs.get_student_input()
                    model.add_student(contact, FILEPATH)
                case '3':
                    user_interface.fields_menu('поиска')
                    search_choice = input('-: ').lower()
                    query = user_inputs.get_random_input('запрос')
                    records = model.search_record(
                        search_choice, query, FILEPATH)
                    if records:
                        user_interface.print_message(
                            'Найдены следующие записи:')
                        user_interface.show_database(records)
                        if len(records) > 1:
                            find_id = user_inputs.get_random_input(
                                'id нужной записи')
                        else:
                            find_id = records[0][0]
                        if not model.check_id(find_id, FILEPATH):
                            user_interface.print_message(
                                f'Запись c id "{find_id}" отсутствует')
                        else:
                            inner_menu = True
                            while inner_menu:
                                user_interface.change_menu()
                                change_choice = input('-: ').lower()
                                match change_choice:
                                    case '1':
                                        user_interface.fields_menu(
                                            'изменения', 1)
                                        field_choice = input('-: ').lower()
                                        new_value = user_inputs.get_random_input(
                                            f'новое значение поля {field_choice}')
                                        updated_record = model.get_updates(
                                            find_id, field_choice, new_value, FILEPATH)
                                        user_interface.show_record(
                                            updated_record)
                                        if user_inputs.confirm_choice('Внести эти изменения?'):
                                            model.change_field(
                                                find_id, field_choice, new_value, FILEPATH)
                                        inner_menu = False
                                    case '2':
                                        record = model.search_record(
                                            '1', find_id, FILEPATH, compliance=True)
                                        user_interface.show_record(*record)
                                        if user_inputs.confirm_choice('Вы действительно хотите удалить данную запись?'):
                                            model.remove_student(
                                                find_id, FILEPATH)
                                        inner_menu = False
                                    case '0':
                                        inner_menu = False
                    else:
                        user_interface.print_message(
                            f'Записи по запросу "{query}" отсутствуют')
                case '0':
                    running = False


def start():
    global FILEPATH
    user_interface.print_message('Добро пожаловать в менеджер баз данных!')
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
