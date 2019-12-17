import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="navin",passwd="1234")

mycursor=mydb.cursor()
mycursor.execute("select * from student")

result=mycursor.fetchone()#fetchall

for i in mycursor:
    print(i)