import user_interface as ui
import user_inputs
import model as m

DB_FILENAME = 'school.db'
con = m.db_connect(DB_FILENAME)


def choose_table(unified=False):
    """
    Позволяет пользователю выбрать таблицу
    """

    choices = ['1', '2', '3'] if unified else ['1', '2']
    table_choice = ''
    while table_choice not in choices:
        ui.print_tables(unified=unified)
        table_choice = input(': ')
        if table_choice not in choices:
            ui.print_message('Неверный ввод')
    return m.TABLES[table_choice]


def run():
    ui.print_message('Добро пожаловать базу учеников!')

    for table in ['students', 'classes']:
        if not m.check_table_exist(con, table):
            m.create_table(con, table)

    while True:
        ui.new_line()
        ui.menu()
        user_choice = input(': ')
        match user_choice:
            case '1':
                table = choose_table(unified=True)
                data = m.get_data(con, table)
                ui.show_table(data, table)

            case '2':
                table = choose_table()
                ui.print_message('Введите данные')
                record = user_inputs.get_data_input(table)
                ui.show_record(record, table)
                if user_inputs.confirm_choice('Внести эту запись Д/Н?'):
                    m.add_record(table, record, con)
                    ui.print_message('Запись успешно внесена')
                else:
                    ui.print_message('Запись не внесена')

            case '3':
                table = choose_table()
                find_id = user_inputs.get_random_input(
                    'id нужной записи')
                if not m.check_id(find_id, table, con):
                    ui.print_message(
                        f'Запись c id "{find_id}" отсутствует')
                else:
                    record = m.search_record(
                        '1', find_id, table, con, compliance=True)
                    ui.show_record(*record, table)
                    if user_inputs.confirm_choice('Вы действительно хотите удалить данную запись Д/Н?'):
                        m.remove_record(
                            find_id, table, con)
                        ui.print_message('Запись успешно удалена')
                    else:
                        ui.print_message(
                            'Удаление записи отменено')

            case '4':
                table = choose_table()
                ui.fields_menu('поиска', table)
                search_choice = input(': ')
                query = user_inputs.get_random_input('запрос')
                records = m.search_record(
                    search_choice, query, table, con)
                if records:
                    ui.print_message(
                        'Найдены следующие записи:')
                    ui.show_table(records, table)
                    if len(records) > 1:
                        find_id = user_inputs.get_random_input(
                            'id нужной записи')
                    else:
                        find_id = records[0][0]
                    if not m.check_id(find_id, table, con):
                        ui.print_message(
                            f'Запись c id "{find_id}" отсутствует')
                    else:
                        inner_menu = True
                        while inner_menu:
                            ui.change_menu()
                            change_choice = input(': ')
                            match change_choice:
                                case '1':
                                    ui.fields_menu(
                                        'изменения', table, 1)
                                    field_choice = input(': ')
                                    new_value = user_inputs.get_random_input(
                                        f'новое значение поля {field_choice}')
                                    updated_record = m.get_updates(
                                        find_id, field_choice, new_value, table, con)
                                    ui.show_record(
                                        updated_record, table)
                                    if user_inputs.confirm_choice('Внести эти изменения?'):
                                        m.change_field(
                                            find_id, field_choice, new_value, table, con)
                                        ui.print_message(
                                            'Изменения успешно внесены')
                                    else:
                                        ui.print_message(
                                            'Изменения не внесены')
                                    inner_menu = False
                                case '2':
                                    record = m.search_record(
                                        '1', find_id, table, con, compliance=True)
                                    ui.show_record(*record, table)
                                    if user_inputs.confirm_choice('Вы действительно хотите удалить данную запись?'):
                                        m.remove_record(
                                            find_id, table, con)
                                        ui.print_message(
                                            'Запись успешно удалена')
                                    else:
                                        ui.print_message(
                                            'Удаление записи отменено')
                                    inner_menu = False
                                case '0':
                                    inner_menu = False
                                case _:
                                    ui.print_message(
                                        'Неверный ввод')
                else:
                    ui.print_message(
                        f'Записи по запросу "{query}" отсутствуют')
            case '0':
                con.close()
                ui.print_message(f'Бай Бай!')
                break
            case _:
                ui.print_message('Неверный ввод')
