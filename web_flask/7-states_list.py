#!/usr/bin/python3
'''script that create new route'''
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_l():
    '''“HBNB!” '''
    return (render_template(
        '7-states_list.html', states=storage.all('State').values()))


@app.teardown_appcontext
'''“HBNB!” '''


def tear_d(self):
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
