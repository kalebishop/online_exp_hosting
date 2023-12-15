"""
Source: https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

A simple flask app that returns "Hello, World!" when you visit the root URL.
For this example, you can just run:
flask --app 1_flask_only run

If you wanted to make your app visible to other
devices on the local network, you would specify
your host IP:
flask --app 1_flask_only --host=0.0.0.0 run
"""


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/') # The root URL
def index():
    return 'Index Page'

@app.route('/about')
def about():
    return 'The about page'

# Serving templates (HTML, CSS, JS, etc.) using render_template
# Also an example of passing URL variables to templates
@app.route('/hello/')
@app.route('/hello/<name>') # The <name> part is a variable
def hello(name=None): # The variable is passed to the function
    # ...which we then pass to the template
    return render_template('hello.html', name=name)
