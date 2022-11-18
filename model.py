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

def remove_student(id):
    full_db = get_db()
    new_db = []
    for row in full_db:
        if row[0] != id:
            new_db.append(row)

    with open('file.csv', 'w', encoding='utf-8') as file:
        for i in new_db:
            file.write(','.join(i))
            file.write('\n')

