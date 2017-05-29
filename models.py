import sqlite3 as sql
from datetime import datetime

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
            	if row["user"]==username:
                	message = "Already Admin"
                return message
        if (flag):
            message = "New Admin"
        else:
            message = "No New"
    cur.execute("INSERT INTO admins (user,ssid) VALUES (?,?)",(username,ssid))
    con.commit()
    con.close()
    return message

def remove_admin(username, ssid):
    con = sql.connect("database.db")
    flag = True
    message = ""
    with con:
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM admins")

        rows = cur.fetchall()
        for row in rows:
            if row["ssid"]==ssid and row["user"]==username:
                message = "Deleted Admin"
                cur.execute("DELETE FROM admins WHERE user=?",(username,))
                flag = False
                print flag
    if flag:
        message = "Admin Not Found"
    con.commit()
    con.close()
    return message

def insert_tempAccess(username,ssid,start_date, end_date):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tempAccess (tempuser,tempssid,startdate,enddate) VALUES (?,?,?,?)",(username,ssid,start_date,end_date))
    con.commit()
    con.close()
    return "Success"

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
    con.commit()
    con.close()

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
    con.commit()
    con.close()

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
    con.commit()
    con.close()
    return ssid

def register_lock(ssid):
    con = sql.connect("database.db") 
    cur = con.cursor()
    cur.execute("INSERT INTO locks (ssid) VALUES (?)",(ssid))
    con.commit()
    con.close()

def is_user(username):
    con = sql.connect("database.db")
    with con:
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM users")

        rows = cur.fetchall()
        for row in rows:
            if row["username"]==username:
                return True
    con.commit()
    con.close()
    return False

def allowance(username):
	con = sql.connect("database.db")
	with con:
		con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM admins")

        rows = cur.fetchall()
        for row in rows:
        	if row["username"]==username:
        		return datetime.today().isoformat()<row['enddate']
        		con.commit()
        		con.close()
	return "User not found"
	con.commit()
	con.close()
