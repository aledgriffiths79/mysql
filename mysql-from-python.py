import os
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
  with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    sql = "select * from genre;"
    cursor.execute(sql)
    for row in cursor:
      print(row)

finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









