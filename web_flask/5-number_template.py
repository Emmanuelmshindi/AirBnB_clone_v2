#!/usr/bin/python3
""" Script to run flask app """

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Prints Hello HBNB """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ Prints HBNB """
    return "HBNB"

@app.route("/c/<name>", strict_slashes=False)
def sentence(name):
    """ Prints c <name> """
    return "c {}".format(escape(name).replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<name>", strict_slashes=False)
def py_sentence(name="is cool"):
    """ Prints Python <name> """
    return "Python {}".format(escape(name).replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Prints number """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Prints template if n is a number """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
