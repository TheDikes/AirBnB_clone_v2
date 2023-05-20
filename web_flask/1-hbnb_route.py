#!/usr/bin/python3
"""Starts a web application listening
on 0.0.0.0:5000
Routes:
    /:displays 'Hello HBNB!'
    /hbnb: displays 'HBNB'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
