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
  with connection.cursor() as cursor:
    sql = "select * from artist;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









