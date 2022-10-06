""" Q.5. Provide a program to create tables (Employee, Department, Project) in database Sqlite and insert the data.
Make sure to add basic field, with employee to department and project relation.
 Make sure maintain M2M relation between employee and project.
"""

import sqlite3 as sql


con = sql.connect('Company.db') # DataBase Crated
cur = con.cursor() # database connected

cur.execute("CREATE TABLE IF NOT EXISTS Employee (FirstName TEXT, LastName TEXT,Age INT ,EmpID TEXT PRIMARY KEY, Dept TEXT, Role TEXT)")
data = [("Patt", "Commince", 34 ,"C1","ENG", "jr.Eng"),("Mahendra", "Dhoni",41,"R1", "IT", "DA"),("Jane","Banner",34,"b1","Bio","Sr.Eng")]
cur.executemany("INSERT INTO Employee VALUES(?,?,?,?,?,?)",data)

print(data)

cur.execute("CREATE TABLE IF NOT EXISTS Department (Dept TEXT, EmpID TEXT)")
data1 = [("ENG","C1"),("IT","R1"),("Bio","b1")]
cur.executemany("INSERT INTO Department VALUES(?,?)",data1)
print(data1)

cur.execute("CREATE TABLE IF NOT EXISTS Project (Project TEXT, EmpID TEXT)")
data2 = [("ColourPrediction","C1"),("SnakeGame","R1"),("SpamDetection","b1")]
cur.executemany("INSERT INTO Department VALUES(?,?)",data2)
print(data2)

Updata = cur.execute("SELECT * FROM Employee JOIN Project ON Employee.EmpId = Project.EmpID WHERE Employee.EmpID==Project.EmpID")

print(list(Updata))
con.commit() # saving the database
con.close() # closing the database