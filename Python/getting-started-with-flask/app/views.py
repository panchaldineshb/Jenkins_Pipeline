# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/about')
def about():
    return render_template("about.html")
