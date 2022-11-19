import sqlite3


def get_db():
    db = sqlite3.connect('student.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows


def add_student(contact):
    db = sqlite3.connect('student.db')
    db.execute('CREATE TABLE IF NOT EXISTS {}('
               'student_id INTEGER PRIMARY KEY, '
               'name TEXT NOT NULL, '
               'patronym TEXT NOT NULL, '
               'surname TEXT NOT NULL, '
               'birthdate TEXT NOT NULL, '
               'phone TEXT NOT NULL, '
               'grade TEXT NOT NULL)'.format('students'))
    cur = db.cursor()
    cur.execute("INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?)", tuple(value for value in contact))
    db.commit()
    db.close()


def remove_student(id):
    db = sqlite3.connect('student.db')
    cur = db.cursor()
    cur.execute(f"DELETE FROM students WHERE student_id={id}")
    db.commit()
    db.close()
