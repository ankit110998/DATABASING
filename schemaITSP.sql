drop table if exists users;
create table users(
username text primary key,
password text not null);

drop table if exists locks;
create table locks(
ssid text primary key);

drop table if exists admins;
create table admins(
user text,
ssid text,
foreign key (user) REFERENCES users(username));

drop table if exists tempAccess;
create table tempAccess(
id integer primary key autoincrement,
tempuser text,
tempssid text,
foreign key (tempuser) REFERENCES users(username)
foreign key (tempssid) REFERENCES admins(ssid));

