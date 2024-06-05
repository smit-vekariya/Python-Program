import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9537127284",
    database="pythondb"
    )
mycursor=mydb.cursor()
#create databases
#mycursor.execute("Create database pythondb")

#check databases create or not
"""
mycursor.execute("Show databases")
for x in mycursor:
    print(x)
"""
#ceate table
#mycursor.execute("Create table Student(name varchar(25), rollno int(3), address varchar(100))")

#add table
#mycursor.execute("alter table Student add column id int Auto_increment primary key")

#show table
"""
mycursor.execute("show tables")
for x in mycursor:
    print(x)
"""
#insert record in Student database
"""
sql="INSERT INTO Student(name, rollno, address) VALUES (\'smit\',12,\'surat\')"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
"""
#insert record in Student database
"""
sql="INSERT INTO Student(name, rollno, address) VALUES (%s, %s, %s)"
val=[
    ("ramkrish", '17', "jamnager"),
    ("om", "18", "goa")
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
"""
#delete record
"""
  #sql="DELETE FROM Student where id=6"
  #mycursor.execute(sql)
sql = "DELETE FROM Student WHERE id = %s"
adr = ("10",)   
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record deleted.")
"""

#orderby
"""
sql="select * from Student ORDER BY name"
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
"""
#update table
"""
sql = "UPDATE Student SET id= 5 WHERE id = 12"
mycursor.execute(sql)
 #sql = "UPDATE Student SET id= %s WHERE id = %s"
 #val = ("2", "7")
 #mycursor.execute(sql, val)
mydb.commit()
"""
#limit
"""
mycursor.execute("SELECT * FROM Student LIMIT 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""
#show contain of table

mycursor.execute("select * from Student")
    #We use the fetchall() method, which fetches all rows from the last executed statement.
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
