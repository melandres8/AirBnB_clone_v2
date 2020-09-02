#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at
        the end of the request. """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    list_states = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        all_states=list_states,
        all_amenities=list_amenities
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
