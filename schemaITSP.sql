drop table if exists users;
create table users(
username text primary key,
password text not null);

drop table if exists locks;
create table locks(
ssid text primary key);

drop table if exists admins;
create table admins(
username text,
ssid text primary key,
foreign key (user) REFERENCES users(username);

drop table if exists tempAccess;
create table tempAccess(
Time datetime null,	
id integer primary key autoincrement,
user text,
foreign key (user) REFERENCES users(username));

