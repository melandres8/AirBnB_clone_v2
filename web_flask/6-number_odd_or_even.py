#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    string = text.replace('_', ' ')
    return "C {}".format(string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text='is cool'):
    string = text.replace('_', ' ')
    return "Python {}".format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        typo = '{} is even'.format(n)
    else:
        typo = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', n=typo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
