#!/usr/bin/python3
"""
This Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
/states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

# Create an instance of the Flask class and assign to app variable
app = Flask(__name__)
app.url_map.strict_slashes = False

# Function to remove sqlalchemy session after each request
@app.teardown_appcontext
def teardown(exception):
    """This close the current session of sqlalchemist"""
    storage.close()

# Route to return all state objects
@app.route('/states_list')
def states_list():
    """
    This Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    # Fetch all states from storage engine used
    states = storage.all(State).values()
    # Return html page with states list passed onto it
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
