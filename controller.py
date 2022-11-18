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
                    phonebook = model.get_phonebook()
                    view.show_book(phonebook)
                case '2':
                    name = input('Введите имя: ')
                    phone = input('Введите телефон: ')
                    contact = [name, phone]
                    model.add_contact(contact)
                case 'X':
                    running = False