#!/usr/bin/python3
"""flask web application module"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """display cities of id state"""
    states_list = storage.all(State)
    for state in states_list.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.route('/states', strict_slashes=False)
def states_list():
    """display all states list"""
    states_list = storage.all(State)
    return render_template('9-states.html', states=states_list)


@app.teardown_appcontext
def teardown(exception):
    """close stroage db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
