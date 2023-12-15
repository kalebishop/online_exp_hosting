"""
Flask HTTP Methods

There are a few core HTTP methods that you might want to use
with Flask:
GET: The default method for a route. The client is requesting data.
POST: The client is sending data to the server (append)
PUT:  The client is sending data to the server (overwrite)

There are a few other methods, but these are the most common.
Below is a simple example showing how to specify a method for a route
and how that method behaves.
"""

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/') # The root URL
def index():
    return 'Index Page'

def execute_command(request):
    # Do something with the data
    print(request.form)
    print("Received command: " + request.form["command"])

@app.route('/robotcommand', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        execute_command(request)
    return render_template('command.html')
