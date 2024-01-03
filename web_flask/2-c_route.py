#!/usr/bin/python3
""" This starts Flask Web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """print web"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """print C then the value of the variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
