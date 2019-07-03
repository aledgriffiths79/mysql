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
    row = [("Bob", 21, "1990-02-06 23:04:56"),
            ("Jim", 56, "1955-05-09 13:12:45"),
              ("Fred", 100, "1911-09-12 01:01:01")]
    cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", row)
    connection.commit()
    
finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









