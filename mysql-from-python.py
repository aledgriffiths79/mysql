import os
import datetime
import pymysql

# Get username from cloud9 workspace
# (modify this variable if runnin on another environment)

username = "root"

# connect to the database
connection = pymysql.connect(host = "localhost",
user=username,
password="motoisfun38",
db="chinook")

try:
  # run a query
  with connection.cursor() as cursor:
    row = ("Bob", 21, "1990-02-06 23:04:56")
    cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
    connection.commit()
    
finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









