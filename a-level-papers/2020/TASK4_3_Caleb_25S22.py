# Task 4.3

import flask, sqlite3
from flask import render_template

app = flask.Flask(__name__)

conn = sqlite3.connect("school.db")
cursor = conn.execute("SELECT ScreenName FROM People")
rows = cursor.fetchall()

screen_names = []
for row in rows:
    screen_names.append(row)

with open('people.txt', 'r') as file:
    file = file.read().strip().split("\n") # John Tan,2000-06-01,Person
    data = []
    for i in range(len(file)):
        file[i] = file[i].split(',')
        data.append([file[i][0], screen_names[i][0], file[i][2]])

@app.route("/")
def home():
    return render_template('TASK4_3_Caleb_25S22.html', data=data)

app.run(port=12345)
conn.close()