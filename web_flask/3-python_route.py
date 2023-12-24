#!/usr/bin/python3
"""Create a flask app"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB!"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return ("{}".format(text))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="cool"):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return ("python is {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
