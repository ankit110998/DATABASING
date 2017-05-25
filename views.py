from app import app
from flask import render_template, redirect, request, flash, g, session, url_for
from models import *

@app.route("/", methods=["GET","POST"])
@app.route("/signup",methods=["GET","POST"])
def signup():
	return render_template("signup.html")

@app.route("/signedup", methods=["GET","POST"])
def signup():
	username=request.form['username']
	password=request.form['password']

	if not session.get("logged_in"):
		insert_users(username,password)
	return render_template("homepage.html",username=username)
	
@app.route("/home/<username>")
def homepage(username):
    return render_template("homepage.html",username=username)

@app.route("/login")
def login(): 
    return render_template("login.html")

@app.route("/adding/<username>", methods=["GET","POST"])
def adding(username):
    username = request.form['username']
    password=request.form['password']
    return redirect("/home",username=username) # add a route to the signed in homepage

@app.route("/lockid")
ssid=request.json['ssid']
def lockid(ssid):
        insert_locks(ssid)
    		
