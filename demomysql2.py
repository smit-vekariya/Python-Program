# in this program we join two table 1. Student and 2. matks using join
import mysql.connector as db
mydb=db.connect(
    host="localhost",
    user="root",
    password="9537127284",
    database="pythondb"
)
myd=mydb.cursor()

#create table
"""
sql="Create table Marks(id int(2), java int(3), python int(3), maths int(3))"
myd.execute(sql)
mydb.commit()
print(myd.rowcount,"row created")
"""

#show table
"""
myd.execute("show tables")
for x in myd:
    print(x)
    
"""
#insert record
"""
sql="insert into Marks(id, java, python, maths) values (%s, %s, %s, %s)"
val=[
  ('13', ' ', '96', '05'),
  ('14', ' ', '95', '97')
]
myd.executemany(sql,val) #use executemany for many record
mydb.commit()
print(myd.rowcount,"row created")
"""
#join the table
    #You can use JOIN instead of INNER JOIN. They will both give you the same result.


sql="SELECT \
    Student.name as Student, \
    Marks.java as javamraks \
    FROM Student \
    RIGHT JOIN Marks ON Student.id =Marks.id"
    #LEFT JOIN Marks ON Student.id =Marks.id"  
    #INNER JOIN Marks ON Student.id =Marks.id"
    
myd.execute(sql)
myresult=myd.fetchall()
for x in myresult:
    print(x)

#show table contain
"""
myd.execute("select * from marks")
myresult=myd.fetchall()
for x in myresult:
    print(x)
"""
