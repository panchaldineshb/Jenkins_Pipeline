#!/usr/bin/python

import MySQLdb as db
import exceptions

# Open database connection
connection = db.connect("localhost","root","meeN$2402","sarabi" )


# Create table as per requirement
sql = """insert into platforms (name, display_name, description)
    values ('eCommerce', 'eCommerce Banking', 'eCommerce Banking Platform')
    """

# prepare a cursor object using cursor() method
cursor = connection.cursor()
try:
    count = cursor.execute(sql)
    connection.commit()
except exceptions.NameError, e:
    print('What? Something went wrong?')
    print e
else:
   print('Ah ... It went as planned.')
finally:
    # close cursor
    cursor.close()

# disconnect from server
connection.close()
