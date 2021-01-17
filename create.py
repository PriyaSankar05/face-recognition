import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",password ="root", charset='utf8',database="sam")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  varCHAR(20) NOT NULL,
         LAST_NAME  varCHAR(20),
         AGE int,  
         SEX varCHAR(1),
         INCOME float)"""
cursor.execute(sql)
print("Table Created")
db.close()
