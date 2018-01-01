#!/usr/bin/python

import MySQLdb as db

# Open database connection
connection = db.connect("localhost","root","meeN$2402","sarabi" )

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("drop table if exists platforms")

# Create table as per requirement
sql = """create table platforms (
    id int unsigned auto_increment not null,
    name char(20) not null,
    display_name char(40) not null,
    description char(60) not null,
    last_updated timestamp not null default now(),
    primary key(id)
    )"""
cursor.execute(sql)

# disconnect from server
connection.close()
