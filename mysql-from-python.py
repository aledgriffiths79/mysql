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
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
                    Friends(name char(20), age int, DOB datetime);""")
    # Note that the above will still display a warning (not error) if the table already exists
    for row in cursor:
      print(row)

finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









