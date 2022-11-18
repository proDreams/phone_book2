def get_db():

    with open('file.csv', 'r', encoding='utf-8') as file:
        result = []
        for i in file:
            result.append(i.rstrip().split(','))
    return result

def add_student(contact):
    with open('file.csv', 'a', encoding='utf-8') as file:
        line = ','.join(contact)
        file.write(line)
        file.write('\n')