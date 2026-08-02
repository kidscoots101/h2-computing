
import flask
from flask import render_template

app = flask.Flask(__name__)

def readData(file):
    with open(file, 'r') as data:
        data = data.read().strip()

    pixels = []
    for i in range(0, len(data), 3): # splits bits into groups of 3 (for easy reference)
        pixels.append(data[i:i+3])

    return pixels

@app.route('/')
def home():
    colours = { # binary values of colour options
        "000": "red",
        "001": "white",
        "010": "yellow",
        "011": "blue",
        "100": "black",
        "110": "green"
    }
    data = readData('decompressedimage.txt')

    grid = [] # converts into a grid of 9x9

    for i in range(9):
        grid.append(data[0:9])
        data = data[9:]

    for row in range(len(grid)):
        for i in range(len(grid[0])):
            grid[row][i] = colours[grid[row][i]] # converts from binary to colour values
    
    return render_template('TASK4_3_25S22_Caleb.html', image=grid)

app.run(port=12345)
