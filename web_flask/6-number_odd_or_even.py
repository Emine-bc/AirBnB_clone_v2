#!/usr/bin/python3
'''script that create new route'''
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''“Hello HBNB!” '''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    '''“HBNB!” '''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_var_text(text):
    '''“HBNB!” '''
    return ("C " + str(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
def display():
    return('Python is cool')


@app.route('/python/<text>', strict_slashes=False)
def p_var_text(text):
    '''“HBNB!” '''
    return ("Python " + str(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def d_int(n):
    '''“HBNB!” '''
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    '''“HBNB!” '''
    return (render_template("5-number.html", nbre=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''“HBNB!” '''
    return (render_template("6-number_odd_or_even.py", num=n))
if __name__ == "__main__":
    app.run(host='0.0.0.0')
