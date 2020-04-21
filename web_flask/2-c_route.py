#!/usr/bin/python3
'''script that create new route'''
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
def c_var_text(text_type):
    '''“HBNB!” '''
    display = "c" + " " + text_type.replace('_', ' ')
    return(display)
if __name__ == "__main__":
    app.run(host='0.0.0.0')
