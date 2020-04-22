#!/usr/bin/python3
'''script that create new route'''
from models import storage
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_l():
    '''HBNB!'''
    out = []
    for key in storage.all(State):
        states.append(storage.all(key))
        y = render_template('7-states_list.html', out=out)
    return (y)


@app.teardown_appcontext
def tear_d(self):
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
