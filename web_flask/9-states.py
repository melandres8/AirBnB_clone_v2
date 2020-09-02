#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at
        the end of the request. """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ Render state template """
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=list_states)


@app.route('/states/<id>', strict_slashes=False)
def cities(id):
    """ Cities template """
    list_states = storage.all(State)
    state_id = "State.{}".format(id)
    if state_id in list_states:
        list_states = list_states[state_id]
    else:
        list_states = None
    return render_template('9-states.html', all_states=list_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
