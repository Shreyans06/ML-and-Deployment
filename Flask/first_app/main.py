from doctest import debug
from flask import Flask, render_template, request

### Jinga2 Template engine
'''
{{ }} expressions to print the output in html
{%...%} conditions, for loops
{#...#} this is used for comments
'''

# Instance of the Flask App which will act as WSGI
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>First flask course</h1></html>"

@app.route("/index" , methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/form" , methods = ['GET' , 'POST'])
def form():
    if request.method == "POST":
        name = request.form['name']
        return f'Hello {name}'
    return render_template("form.html")


@app.route("/submit" , methods = ['GET' , 'POST'])
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f'Hello {name}'
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html' , result = res)

@app.route("/success_res/<int:score>")
def success_jinja(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score' : score , 'res' : res}
    return render_template('result_jinja.html' , result = exp)

if __name__ == "__main__":
    app.run()