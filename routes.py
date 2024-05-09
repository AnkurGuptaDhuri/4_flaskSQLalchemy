from flask import render_template, request, redirect, url_for
from flask_login import login_required
import datetime
from main_app import app, db

#Route to index page
@app.route("/")
def hello_world():
    return "<p>Hello, World!, Welcome</p>"

#routing to login page
@app.route("/login", methods =['POST', 'GET'])
def login_to_application():
    if request.method == 'POST':  
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        #return redirect("http://www.google.com") 
        #redirect(url_for('/welcome'))
        return render_template("home.html", utc_dt=datetime.datetime.utcnow())
    else:
        return (render_template("login.html", utc_dt=datetime.datetime.utcnow()))
    #("<h1> render template </h1>")

@app.route("/signup", methods=['POST','GET'])
def signup_users():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        user = [fname, lname, email]
    return render_template("home.html", utc_dt=datetime.datetime.utcnow())

@app.route('/welcome')
def home():
    return render_template("home.html", utc_dt=datetime.datetime.utcnow())

@app.route('/logout')
#@login_required
def  logout():
    #logout_user()
    return redirect(url_for('/login'))