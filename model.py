def get_phonebook():

    with open('file.csv', 'r', encoding='utf-8') as file:
        result = file.read().split(',')
    return result
