import random
import csv
from http import HTTPStatus

import requests
from flask import Flask, Response
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
from faker import Faker


app = Flask(__name__)


@app.route('/')
def hello_world():
    links = [
        '<a href="/generate_password">Generate students</a>',
        '<a href="/get_bitcoin_value">Get Bitcoin value</a>'
    ]

    return '<br>'.join(links)


@app.route('/generate_students')
@use_kwargs(
    {
        'count': fields.Int(missing=20, validate=validate.Range(
            min=1, max=1000, max_inclusive=True
        )),

    },
    location='query'
)
def generate_students(count: int):
    fake = Faker()
    users = []
    for i in range(count):
        user_name = fake.name().split(' ')
        user = {
            'first_name': user_name[0],
            'last_name': user_name[1],
            'email': fake.email(),
            'password': fake.password(length=8),
            'age': random.randint(18, 60)
        }
        users.append(user)

    file_name = 'users.csv'
    with open(file_name, 'w', newline='') as csvfile:
        headers = ['first_name', 'last_name', 'email', 'password', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(users)
    return users


@app.route('/get_bitcoin_value')
@use_kwargs(
    {
        'currency': fields.Str(missing='USD', validate=validate.OneOf(['USD', 'EUR', 'UAH'])),
        'convert': fields.Int(missing=1, validate=validate.Range(
            min=1, min_inclusive=True
        )),
    },
    location='query'
)
def get_bitcoin_value(currency: str, convert: int):
    response = requests.get('https://bitpay.com/api/rates')
    if response.status_code not in [HTTPStatus.OK]:
        return Response('Error: something went wrong', status=response.status_code)

    data: dict = response.json()
    result = ''
    for entity in data:
        if entity.get('code') == currency:
            rate = entity.get('rate')
            result = str(rate * convert)
            break

    currency_response = requests.get('https://test.bitpay.com/currencies')
    currency_data: dict = currency_response.json()
    symbol = ''
    for currency_entity in currency_data.get('data'):
        if currency_entity.get('code') == currency:
            symbol = currency_entity.get('symbol')
            break

    return symbol + result

