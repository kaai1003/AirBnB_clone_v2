#!/usr/bin/python3
"""flask web application module"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """display cities by state list"""
    states_list = storage.all(State)
    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def teardown(exception):
    """close stroage db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
