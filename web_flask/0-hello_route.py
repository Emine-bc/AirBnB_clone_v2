#!/usr/bin/python3
'''script that create new route'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''“Hello HBNB!” '''
    return ("Hello HBNB!")
if __name__ == "__main__":
    app.run("0. 0.0.0")
