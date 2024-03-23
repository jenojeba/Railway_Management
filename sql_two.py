import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="railway_management")

cursor=mycon.cursor()
cursor.execute("create table class(S_NO integer(1),CLASS varchar(15))")

cursor.execute("insert into class(S_NO,CLASS) values({},'{}')".format(1,"1st class"))
cursor.execute("insert into class(S_NO,CLASS) values({},'{}')".format(2,"2nd class"))
cursor.execute("insert into class(S_NO,CLASS) values({},'{}')".format(3,"3rd class"))
cursor.execute("insert into class(S_NO,CLASS) values({},'{}')".format(4,"Sleeper"))

mycon.commit()

cursor.execute("create table quota(S_NO integer(1),Quota varchar(18))")
cursor.execute("insert into quota(S_NO,Quota) values({},'{}')".format(1,"General"))
cursor.execute("insert into quota(S_NO,Quota) values({},'{}')".format(2,"Ladies"))
cursor.execute("insert into quota(S_NO,Quota) values({},'{}')".format(3,"Gents"))
cursor.execute("insert into quota(S_NO,Quota) values({},'{}')".format(4,"Tatkal"))

mycon.commit()

cursor.execute("CREATE TABLE `pd`(`S_No` int NOT NULL AUTO_INCREMENT,`B_No` int NOT NULL DEFAULT '0',`Name` varchar(15) DEFAULT NULL,`Age` int DEFAULT NULL,`Gender` varchar(7) DEFAULT NULL,`Phone_Number` varchar(14) DEFAULT NULL,PRIMARY KEY (`S_No`) AUTO_INCREMENT=14 ")

cursor.execute("create table amt(S_NO int PRIMARY KEY AUTO_INCREMENT,Name varchar(20),total_amt int(10))")

#sql_three.py
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="railway_management")

cursor=mycon.cursor()

cursor.execute("create table Tatkal(S_NO integer(1),Class varchar(15))")
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(1,'First class'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(2,'Second class'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(3,'Third class'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(4,'Sleeper'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(5,'Ladies'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(6,'Gents'))
cursor.execute("insert into Tatkal(S_NO,Class) values({},'{}')".format(7,'General'))

mycon.commit()

cursor.execute("create table td(S_NO int PRIMARY KEY AUTO_INCREMENT,Departure varchar(25),Destination varchar(25),Train varchar(30),Time varchar(15),B_NO int(5))")

cursor.execute("create table st(S_NO int PRIMARY KEY AUTO_INCREMENT,B_NO int(5),Class_Quota varchar(20),Seat varchar(20))")

cursor.execute("create table da(S_NO int PRIMARY KEY AUTO_INCREMENT,Date varchar(10))")

cursor.execute("CREATE TABLE booking_details(S_NO int NOT NULL AUTO_INCREMENT,name varchar(50),phone_number varchar(50),age int,gender varchar(10),booked_date timestamp NULL DEFAULT CURRENT_TIMESTAMP,_from varchar(50),_to varchar(50),total_passenger int,total_amount int,date_to_journy varchar(50),payment_status varchar(50) DEFAULT 'No',PRIMARY KEY (`s_no`),UNIQUE KEY `S.No` (`s_no`))")

