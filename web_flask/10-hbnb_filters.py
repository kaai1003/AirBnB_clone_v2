#!/usr/bin/python3
"""flask web application module"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_filter():
    """display cities of id state"""
    states_list = storage.all(State)
    amenities_list = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states_list,
                           amenities = amenities_list)


@app.teardown_appcontext
def teardown(exception):
    """close stroage db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
