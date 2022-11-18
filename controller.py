import view
import model


def run():
    running = True
    while running:
        view.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('Выберите действие: ')
            match user_choice:
                case '1':
                    db = model.get_db()
                    view.show_database(db)
                case '2':
                    s_id = input('Введите id ученика: ')
                    f_name = input('Введите имя ученика: ')
                    l_name = input('Введите фамилию ученика: ')
                    s_name = input('Введите отчество ученика: ')
                    dob = input('Введите дату рождения: ')
                    phone = input('Введите телефон: ')
                    class_num = input('Введите номер класса: ')
                    contact = [s_id, f_name, l_name, s_name, dob, phone, class_num]
                    model.add_student(contact)
                case '3':
                    find_id = input('Введите id ученика для удаления: ')
                    model.remove_student(find_id)
                case 'X':
                    running = False