#importing mysqldb module
import MySQLdb as mdb
import sys

con=mdb.connect('localhost','gurunath','guru','CoffeeShop')

#With the with keyword,the python interpreter automatically releases the resources.It also provides error handling
with con:
        cur=con.cursor()
f=open("Big_eats","r")
cur.execute("CREATE TABLE IF NOT EXISTS Big_eats(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Big_eats(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

f=open("Small_eats","r")
cur.execute("CREATE TABLE IF NOT EXISTS Small_eats(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Small_eats(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

f=open("Combo","r")
cur.execute("CREATE TABLE IF NOT EXISTS Combo(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Combo(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

f=open("Cakeaway","r")
cur.execute("CREATE TABLE IF NOT EXISTS Cakeaway(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Cakeaway(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

f=open("Sundaes","r")
cur.execute("CREATE TABLE IF NOT EXISTS Sundaes(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Sundaes(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

f=open("Sweet_Treats","r")
cur.execute("CREATE TABLE IF NOT EXISTS Sweet_Treats(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(50),Price CHAR(5))")
for i in f.readlines():
	i=i.strip()
	name,value=i.split(" ")
	cur.execute("INSERT INTO Sweet_Treats(Name,Price) VALUES(%s,%s)",(name,value))
f.close()

cur.execute("create table if not exists Person_Details(Name varchar(50),Address1 varchar(100),Address2 varchar(100),Address3 varchar(100),Number char(15) primary key)")

