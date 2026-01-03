from flask import Flask

## Creating Instance of the flask Class
## Which is be our WSGI(Web Server Gateway Interface) application.

## WSGI Application
app = Flask(__name__)

## This is a Home Page
@app.route("/")
def welcome():
    return "Welcome to this flask Course"

@app.route("/index")
def index():
    return "Welcome to the Index page"

if __name__ == "__main__":
    app.run(debug=True)