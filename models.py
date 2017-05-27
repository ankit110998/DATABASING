import sqlite3 as sql

def insert_users(username, password):
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute("INSERT INTO users (username, password) VALUES (?,?)",(username,password))
	con.commit()
	con.close()

def insert_admins(username,ssid):
	con = sql.connect("database.db")
        flag = True
	ssidd = ""
	with con:
		con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM admins")

        rows = cur.fetchall()
        for row in rows:
        	if row["ssid"]==ssid:
        		flag = False
        if (flag):
	    cur.execute("INSERT INTO admins (user,ssid) VALUES (?,?)",(username,ssid))
	    message = "New Admin"
	else:
	    message = "No New"
	con.commit()
	con.close()
        return(message)

def insert_tempAccess(username,ssid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO tempAccess (tempuser,tempssid) VALUES (?,?)",(username,ssid))
	con.commit()
	con.close()

def delete_tempAccess(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM tempAccess WHERE tempuser=?",(username,))
	con.commit()
	con.close()

def query(username):
    con = sql.connect("database.db")
    with con:
        con.row_factory = sql.Row
       
        cur = con.cursor() 
        cur.execute("SELECT * FROM users")

        rows = cur.fetchall()

        for row in rows:
            if row["username"] == username:
                return row["password"]

def is_admin(username):
	con = sql.connect("database.db")
	with con:
		con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM admins")

        rows = cur.fetchall()
        for row in rows:
        	if row["user"]==username:
        		return True
        return False

def get_ssid(username):
	con = sql.connect("database.db")
	ssid = ""
	with con:
		con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM admins")

        rows = cur.fetchall()
        for row in rows:
        	if row["user"]==username:
        		ssid = row["ssid"]
        if ssid == "":
        	cur.execute("SELECT * FROM tempAccess")
        	rows = cur.fetchall()
        	for row in rows:
        		if row["tempuser"]==username:
        			ssid = row["tempssid"]
        return ssid