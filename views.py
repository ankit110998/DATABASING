#from app import app
from flask import render_template, redirect, request, flash, g, session, url_for, jsonify, Flask
from models import *
<<<<<<< HEAD
from servo import *
=======
>>>>>>> b9c0d907f21471dd628d57883ca498fef4827b1f
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
<<<<<<< HEAD

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

=======

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

@app.route("/makeadmin", methods=["GET","POST"])
def makeadmin():
	username= request.json['username']
	ssid=request.json['ssid']
	insert_admins(username,ssid)
	list = [
		{'param':'success'}
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

>>>>>>> b9c0d907f21471dd628d57883ca498fef4827b1f
@app.route("/operatelock", methods=["GET","POST"])
def operatelock():
	username = request.json['username']
	ssid = request.json['ssid']
<<<<<<< HEAD
	action=request.json['action']
	response = ""
	conf_ssid = get_ssid(username)
	if conf_ssid==ssid:
		response = "Open Lock"
                if action=="open":
                    open()
                elif action=="close":
                    close()         
=======
	conf_ssid = get_ssid(username)
	if conf_ssid==ssid:
		response = "Open Lock"
>>>>>>> b9c0d907f21471dd628d57883ca498fef4827b1f
	else:
		response = "Invalid SSID"
	list = [
        {'param': response}
<<<<<<< HEAD
        ]
	
=======
    ]
>>>>>>> b9c0d907f21471dd628d57883ca498fef4827b1f
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
<<<<<<< HEAD
		print "nice"
=======
>>>>>>> b9c0d907f21471dd628d57883ca498fef4827b1f
		response = "Removed User"
	list = [
        {'param': response}
    ]
	return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    		