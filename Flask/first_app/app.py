from doctest import debug
from flask import Flask

# Instance of the Flask App which will act as WSGI
app = Flask(__name__)

@app.route("/")
def welcome():
    return "First flask course"

@app.route("/index")
def index():
    return "First flask course Index Page"

if __name__ == "__main__":
    app.run(debug = True)