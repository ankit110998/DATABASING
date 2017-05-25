import sqlite3 as sql

def insert_users(username, password):
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute("INSERT INTO users (username, password)",(username,password))
	con.commit()
	con.close()

def insert_locks(ssid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO locks(ssid)", ssid)
	con.commit()
	con.close()

def insert_admins(username,ssid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO admins",(username,ssid))
	con.commit()
	con.close()

def insert_tempAccess(Time,username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute(INSERT INTO "tempAccess",(Time,username))
	con.commit()
	con.close()

def delete_tempAccess(username1):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM tempAccess WHERE username=username1";)
	con.commit()
	con.close()

def select_users(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	if username = 'username' :
		cur.execute("select * from users")
	else:
		string = "select"
		for i in xrange(len(username)-1):
			string +="%s"
		string += "%s"
		string += "from users"
        result=cur.execute(string)
        con.close()
        return result.fetchall()
	
			 		


				
