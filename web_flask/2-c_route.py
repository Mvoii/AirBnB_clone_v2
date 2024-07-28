#!/usr/bin/python3
"""Route using c vars"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """route to root"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to /hbnb"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """route using c vars"""
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
