import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, rollno TEXT, email TEXT, gender TEXT, class TEXT, contact TEXT, dob TEXT, address TEXT)")
    conn.commit()
    conn.close()

def insert(name, rollno, email, gender, student_class, contact, dob, address):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, rollno, email, gender, student_class, contact, dob, address))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name="", rollno="", email="", gender="", student_class="", contact="", dob="", address=""):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR rollno=? OR email=? OR gender=? OR class=? OR contact=? OR dob=? OR address=?", (name, rollno, email, gender, student_class, contact, dob, address))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, rollno, email, gender, student_class, contact, dob, address):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?, rollno=?, email=?, gender=?, class=?, contact=?, dob=?, address=? WHERE id=?", (name, rollno, email, gender, student_class, contact, dob, address, id))
    conn.commit()
    conn.close()

connect()
