
# Task 4.1

import flask, sqlite3
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('TASK4_1_Caleb_25S22.html')

app.run(port=12345)