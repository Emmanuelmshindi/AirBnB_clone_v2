#!/usr/bin/python3
""" Starts a flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# Creates an instance of the flask app and assigns it to the variable app
app = Flask(__name__)

# Teardown the sqlalchemy session after each request
@app.teardown_appcontext
def teardown(exception):
    storage.close()

# Define the route for /cities_by_states
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """ Return state objects with cities related to each state """
    # Fetch all State objects from DBStorage
    states = storage.all(State)

    # Render template and pass list of states to it
    return render_template("8-cities_by_states.html", states=states)

if __name__ == '__main__':
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
