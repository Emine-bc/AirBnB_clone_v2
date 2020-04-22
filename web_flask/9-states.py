#!/usr/bin/python3
'''script that create new route'''
from models import State
from models import storage
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id():
    '''city by state'''
    return render_template('9-states.html', stat=stat)


@app.teardown_appcontext
def tear_d(self):
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
