#from app import app
from flask import render_template, redirect, request, flash, g, session, url_for, jsonify, Flask
from models import *
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

@app.route("/signup", methods=["GET","POST"])
def signup():
    print request.json
    insert_users(request.json['username'],request.json['password'])
    reponse = 'success'
    list = [
        {'param': reponse}
    ]
    return jsonify(results=list)

	
@app.route("/home/<username>")
def homepage(username):
    return render_template("homepage.html",username=username)

@app.route("/login", methods=["GET","POST"])
def login():
    username = request.json['username']
    password = request.json['password']
    conf_pass = query(username)
    if conf_pass==password:
    	reponse = "Grant Access"
    else:
    	reponse = "Incorrect Username or Password"
    list = [
        {'param': reponse}
    ]
    return jsonify(results=list)

@app.route("/adding/<username>", methods=["GET","POST"])
def adding(username):
    username = request.form['username']
    password=request.form['password']
    return redirect("/home",username=username) # add a route to the signed in homepage

@app.route("/lockid")
def lockid():
	ssid=request.json['ssid']
	insert_locks(ssid)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    		
