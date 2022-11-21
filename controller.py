import user_interface
import user_inputs
import model

FILEPATH = ''


def choose_table(unified=False):
    """
    Позволяет пользователю выбрать таблицу
    """

    choices = ['1', '2', '3'] if unified else ['1', '2']
    table_choice = ''
    while table_choice not in choices:
        user_interface.print_tables(unified=unified)
        table_choice = input(': ')
        if table_choice not in choices:
            user_interface.print_message('Неверный ввод')
    return model.TABLES[table_choice]


def run():
    global FILEPATH
    user_interface.print_message('Добро пожаловать в менеджер баз данных!')

    FILEPATH = user_inputs.choice_file_input()
    if FILEPATH == '':
        FILEPATH = 'school'

    for table in ['students', 'classes']:
        if not model.check_table_exist(FILEPATH, table):
            model.create_table(FILEPATH, table)

    running = True
    while running:
        user_interface.new_line()
        user_interface.menu()
        user_choice = input(': ')
        match user_choice:
            case '1':
                table = choose_table(unified=True)
                data = model.get_data(FILEPATH, table)
                user_interface.show_table(data, table)
            case '2':
                table = choose_table()
                user_interface.print_message('Введите данные')
                record = user_inputs.get_data_input(table)
                user_interface.show_record(record, table)
                if user_inputs.confirm_choice('Внести эту запись Д/Н?'):
                    model.add_record(table, record, FILEPATH)
                    user_interface.print_message('Запись успешно внесена')
                else:
                    user_interface.print_message('Запись не внесена')
            case '3':
                table = choose_table()
                find_id = user_inputs.get_random_input(
                    'id нужной записи')
                if not model.check_id(find_id, table, FILEPATH):
                    user_interface.print_message(
                        f'Запись c id "{find_id}" отсутствует')
                else:
                    record = model.search_record(
                        '1', find_id, table, FILEPATH, compliance=True)
                    user_interface.show_record(*record, table)
                    if user_inputs.confirm_choice('Вы действительно хотите удалить данную запись Д/Н?'):
                        model.remove_record(
                            find_id, table, FILEPATH)
                        user_interface.print_message('Запись успешно удалена')
                    else:
                        user_interface.print_message(
                            'Удаление записи отменено')
            case '4':
                table = choose_table()
                user_interface.fields_menu('поиска', table)
                search_choice = input(': ')
                query = user_inputs.get_random_input('запрос')
                records = model.search_record(
                    search_choice, query, table, FILEPATH)
                if records:
                    user_interface.print_message(
                        'Найдены следующие записи:')
                    user_interface.show_table(records, table)
                    if len(records) > 1:
                        find_id = user_inputs.get_random_input(
                            'id нужной записи')
                    else:
                        find_id = records[0][0]
                    if not model.check_id(find_id, table, FILEPATH):
                        user_interface.print_message(
                            f'Запись c id "{find_id}" отсутствует')
                    else:
                        inner_menu = True
                        while inner_menu:
                            user_interface.change_menu()
                            change_choice = input(': ')
                            match change_choice:
                                case '1':
                                    user_interface.fields_menu(
                                        'изменения', table, 1)
                                    field_choice = input(': ')
                                    new_value = user_inputs.get_random_input(
                                        f'новое значение поля {field_choice}')
                                    updated_record = model.get_updates(
                                        find_id, field_choice, new_value, table, FILEPATH)
                                    user_interface.show_record(
                                        updated_record, table)
                                    if user_inputs.confirm_choice('Внести эти изменения?'):
                                        model.change_field(
                                            find_id, field_choice, new_value, table, FILEPATH)
                                        user_interface.print_message(
                                            'Изменения успешно внесены')
                                    else:
                                        user_interface.print_message(
                                            'Изменения не внесены')
                                    inner_menu = False
                                case '2':
                                    record = model.search_record(
                                        '1', find_id, table, FILEPATH, compliance=True)
                                    user_interface.show_record(*record, table)
                                    if user_inputs.confirm_choice('Вы действительно хотите удалить данную запись?'):
                                        model.remove_record(
                                            find_id, table, FILEPATH)
                                        user_interface.print_message(
                                            'Запись успешно удалена')
                                    else:
                                        user_interface.print_message(
                                            'Удаление записи отменено')
                                    inner_menu = False
                                case '0':
                                    inner_menu = False
                                case _:
                                    user_interface.print_message(
                                        'Неверный ввод')
                else:
                    user_interface.print_message(
                        f'Записи по запросу "{query}" отсутствуют')
            case '0':
                running = False
            case _:
                user_interface.print_message('Неверный ввод')
