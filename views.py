#from app import app
from flask import render_template, redirect, request, flash, g, session, url_for, jsonify, Flask
from models import *
from servo import *
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

@app.route("/signup", methods=["GET","POST"])
def signup():
    insert_users(request.json['username'],request.json['password'])
    reponse = 'success'
    list = [
        {'param': reponse}
    ]
    return jsonify(results=list)

@app.route("/login", methods=["GET","POST"])
def login():
    username = request.json['username']
    password = request.json['password']
    response = ""
    conf_pass = query(username)
    if conf_pass==password:
    	response = "Grant Access"
    else:
    	response = "Incorrect Username or Password"
    list = [
        {'param': response}
    ]
    return jsonify(results=list)

@app.route("/makeadmin", methods=["GET","POST"])
def makeadmin():
	username= request.json['username']
	ssid=request.json['ssid']
	response = insert_admins(username,ssid)
	list = [
		{'param':response}
	]
	return jsonify(results=list)

@app.route("/checkrights", methods=["GET","POST"])
def checkrights():
	username = request.json['username']
	response = ""
	if(is_admin(username)):
		response = "Admin"
	else:
		response = "Not Admin"
	list = [
        {'param': response}
    ]
	return jsonify(results=list)

@app.route("/operatelock", methods=["GET","POST"])
def operatelock():
	username = request.json['username']
	ssid = request.json['ssid']
	action=request.json['action']
	response = ""
	conf_ssid = get_ssid(username)
	if conf_ssid==ssid:
		response = "Open Lock"
                if action=="open":
                    open()
                elif action=="close":
                    close()         
	else:
		response = "Invalid SSID"
	list = [
        {'param': response}
        ]
	
	return jsonify(results=list)

@app.route("/tempaccess", methods=["GET", "POST"])
def addtempaccess():
	username = request.json['username']
	ssid = request.json['ssid']
	action =  request.json['action']
	response = ""
	if action == 'add':
		insert_tempAccess(username,ssid)
		response = "Added user"
	elif action == 'remove':
		delete_tempAccess(username)
		print "nice"
		response = "Removed User"
	list = [
        {'param': response}
    ]
	return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    		