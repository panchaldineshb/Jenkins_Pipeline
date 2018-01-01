#!/usr/bin/python

import MySQLdb as db

# Open database connection
connection = db.connect("localhost","root","meeN$2402","sarabi" )

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
    ID INT(11) NOT NULL auto_increment PRIMARY KEY,
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server
connection.close()
