from flask import Flask
import pandas as pd
import password_generator as pg

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = '<a href="/generate_password">Generate password</a><br>'
    html += '<a href="/calculate_average">Calculate average</a>'
    return html


@app.route('/generate_password')
def generate_password():
    password = pg.generate_password()
    return password


@app.route('/calculate_average')
def calculate_average():
    data_frame = pd.read_csv('hw.csv', sep=', ')
    height = round(data_frame["Height(Inches)"].mean(), 2)
    weight = round(data_frame["Weight(Pounds)"].mean(), 2)
    return f'The average height is {height} and the average weight is {weight}'
