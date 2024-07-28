#!/usr/bin/python3
"""start a flak app"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """route to root"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to /hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
