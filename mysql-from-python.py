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
    rows = [(23, "Bob"),
             (24, "Jim"),
              (25, "Fred")]
    cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
    rows)
    connection.commit()
    
finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









