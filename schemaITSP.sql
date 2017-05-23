drop table if exists users;
create table users(
username text primary key,
password text not null);

drop table if exists locks;
create table locks(
ssid text primary key);

drop table if exists admins;
create table admins(
id integer primary key autoincrement,
username text,
ssid text,
foreign key (username) REFERENCES users,
foreign key (ssid) REFERENCES locks);

drop table if exists tempAccess;
create table tempAccess(
Time datetime null,	
id integer primary key autoincrement,
username text,
foreign key (username) REFERENCES users);

