from flask import render_template, redirect, request, flash, g, session, url_for, jsonify, Flask
from models import *
from servo import *
from datetime import datetime,date
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])

@app.route("/signup", methods=["GET","POST"])
def signup():
    username = request.json['username']
    if is_user(username):
    	response = "Choose a different username"
    	
    else:
    	response = "Success"
    	insert_users(request.json['username'],request.json['password'])
    list = [
        {'param': response}
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
		print is_user(username)
		response  = insert_admins(username,ssid)
	else:
		response = "User Not Found"
	list = [
		{'param':response}
	]
	print response
	return jsonify(results=list)

@app.route("/removeadmin", methods=["GET","POST"])
def removeadmin():
	username = request.json['username']
	ssid = request.json['ssid']
	if is_user(username):
		response  = remove_admin(username,ssid)
	else:
		response = "User Not Found"
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
	if is_admin(username) and conf_ssid==ssid:
		response = "Operate Lock"
		if action == "open":
			pass
		elif action == "close":
			pass
	else:
		print allowance(username,ssid)
		if allowance(username,ssid) and conf_ssid==ssid:
			response = "Operate Lock"
			if action == "open":
				pass
			elif action == "close":
				pass
		else:
			response  = "Invalid Username/SSID"
	list = [
		{'param':response}
		]
	return jsonify(results=list)

@app.route("/tempaccess", methods=["GET", "POST"])
def tempaccess():
	username = request.json['username']
	ssid = request.json['ssid']
	password = query(username)
	start_time = datetime(request.json['start-year'],request.json['start-month'],request.json['start-date'],request.json['start-hours'],request.json['start-minute'])
	end_time = datetime(request.json['end-year'],request.json['end-month'],request.json['end-date'],request.json['end-hours'],request.json['end-minute'])
	start_date = date(request.json['start-year'],request.json['start-month'],request.json['start-date'])
	end_date = date(request.json['end-year'],request.json['end-month'],request.json['end-date'])
	start_minute = request.json['start-minute']
	start_hour = request.json['start-hours']
	end_hour = request.json['end-hours']
	end_minute = request.json['end-minute']
	response = ""
	print start_time>end_time
	if not is_user(username):
		response = "Invalid Username"
		list = [
        {'param': response}
    ]
		return jsonify(results=list)
	if start_time>end_time:
		response = "Invalid Time Span!" 
		list = [
        {'param': response}
    ]
		return jsonify(results=list)
	elif datetime.today()>end_time:
		print end_time
		response = "The end time is from the past."
		list = [
        {'param': response}
    ]
		return jsonify(results=list)
	response = insert_tempAccess(username,ssid,start_time.isoformat(),end_time.isoformat())
	list = [
        {'param': response}
    ]
	print response
	return jsonify(results=list)

@app.route("/validuser", methods=["GET","POST"])
def valid_user():
	username = request.json['username']
	response = ""
	if is_user(username):
		response = "OK"
	else:
		response = "Not Ok"
	list = [
	{'param':response}
	]
	return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    		
