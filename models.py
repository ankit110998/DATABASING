import sqlite3 as sql

def insert_users(username, password):
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute("INSERT INTO users (username, password) VALUES (?,?)",(username,password))
	con.commit()
	con.close()

def insert_admins(username,ssid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO admins (username,ssid) VALUES (?,?)",(username,ssid))
	con.commit()
	con.close()

def insert_tempAccess(Time,username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO tempAccess",(Time,username))
	con.commit()
	con.close()

def delete_tempAccess(username1):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM tempAccess WHERE username=username1")
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
	
			 		


				
