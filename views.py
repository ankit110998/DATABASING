from flask import render_template, redirect, request, flash, g, session, url_for, jsonify, Flask
from models import *
from servo import *
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

@app.route("/signup", methods=["GET","POST"])
def signup():
    insert_users(request.json['username'],request.json['password'])
    if is_user(username):
    	reponse = "Choose a different username"
    else:
    	reponse = "Success"
    list = [
        {'param': reponse}
    ]
    return jsonify(results=list)

@app.route("/login", methods=["GET","POST"])
def login():
    username = request.json['username']
    password = request.json['password']
    conf_pass = query(username)

    if not is_user(username):
    	response = "Not a User"
    	list = [
        {'param': response}
    	]
    	return jsonify(results=list)
    if conf_pass==password:
    	reponse = "Grant Access"
    else:
    	reponse = "Incorrect Password"
    list = [
        {'param': reponse}
    ]
    return jsonify(results=list)

@app.route("/makeadmin", methods=["GET","POST"])
def makeadmin():
	username= request.json['username']
	ssid=request.json['ssid']
	if is_user(username):
		response  = insert_admins(username,ssid)
	else:
		response = "User Not Found"
	list = [
		{'param':response}
	]
	return jsonify(results=list)

@app.route("/removeadmin", methods=["GET","POST"])
def removeadmin():
	username = request.json['username']
	ssid = request.json['ssid']
	response = remove_admin(username, ssid)
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
	action = request.json['action']
	conf_ssid = get_ssid(username)
	response = ""
	if conf_ssid==ssid:
		response = "Operate Lock"
	else:
		response = "Invalid SSID"
	if action == "open":
		open()
	elif action = "close":
		close()
	list = [
        {'param': response}
    ]
	return jsonify(results=list)

@app.route("/tempaccess", methods=["GET", "POST"])
def tempaccess():
	username = request.json['username']
	ssid = request.json['ssid']
	action =  request.json['action']
	password = query(username)
	list = [
        {'param': response}
    ]
	if not is_user():
		response = "Invalid User"
		return jsonify(results=list) 
	response = ""
	if action == 'add':
		insert_tempAccess(username,ssid)
		response = "Added user"
	elif action == 'remove':
		delete_tempAccess(username)
		response = "Removed User"
	list = [
        {'param': response}
    ]
	return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    		