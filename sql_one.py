import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="railway_management")

cursor=mycon.cursor()

# FROM AND TO
#create database railway_management;
#use railway_management;
cursor.execute("create table Journey(S_NO integer(2),DEPARTURE_FROM varchar(20),DESTINED_TO varchar(20))")

cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(1,'Tirunelveli','Chengalpattu'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(2,'Tirunelveli','Erode'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(3,'Tirunelveli','Tiruchendur'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(4,'Tirunelveli','Sengottai'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(5,'Tirunelveli','Coimbator'))

cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(6,'Tuticorin','Chengalpattu'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(7,'Tuticorin','Erode'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(8,'Tuticorin','Tiruchendur'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(9,'Tuticorin','Sengottai'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(10,'Tuticorin','Coimbator'))

cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(11,'Kanyakumari','Chengalpattu'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(12,'Kanyakumari','Erode'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(13,'Kanyakumari','Tiruchendur'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(14,'Kanyakumari','Sengottai'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(15,'Kanyakumari','Coimbator'))

cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(16,'Madurai','Chengalpattu'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(17,'Madurai','Erode'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(18,'Madurai','Tiruchendur'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(19,'Madurai','Sengottai'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(20,'Madurai','Coimbator'))

cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(21,'Nagarcoil','Chengalpattu'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(22,'Nagarcoil','Erode'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(23,'Nagarcoil','Tiruchendur'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(24,'Nagarcoil','Sengottai'))
cursor.execute("insert into Journey(S_NO,DEPARTURE_FROM,DESTINED_TO) values({},'{}','{}')".format(25,'Nagarcoil','Coimbator'))

mycon.commit()



#Search Train

cursor.execute("create table Train(S_No integer(3),Train varchar(25),Time varchar(10))")

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(1,'CAPE HWH FESTSPL','9:40 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(2,'TEN MS Express','7:45 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(3,'TEN DR EXPRESS','7:15 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(4,'CHALUKYA EXPRESS','3:00 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(5,'COIMBATORE EXPRESS','10:40 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(6,'MUMBAI EXPRESS','7:45 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(7,'MYS TN FEST SPL','10 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(8,'TN MYS FESt SPL','4:30 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(9,'HWH CAPE SPECIAL','6:05 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(10,'TS EXPRESS','7:30 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(11,'COIMBATORE EXPRESS','10:40 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(12,'TEN DR EXPRESS','7:15 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(13,'TEN BILASPUR EXPRESS','1:15 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(14,'CAPE HWH FESTSPL','9:40 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(15,'TEN MS EXPRESS','7:45 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(16,'VIVEK EXPRESS','10:00 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(17,'MYSORE EXPRESS','4:25 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(18,'TN CBE LINK EXPRESS','10:35 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(19,'TT EXPRESS','8:15 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(20,'TS EXPRESS','4:00 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(21,'TN CB LINK EXPRESS','10:35 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(22,'CAPE MS EXPRESS','5:05 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(23,'CHENNAI EXPRESS','5:05 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(24,'KANYAKUMARI EXPRESS','5:20 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(25,'GUV CHENNAI EXPRESS','6:15 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(26,'MUMBAI EXPRESS','6:00 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(27,'COIMBATORE EXPRES','9:30 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(28,'TEN BILASPUR EXPRESS','2:30 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(29,'KT EXPRESS','3:30 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(30,'KS EXPRESS','4:00 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(31,'COIMBATORE EXPRESS','9:30 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(32,'GURUDEV EXPRESS','2:45 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(33,'TEN BILASPUR EXPRESS','2:30 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(34,'CAPE HWH FESTSPL','11:55 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(35,'TEN MS EXPRESS','10:15 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(36,'RMM MUV FEST SPL','1:45 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(37,'MDU MAS AC EXPRESS','10:45 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(38,'DEHRADUN EXPRESS','11:35 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(39,'VIVEK EXPRESS','1:00 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(40,'TEN JAMMU EXPRESS','7:30 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(41,'MS TEN EXPRESS','3:35 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(42,'HWH CAPE SPL','4:20 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(43,'MS TEN EXPRESS','3:35 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(44,'HWH CAPE SPL','4:20 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(45,'TEN DR EXPRESS','9:55 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(46,'COIMBATORE EXPRESS','1:55 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(47,'TN CBE LINK EXPRESS','1:55 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(48,'CAPE HWH FESTSPL','8:25 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(49,'CAPE MS EXPRESS','5:25 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(50,'COIMBTORE EXPRESS','9:30 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(51,'MUMBAI EXPRESS','6:00 AM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(52,'GURUDEV EXPRESS','2:45 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(53,'HIMSAGAR EXPRESS','2:45 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(54,'NT EXPRESS','5:00 AM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(55,'NS EXPRESS','4:30 PM'))

cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(56,'COIMBATORE EXPRESS','9:30 PM'))
cursor.execute("insert into Train(S_No,Train,Time) values({},'{}','{}')".format(57,'GURUDEV EXPRESS','2:45 PM'))

mycon.commit()

