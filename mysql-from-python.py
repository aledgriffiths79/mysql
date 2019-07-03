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
    list_of_names = ['fred', 'fred']
    # Prepare a string with the same number of placeholders as in list_of_names
    format_strings = ",".join(['%s']*len(list_of_names))
    cursor.execute("delete from Friends where name in ({})".format(format_strings), list_of_names)
    connection.commit()
    
finally:
  # close the connection, regardless of whether the above was successful
  connection.close()









