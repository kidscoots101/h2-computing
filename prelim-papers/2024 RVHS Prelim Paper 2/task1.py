import sqlite3
import csv
from flask import Flask, render_template

con = sqlite3.connect("cu_booking.db")
cursor = con.cursor()
"""
#Task 1.1

cursor.execute("CREATE TABLE student(id TEXT PRIMARY KEY UNIQUE, name TEXT, contact INTEGER)")
cursor.execute("CREATE TABLE cubicle(cubicle_no TEXT PRIMARY KEY, maintenance TEXT)")
cursor.execute("CREATE TABLE booking(date TEXT, cubicle_no TEXT REFERENCES cubicle(cubicle_no), student_id REFERENCES student(id))")

#Task 1.2

with open("student.csv", "r") as f:
    s = list(csv.reader(f))[1::]
    for student in s:
        print(student)
        cursor.execute(f"INSERT INTO student(id, name, contact) VALUES(?, ?, ?)", student)


with open("cubicle.csv", "r") as f:
    c = list(csv.reader(f))[1::]
    for cubicle in c:
        cursor.execute(f"INSERT INTO cubicle(cubicle_no, maintenance) VALUES(?, ?)", cubicle)

with open("booking.csv", "r") as f:
    b = list(csv.reader(f))[1::]
    for booking in b:
        cursor.execute(f"INSERT INTO booking(date, cubicle_no, student_id) VALUES(?, ?, ?)", booking)


#Task 1.3
cursor.execute("UPDATE cubicle SET maintenance='0' WHERE cubicle_no='c01'")


#Task 1.4
available = list(cursor.execute("SELECT cubicle_no FROM booking WHERE date='17112024'"))
for i in available:
    print(i[0])

con.commit()
con.close()

"""
#Task 1.4
app = Flask(__name__)

@app.route("/available/<date>")
def date(date):
    con = sqlite3.connect("cu_booking.db")
    cursor = con.cursor()
    cubicles = []
    available = list(cursor.execute(f"SELECT cubicle_no FROM booking WHERE date='{date}'"))
    for i in available:
        cubicles.append(list(cursor.execute(f"SELECT * FROM cubicle WHERE cubicle_no='{i[0]}'"))[0])
    con.close()
    return render_template("date.html", date=date, cubicles=cubicles)
app.run(debug=True)


con.close()
