#!/usr/bin/python

import MySQLdb as db

# Open database connection
connection = db.connect("localhost","root","meeN$2402","" )

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute('CREATE DATABASE sarabi;')

# disconnect from server
connection.close()
