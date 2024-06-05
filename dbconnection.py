import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="",
    password=""
)

mycursor=mydb.cursor()

mycursor.execute("SHOE DATABASES")

for x in mycursor:
    prinnt(x)