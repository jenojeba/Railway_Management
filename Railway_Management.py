for i in range(1,10000000000000000000):
     print("""                                                 
=  ==   =  = =   =     =     ==   =       = =      =     =  =    =         =     =    =   =  = =
=  = =  =  =  =  =    = =    = =  =       =  =    = =    =  =     =   =   =     = =    = =   = 
=  =  = =  =  =  =   = = =   =  = =       = =    = = =   =  =      = = = =     = = =    =      =
=  =   ==  = =   =  =     =  =   ==       =  =  =     =  =  = = =   =   =     =     =   =    = =

""")                      
     print("""

ABOUT INDIAN RAILWAYS

The first railway on Indian sub-continent ran over a stretch of 21 miles from Bombay to Thane.
The idea of a railway to connect Bombay with Thane, Kalyan and with the Thal and Bhore Ghats inclines first occurred
to Mr. George Clark, the Chief Engineer of the Bombay Government, during a visit to Bhandup in 1843.

The formal inauguration ceremony was performed on 16th April 1853, when 14 railway carriages carrying about 400 guests
left Bori Bunder at 3.30 pm "amidst the loud applause of a vast multitude and to the salute of 21 guns."
The first passenger train steamed out of Howrah station destined for Hooghly, a distance of 24 miles, on 15th August,
1854. Thus the first section of the East Indian Railway was opened to public traffic, inaugurating the beginning of
railway transport on the Eastern side of the subcontinent.


In south the first line was opened on Ist July, 1856 by the Madras Railway Company. It ran between Vyasarpadi Jeeva
Nilayam (Veyasarpandy) and Walajah Road (Arcot), a distance of 63 miles. In the North a length of 119 miles of line
was laid from Allahabad to Kanpur on 3rd March 1859. The first section from Hathras Road to Mathura Cantonment was opened
to traffic on 19th October, 1875.

These were the small’s beginnings which is due course developed into a network of railway lines all over the country.
By 1880 the Indian Railway system had a route mileage of about 9000 miles. INDIAN RAILWAYS, the premier transport organization
of the country is the largest rail network in Asia and the world’s second largest under one management.

""")


     import mysql.connector as sqltor
     mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="railway_management")

     cursor=mycon.cursor()

     def pr():
          data=cursor.fetchall()
          for row in data:
               print(row)
     def s():
          cursor.execute(sql)
          mycon.commit()

     print('\n')
     print('Welcome to Booking, please register your details for booking')
     name=str(input("\nEnter Name : "))

     a_g_e=int(input("Enter your age:"))


     for i in range(0,10):
          g=str(input("\nEnter Gender(Male/Female) : "))
          if g[0:6]=="female" or g[0:6]=="Female" or g[0]=="F" or g[0]=="f":
               break
          elif g[0:4]=="male" or g[0:4]=="Male" or g[0]=="M" or g[0]=="m":
               break
          else:
               continue

     for i in range(0,10000000):
          p=int(input("\nEnter Phone Number : "))
          ph=str(p)
          if len(ph)!=10:
               print("*****Give the Correct Phone number*****")
               continue
          else:
               break


     sql="insert into booking_details(name,phone_number,gender,age) values(%s,%s,%s,%s)"
     val=(name,ph,g,a_g_e)
     cursor.execute(sql,val)
     mycon.commit()


     cursor.execute("SELECT * FROM booking_details ORDER BY s_no DESC LIMIT 1")
     myresult = cursor.fetchall()
     booking_details_sno=list(myresult)
     print("Booking Number = ",booking_details_sno[0][0])
     b_no = booking_details_sno[0][0]

     print('\nWelcome to Booking')
     choice=int(input("\n\t1.Plan your Journey \n\t2.PNR Enquiry \n\t3.Refund \n\t4.Exit \n\nSelect your need : "))

     if choice==1:
          print('\n\tPlanning a Journey')
          print('\n')
          from datetime import date

          today = date.today()

          a=str(today)
          spl=a.split('-')
          year=int(spl[0])
          month=int(spl[1])
          day=int(spl[2])

          print("Today's date:",day,'/',month,'/',year)

          for i in range(0,10):
               date=input("Enter Date of Travel(dd/mm/yyyy) : ")     
               sd=date.split('/')
               d=int(sd[0])
               m=int(sd[1])
               y=int(sd[2])
               if y==2021 or y==2022:
                    if y==2021:
                         if d<day and m<=month:
                              print("Incorrect date(date of journey should not be before current date)")
                              continue
                         elif m<month:
                              print("Incorrect month")
                              continue          
                    elif y==2022:
                         if m==7 or m==8 or m==9 or m==10 or m==11 or m==12:
                              print("The ticket has validation of only 6 months...Book later")
                              continue
                         elif d<day and m<=month:
                              print("Incorrect date(date of journey should not be before current date)")
                              continue
                         elif m<month:
                              print("Incorrect month")
                              continue 

                    else:
                         continue
               else:
                    continue
               break

          sql = "insert into da(Date) values('{}')".format(date)
          s()

          sql = "UPDATE booking_details SET date_to_journy = %s WHERE s_no = %s"
          val = (date, b_no)
          cursor.execute(sql,val)
          mycon.commit()

          print("\n")
          print("    DEPARTURE   AND   DESTINATION    \n")
          cursor.execute("select distinct S_No,Departure_From,Destined_To from Journey")
          pr()

          print('\n')

          for i in range(1,10):

               d=int(input("Select your Departure and Destination : "))
               if d==1:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(1))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(1))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(2))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==1:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(1))
                              pr()

                              cursor.execute('select * from journey where S_No=%s',[d])
                              journey_details = cursor.fetchall()


                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tirunelveli','Chengalpattu','CAPE HWH FESTSPL','9:40 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==2:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(2))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Chengalpattu','TEN MS Express','7:45 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 1 or 2")
                              continue
                    break
               elif d==2:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(2))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(3))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(4))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(5))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(6))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==3:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(3))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Erode','TEN DR EXPRESS','7:15 AM,'{}')".format(b_no)
                              s()
                              break
                         elif t==4:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(4))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Erode','CHALUKYA EXPRESS','3:00 PM','{}')".format(b_no)
                              s()
                              break


                         elif t==5:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(5))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Erode','COIMBATORE EXPRESS','10:40 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==6:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(6))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time) values('Tiunelveli','Erode','MUMBAI EXPRESS','7:45 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 3,4,5 or 6")
                              continue
                    break
               elif d==3:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(3))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(7))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(8))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(9))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==7:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(7))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Tiruchendur','MYS TN FEST SPL','10 AM','{}')".format(b_no)
                              s()
                              break







                         elif t==8:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(8))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Tiruchendur','TN MYS FESt SPL','4:30 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==9:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(9))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tiunelveli','Tiruchendur','HWH CAPE SPECIAL','6:05 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 7,8 or 9")
                              continue
                    break
               elif d==4 :
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(4))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(10))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(10))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tirunelveli', 'Sengottai','TS EXPRESS','7:30 PM','{}')".format(b_no)
                    s()
                    break

               elif d==5:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(5))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(11))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(12))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(13))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==11:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(11))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tirunelveli', 'Coimbator','COIMBATORE EXPRESS','10:40 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==12:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(12))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tirunelveli', 'Coimbator','TEN DR EXPRESS','7:15 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==13:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(13))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tirunelveli', 'Coimbatore','TEN BILASPUR EXPRESS','1:15 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 11,12 or 13")
                              continue
                    break
               elif d==6:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(6))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(14))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(15))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))



                         if t==14:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(14))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Chengalpattu','CAPE HWH FESTSPL','9:40 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==15:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(15))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin', 'Chengalpattu','TEN MS EXPRESS','7:45 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 14 or 15")
                              continue
                    break
               elif d==7:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(7))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(16))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(17))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(18))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==16:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(16))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Erode',' VIVEK EXPRESS','10:00 PM','{}')".format(b_no)
                              s()
                              break







                         elif t==17:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(17))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Erode',' MYSORE EXPRESS','4:25 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==18:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(18))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Erode',' TN CBE LINK EXPRESS','10:35 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 16,17 or 18")
                              continue
                    break
               elif d==8 :
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(8))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(19))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(19))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Tiruchendur',' TT EXPRESS','8:15 PM','{}')".format(b_no)
                    s()
                    break
               elif d==9:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(9))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(20))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(20))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Sengottai','TS EXPRESS','4:00 PM','{}')".format(b_no)
                    s()
                    break
               elif d==10:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(10))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(21))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(21))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Tuticorin','Coimbator','TN CB LINK EXPRESS','10:35 PM','{}')".format(b_no)
                    s()
                    break
               elif d==11:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(11))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(22))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(23))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(24))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(25))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==22:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(22))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Chengalpattu','CAPE MS EXPRESS','5:05 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==23:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(23))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Chengalpattu','CHENNAI EXPRESS','5:05 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==24:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(24))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Chengalpattu','KANYAKUMARI EXPRESS','5:20 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==25:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(25))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Chengalpattu','GUV CHENNAI EXPRESS','6:15 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 22,23,24 or 25")
                              continue
                    break
               elif d==12:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(12))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(26))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(27))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(28))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==26:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(26))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Erode','MUMBAI EXPRESS','6:00 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==27:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(27))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Erode',' COIMBATORE EXPRESS','9:30 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==28:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(28))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Erode','TEN BILASPUR EXPRESS','2:30 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 26,27 or 28")
                              continue
                    break
               elif d==13:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(13))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(29))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(29))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Tiruchendur','KT EXPRESS','3:30 AM','{}')".format(b_no)
                    s()
                    break
               elif d==14:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(14))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(30))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(30))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Sengottai','KS EXPRESS','4:00 PM','{}')".format(b_no)
                    s()
                    break
               elif d==15:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(15))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(31))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(32))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(33))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==31:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(31))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Coimbatore',' COIMBATORE EXPRESS','9:30 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==32:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(32))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Coimbatore','GURUDEV EXPRESS','2:45 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==33:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(33))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Kanyakumari','Coimbator','TEN BILASPUR EXPRESS','2:30 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 31,32 or 33")
                              continue
                    break


               elif d==16:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(16))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(34))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(35))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(36))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==34:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(34))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Chengalpattu','CAPE HWH FESTSPL','11:55 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==35:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(35))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Chengalpattu',' TEN MS EXPRESS','10:15 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==36:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(36))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Chengalpattu','RMM MUV FEST SPL','1:45 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 34,35 or 36")
                              continue
                    break
               elif d==17:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(17))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(37))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(38))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(39))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(40))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==37:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(37))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Erode','MDU MAS AC EXPRESS','10:45 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==38:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(38))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Erode','DEHRADUN EXPRESS','11:35 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==39:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(39))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Erode','VIVEK EXPRESS','1:00 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==40:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(40))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Erode',' TEN JAMMU EXPRESS','7:30 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 37,38,39 or 40")
                              continue
                    break
               elif d==18:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(18))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(41))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(42))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==41:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(41))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Tiruchendur','MS TEN EXPRESS','3:35 AM ','{}')".format(b_no)
                              s()
                              break
                         elif t==42:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(42))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Tiruchendur','HWH CAPE SPL','4:20 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 41 or 42")
                              continue
                    break
               elif d==19:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(19))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(43))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(44))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==43:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(43))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Sengottai','MS TEN EXPRESS','3:35 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==44:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(44))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Sengottai','HWH CAPE SPL','4:20 AM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 43 or 44")
                              continue
                    break
               elif d==20:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(20))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(45))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(46))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(47))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==45:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(45))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Coimbator','TEN DR EXPRESS','9:55 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==46:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(46))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Coimbator','COIMBATORE EXPRESS','1:55 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==47:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(47))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Madurai','Coimbator','TN CBE LINK EXPRESS','1:55 AM','{}')".format(b_no)

                              s()
                              break
                         else:
                              print("Select only 45,46 or 47")
                              continue
                    break
               elif d==21:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(21))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(48))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(49))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==48:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(48))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Chengalpattu','CAPE HWH FESTSPL','8:25 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==49:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(49))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Chengalpattu','CAPE MS EXPRESS','5:25 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 48 or 49")
                              continue
                    break
               elif d==22:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(22))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(50))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(51))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(52))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(53))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==50:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(50))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Erode','COIMBTORE EXPRESS','9:30 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==51:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(51))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Erode','MUMBAI EXPRESS','6:00 AM','{}')".format(b_no)
                              s()
                              break
                         elif t==52:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(52))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Erode',' GURUDEV EXPRESS','2:45 PM','{}')".format(b_no)
                              s()
                              break
                         elif t==53:
                              cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(53))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time) values('Nagarcoil','Erode','HIMSAGAR EXPRESS','2:45 PM')"
                              s()
                              break
                         else:
                              print("Select only 50,51,52 or 53")
                              continue
                    break
               elif d==23:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(23))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(54))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(54))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Tiruchendur','NT EXPRESS','5:00 AM','{}')".format(b_no)
                    s()
                    break
               elif d==24:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(24))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(55))
                    pr()
                    t=print("\nThere  is only one Train ")
                    cursor.execute("select distinct Train,Time from train where S_No={}".format(55))
                    pr()
                    sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Sengottai','NS EXPRESS','4:30 PM','{}')".format(b_no)
                    s()
                    break
               elif d==25:
                    cursor.execute("select distinct DEPARTURE_FROM,Destined_To from Journey where S_NO={}".format(25))
                    pr()
                    print('\n(S_NO,Trains,Time) \n')
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(56))
                    pr()
                    cursor.execute("select distinct S_No,Train,Time from train where S_No={}".format(57))
                    pr()
                    for i in range(1,10):
                         t=int(input("\nThe Train I need : "))
                         if t==56:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(56))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Coimbator','COIMBATORE EXPRESS','9:30 PM','{}')".format(b_no)
                              s()
                              break





                         elif t==57:
                              cursor.execute("select distinct Train,Time from train where S_No={}".format(57))
                              pr()
                              sql="insert into td(Departure,Destination,Train,Time,B_NO) values('Nagarcoil','Coimbator','GURUDEV EXPRESS','2:45 PM','{}')".format(b_no)
                              s()
                              break
                         else:
                              print("Select only 56 or 57")
                              continue
                    break

               else:
                    print("Select only from 1 to 25")
                    print('\n')
                    continue

               pr()

          for i in range(1,10):
               n=int(input("\nNumber of Passengers = "))
               ns=str(n)
               if len(ns)==1 or len(ns)==2:
                    break
               else:
                    print("*****Give the Correct number of passengers*****")
                    continue

          sql = "UPDATE booking_details SET total_passenger = %s WHERE s_no = %s"
          val = (n,b_no)    
          cursor.execute(sql,val)
          mycon.commit()

          print("\n\t******* You have to give the personal details of all the passengers *******")
          old=0
          adult=0
          children=0
          class_=0
          adult_amt=0
          old_amt=0
          children_amt=0

          while n>0:
               n=n-1

               name=str(input("\nEnter Name : "))


               for i in range(1,10):
                    age=int(input("Enter age : "))
                    if age>=18 and age<120:
                         if age>60 and age<120:
                              print("You are a senior citizen")
                              print("You are provided with a lower berth")
                              old=old+1
                              break
                         elif age>=18 and age<60:
                              adult=adult+1
                              break
                         elif age<18:
                              children=children+1
                              break
                         else:
                              print("Enter correct age")
                              continue
                    elif age>120:
                         continue
                    else:
                         break

               for i in range(0,10):
                    g=str(input("Gender(male/female) : "))
                    if g[0:6]=="female" or g[0:6]=="Female" or g[0]=="F" or g[0]=="f":
                         break
                    elif g[0:4]=="male" or g[0:4]=="Male" or g[0]=="M" or g[0]=="m":
                         break
                    else:
                         continue

               for i in range(0,10000000):
                    p=int(input("Enter Phone Number : "))
                    ph=str(p)
                    if len(ph)!=10:
                         print("*****Give the Correct Phone number*****")
                         continue
                    else:
                         break


               print('\n')
               print("1.Class : ")
               cursor.execute("select class from class")
               pr()

               print('\n')
               print("2.Quota : ")
               cursor.execute("select quota from quota")
               pr()

               for i in range(1,10):
                    print('\n')
                    c=int(input("Class or Quota ?"))
                    if c==1:
                         print('\n')
                         print("     Class    ")
                         cursor.execute("select * from class")
                         pr()
                         for i in range(1,10):
                              print('\n')
                              a=int(input("Enter the class : "))
                              if a==1:
                                   cursor.execute("select class from class where S_NO=1")
                                   pr()
                                   sql="insert into st(Class_Quota,Seat) values('First Class','Room')"
                                   s()
                                   class_=a
                                   break
                              elif a==2:
                                   cursor.execute("select class from class where S_NO=2")
                                   pr()
                                   class_=a
                                   for i in range(1,10):
                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('Second Class','Lower Berth')"
                                             s()
                                             break
                                        else: 
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat=Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class','Upper Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class','Side Lower Berth')"
                                                  s()
                                                  break

                                             elif c==4:
                                                  print("Seat=Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class','Side Upper Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1,2,3 or 4 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break
                              elif a==3:
                                   cursor.execute("select class from class where S_NO=3")
                                   pr()
                                   class_=3
                                   for i in range(1,10):
                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('Third Class','Lower Berth')"
                                             s()
                                             break
                                        else:                                    
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \n\t5.Middle Berth\nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat = Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class','Upper Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class','Side Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  print("Seat=Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  print("Middle Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class','Middle Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1,2,3,4 or 5 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break
                              elif a==4:
                                   class_=4
                                   cursor.execute("select class from class where S_NO=4")
                                   pr()
                                   for i in range(1,10):
                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('Sleeper','Lower Berth')"
                                             s()
                                             break
                                        else:
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat=Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper','Upper Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper','Side Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  print("\nSeat = Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper','Side Upper Berth')"
                                                  s()
                                                  break

                                             else:
                                                  print("Select from 1,2,3 or 4 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break
                              else:
                                   print("Select from 1,2,3 or 4 ")
                                   continue
                         break
                    elif c==2:
                         print('\n')
                         print("    Quota    ")
                         cursor.execute("select * from quota")
                         pr()
                         for i in range(1,10):
                              print('\n')
                              b=int(input("Enter the Quota : "))
                              if b==1:
                                   cursor.execute("select quota from quota where S_NO=1")
                                   pr()
                                   for i in range(1,10):

                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('General','Lower Berth')"
                                             s()
                                             break
                                        else:
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \n\t5.Middle Berth\nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('General','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat=Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('General','Upper Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('General','Side Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  print("Seat=Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('General','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  print("Middle Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('General','Middle Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1,2,3,4 or 5 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break

                              elif b==2:
                                   cursor.execute("select quota from quota where S_NO=2")
                                   pr()
                                   for i in range(1,10):

                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('Ladies','Lower Berth')"
                                             s()
                                             break
                                        else:
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \n\t5.Middle Berth\nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat=Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies','Upper Berth')"
                                                  s()
                                                  break





                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies','Side Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  print("Seat=Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  print("Middle Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies','Middle Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1,2,3,4 or 5 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break

                              elif b==3:
                                   cursor.execute("select quota from quota where S_NO=3")
                                   pr()
                                   for i in range(1,10):

                                        if  age>=65 and age<120:
                                             sql="insert into st(Class_Quota,Seat) values('Gents','Lower Berth')"
                                             s()
                                             break
                                        else:
                                             c=int(input("\nSeat : \n\t1.Lower Berth \n\t2. Upper Berth \n\t3.Side Lower Berth \n\t4.Side Upper Berth \n\t5.Middle Berth\nSelect your desired seat : "))
                                             if c==1:
                                                  print("Seat=Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Gents','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  print("Seat=Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Gents','Upper Berth')"

                                                  s()
                                                  break
                                             elif c==3:
                                                  print("Seat=Side Lower Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Gents','Side Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  print("Seat=Side Upper Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Gents','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  print("Middle Berth")
                                                  sql="insert into st(Class_Quota,Seat) values('Gents','Middle Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1,2,3,4 or 5 to choose your desired seat")
                                                  continue
                                             break
                                        break
                                   break

                              elif b==4:
                                   print('\n')
                                   cursor.execute("select quota from quota where S_NO=4")
                                   pr()
                                   cursor.execute("select * from tatkal")
                                   pr()

                                   for i in range(1,10):
                                        print('\n')
                                        c=int(input("Enter your desired Class/Quota : "))
                                        if  age>=65 and age<120:
                                             if c==1:
                                                  cursor.execute("select class from tatkal where S_NO=1")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('First Class(tatkal)','Room')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  cursor.execute("select class from tatkal where S_NO=2")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  cursor.execute("select class from tatkal where S_NO=3")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  cursor.execute("select class from tatkal where S_NO=4")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  cursor.execute("select class from tatkal where S_NO=5")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==6:
                                                  cursor.execute("select class from tatkal where S_NO=6")
                                                  pr()
                                                  class_=c=1
                                                  sql="insert into st(Class_Quota,Seat) values('Gents(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                             elif c==7:
                                                  cursor.execute("select class from tatkal where S_NO=7")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('General(tatkal)','Lower Berth')"
                                                  s()
                                                  break
                                        else:

                                             if c==1:
                                                  cursor.execute("select class from tatkal where S_NO=1")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('First Class(tatkal)','Room')"
                                                  s()
                                                  break
                                             elif c==2:
                                                  cursor.execute("select class from tatkal where S_NO=2")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Second Class(tatkal)','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==3:
                                                  cursor.execute("select class from tatkal where S_NO=3")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Third Class(tatkal)','Upper Berth')"
                                                  s()
                                                  break
                                             elif c==4:
                                                  cursor.execute("select class from tatkal where S_NO=4")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Sleeper(tatkal)','Middle Berth')"
                                                  s()
                                                  break
                                             elif c==5:
                                                  cursor.execute("select class from tatkal where S_NO=5")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Ladies(tatkal)','Upper Berth')"
                                                  s()
                                                  break




                                             elif c==6:
                                                  cursor.execute("select class from tatkal where S_NO=6")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('Gents(tatkal)','Side Upper Berth')"
                                                  s()
                                                  break
                                             elif c==7:
                                                  cursor.execute("select class from tatkal where S_NO=7")
                                                  pr()
                                                  class_=c+1
                                                  sql="insert into st(Class_Quota,Seat) values('General(tatkal)','Upper Berth')"
                                                  s()
                                                  break
                                             else:
                                                  print("Select from 1 to 7")
                                                  continue
                                             break
                                   else:
                                        print("Select only from 1,2,3 or 4")
                                        continue
                                   break
                              break
                         break

                    else:
                         print('\n')
                         print("Select only 1 or 2")
                         continue


               sql = "insert into pd(Name,Age,Gender,Phone_Number,B_No) values(%s,%s,%s,%s,%s)"
               val = (name,age,g,p,b_no)
               cursor.execute(sql,val)
               mycon.commit()


          for i in range(0,10):
             j=str(input("\nIs there any children with you(y/n)?"))
             for i in range(0,10):
                 if j[0]=="Y" or j[0]=="y" :
                     h=int(input("How many children are with you ? "))
                     if h>=1 and h<=15:
                         pass
                     else:
                         continue
                     ag=input("Are they all below age 15? ")
                     if ag[0]=='Y' or ag[0]=='y':
                         print("***** No need to take ticket for those chlidren ***** ")
                         children=0
                         break
                     elif ag[0]=='N' or ag[0]=='n':
                         a_=int(input("How many are above age 15? "))
                         print("***** Tickets need to be taken for the",a_,"children ***** ")
                         children=a_
                         break
                     else:
                         pint("Type either y or n")
                         continue
                     break
                 elif j[0:2]=="No" or j[0:2]=="no" or j[0]=="N" or j[0]=="n":
                     break
             else:
                 print("Type either yes or no")
                 continue
             break

          if class_==1:
               adult_amt=adult*1000
               old_amt=old*500
               children_amt=children*750
          elif class_==2:
               adult_amt=adult*990
               old_amt=old*490
               children_amt=children*740
          elif class_==3:
               adult_amt=adult*980
               old_amt=old*480
               children_amt=children*730
          elif class_==4:
               adult_amt=adult*970
               old_amt=old*470
               children_amt=children*720
          elif class_==5:
               adult_amt=adult*960
               old_amt=old*460
               children_amt=children*710
          elif class_==5:
               adult_amt=adult*950
               old_amt=old*450
               children_amt=children*700
          elif class_==6:
               adult_amt=adult*940
               old_amt=old*440
               children_amt=children*690

          elif class_==7:
               adult_amt=adult*930
               old_amt=old*430
               children_amt=children*680
          global total_amt
          total_amt=adult_amt+old_amt+children_amt
          print("\nTotal Amount for this booking is ",total_amt)

          sql = "UPDATE booking_details SET total_amount = %s WHERE s_no = %s"
          val = (total_amt, b_no)
          cursor.execute(sql,val)
          mycon.commit()



          import time
          import random

          print("X------------Welcome to Payment---------------X")
          name_trans=input("Enter your name:")
          name_age=int(input("Enter your age:"))



          print("X------------CHOOSE MODE OF TRANSACTION---------------X")
          print("1) NET BANKING")
          print("2) CREDIT/DEBIT CARD")
          print("3) UPI PAYMENT ")

          mode_trans=int(input("ENTER (1/2/3) : "))

          if mode_trans==1:
              print("X------------CHOOSE BANK---------------X")
              sbi_trans="1) STATE BANK OF INDIA"
              ib_trans="2) INDIAN BANK"
              iob_trans="3) INDIAN OVERSEAS BANK"
              cb_trans="4) CANARA BANK"
              icici_trans="5) ICICI BANK"
              hdfc_trans="6) HDFC BANK"
              ub_trans="7) UNION BANK"
              print(sbi_trans)
              print(ib_trans)
              print(iob_trans)
              print(cb_trans)
              print(icici_trans)
              print(hdfc_trans)
              print(ub_trans)
              bank_trans=int(input("ENTER (1/2/3/4/5/6/7) : "))
              if bank_trans==1:
                    bank_name="STATE BANK OF INDIA"

              elif bank_trans==2:
                  bank_name="INDIAN BANK"
              elif bank_trans==3:
                  bank_name="INDIAN OVERSEAS BANK"
              elif bank_trans==4:
                  bank_name="CANARA BANK"
              elif bank_trans==5:
                  bank_name="ICICI BANK"
              elif bank_trans==6:
                  bank_name="HDFC BANK"
              elif bank_trans==7:
                  bank_name="UNION BANK"
              if bank_trans==1 or 2 or 3 or 4 or 5 or 6 or 7:
                  userid_trans=input("USERNAME : ")
                  password_trans=input("ENTER PASSWORD : ")

                  print("X-----------------------------------",bank_name,"----------------------------------------X")
                  print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
                  print("|                                                                                        ")
                  print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
                  print("|                                                                                        ")
                  print("| DATE : ",date,"                                                                        ")
                  print("|                                                                                        ")
                  print("| USERNAME : ",userid_trans,"                                                            ")
                  print("|                                                                                        ")
                  print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
                  print("|                                                                                        ")

                  confirm=input("Do you agree to the payment?(y/n)")
                  if confirm=="y":
                      while True:
                          print("OTP will be generated ...")
                          time.sleep(2)
                          otp=random.randint(10000,90000)
                          print(otp)
                          time.sleep(2)
                          otp_copy=int(input("ENTER OTP : "))
                          if otp==otp_copy:
                              print("YOUR AMOUNT HAS BEEN SUCCESSFULLY PAID AND THE TICKET HAS BEEN BOOKED")
                              print("|                                                                                        ")
                              print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")

                              sql = "UPDATE booking_details SET payment_status = %s WHERE s_no = %s"
                              val = ('Yes', b_no)
                              cursor.execute(sql,val)
                              mycon.commit()


                              sql = "insert into amt(Name,total_amt) values(%s,%s)"
                              val = (name,total_amt)
                              cursor.execute(sql,val)
                              mycon.commit()

                              print("YOUR PNR CODE IS : ",b_no)

                              break
                          else:
                              print("INCORRECT OTP!! TRY AGAIN!!")
                  elif confirm=="n":
                      print("exit")

          if mode_trans==2:
               cardcode_trans=input("ENTER CARD NUMBER : ")
               securitycode_trans=input("ENTER 3-DIGIT SECURITY CODE : ")
               cardholder_trans=input("ENTER CARD HOLDER'S NAME : ")
               expirydate_trans=int(input("ENTER CARD'S EXPIRY DATE (DDMMYYYY) : "))
               print("X-----------------------------------","CREDIT/DEBIT CARD","----------------------------------------X")
               print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
               print("|                                                                                        ")
               print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
               print("|                                                                                        ")
               print("| DATE : ",date,"                                                                        ")
               print("|                                                                                        ")
               print("| CARD NUMBER : ",cardcode_trans,"                                                       ")
               print("|                                                                                        ")
               print("| 3 DIGIT SECURITY CODE : ",securitycode_trans,"                                         ")
               print("|                                                                                        ")
               print("| NAME OF CARD HOLDER : ",cardholder_trans,"                                             ")
               print("|                                                                                        ")
               print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
               print("|                                                                                        ")

               confirm=input("Do you agree to the payment?(y/n)")
               if confirm=="y":
                    while True:
                         print("OTP will be generated ...")
                         time.sleep(2)
                         otp=random.randint(10000,90000)
                         print(otp)
                         time.sleep(2)
                         otp_copy=int(input("ENTER OTP : "))
                         if otp==otp_copy:
                              print("YOUR AMOUNT HAS BEEN SUCCESSFULLY PAID AND THE TICKET HAS BEEN BOOKED")
                              print("|                                                                                        ")
                              print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")
                              sql = "insert into amt(Name,total_amt) values(%s,%s)"
                              val = (name,total_amt)
                              cursor.execute(sql, val)
                              mycon.commit()
                              cursor.execute("select S_NO from pd WHERE Name=%s",[name])
                              pnrcode_value=cursor.fetchone()
                              listy=list(pnrcode_value)
                              inty=int(listy[0])
                              pnrcode_value=inty
                              print("YOUR PNR CODE IS : ",pnrcode_value)

                              break
                         else:
                              print("INCORRECT OTP!! TRY AGAIN!!")
               elif confirm=="n":
                    print("exit")

          if mode_trans==3:
              print("X------------CHOOSE UPI PAYMENT METHOD---------------X")
              gpay_trans="GOOGLE PAY"
              paypal_trans="PAYPAL"
              phonepe_trans="PHONEPE "
              paytm_trans="PAYTM"
              print("1)",gpay_trans)
              print("2)",paypal_trans)
              print("3)",phonepe_trans)
              print("4)",paytm_trans)
              upi_trans=int(input("ENTER (1/2/3/4) : "))
              if upi_trans==1:
                  upi_name=gpay_trans
              elif upi_trans==2:
                  upi_name=paypal_trans
              elif upi_trans==3:
                  upi_name=phonepe_trans

              elif upi_trans==4:
                  upi_name=paytm_trans

              if upi_trans==1 or 2 or 3 or 4:
                  upiid_trans=input("ENTER YOUR UPI ID : ")
                  print("X-----------------------------------",upi_name,"----------------------------------------X")
                  print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
                  print("|                                                                                        ")
                  print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
                  print("|                                                                                        ")
                  print("| DATE : ",date,"                                                                        ")
                  print("|                                                                                        ")
                  print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
                  print("|                                                                                        ")

                  confirm=input("Do you agree to the payment?(y/n)")
                  if confirm=="y":
                          mpin=input("ENTER YOUR MPIN : ")
                          time.sleep(2)
                          print("YOUR AMOUNT HAS BEEN SUCCESSFULLY PAID AND THE TICKET HAS BEEN BOOKED")
                          print("|                                                                                        ")
                          print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")

                          sql = "insert into amt(S_NO,total_amt) values(%s,%s)"
                          val = (b_no,total_amt)
                          cursor.execute(sql, val)
                          mycon.commit()

                          sql = "insert into pd(Name,Age,Gender,Phone_Number) values(%s,%s,%s,%s)"
                          val = (name,age,g,p)
                          cursor.execute(sql, val)
                          mycon.commit()

                          print("YOUR PNR CODE IS : ",b_no)


                  elif confirm=="n":
                      print("exit")
                      pass

          x=input("Press any key to go to main page:")

          if x== "^":
               continue

     elif choice==2:
          no_pd=int(input("Enter your PNR Number:"))
          cursor.execute('select * from booking_details where s_no=%s',[no_pd])
          pdetails=cursor.fetchall()

          p_d=list(pdetails)
          print("PNR NO=",p_d[0][0])
          print("NAME=",p_d[0][1])
          print("PHONE NUMBER=",p_d[0][2])
          print("AGE=",p_d[0][3])
          print("GENDER=",p_d[0][4])
          print("DATE OF JOURNEY=",p_d[0][10])
          print("Total amount=",p_d[0][9])
          no_of_passenger = p_d[0][8]

          cursor.execute('select * from td where B_No=%s',[no_pd])
          pdetails=cursor.fetchall()

          p_d=list(pdetails)
          print("Departure=",p_d[0][1])
          print("Destination=",p_d[0][2])
          print("Train Name=",p_d[0][3])
          print("Train time=",p_d[0][4])

          cursor.execute('select * from pd where B_No=%s',[no_pd])
          pdetails=cursor.fetchall()
          p_d=list(pdetails)

          print("\n*****************PASSENGER DETAILS************************")

          for i in range(no_of_passenger):
              print("\t-------------")
              print("\tPassenger : ",i+1)
              print("\t-------------")
              print("\tName =",p_d[i][2])
              print("\tAge=",p_d[i][3])
              print("\tGender=",p_d[i][4])
              print("\tPhone NUmber=",p_d[i][5])


          print("\n********************HAVE A SAFE JOURNEY AHEAD*******************")


          x=input("Press any key to go to main page:")
          if x== "^":
              continue

     elif choice==3:
          import time
          pnr_code=int(input("ENTER PNR NUMBER : "))#1
          travel_date=int(input("ENTER DATE OF TRAVEL(DDMMYYYY) : "))
          cancellation_date=int(input("ENTER DATE OF CANCELLATION(DDMMYYYY) : "))
          date=int(input("ENTER CURRENT DATE : "))



          cursor.execute("select total_amount from booking_details WHERE S_NO=%s",[pnr_code])
          total_amt=cursor.fetchone()
          listy=list(total_amt)
          inty=int(listy[0])
          total_amt=inty
          total_amt=total_amt/2


          if travel_date==cancellation_date:
               print("NO REFUND WILL BE PROVIDED")
               print("                            ")
               print("x----------THANK YOU FOR USING OUR SERVICES---------x")

          elif travel_date!=cancellation_date:
               print("HALF AMOUNT WILL BE DEDUCTED")
               print("                                  ")
               print("X------------PLEASE FOR THE TRANSACTION PAGE TO LOAD------------X")
               time.sleep(3)
               import random
               name_trans=input("Enter your name:")
               name_age=int(input("Enter your age:"))



               print("X------------CHOOSE MODE OF TRANSACTION---------------X")
               print("1) NET BANKING")
               print("2) CREDIT/DEBIT CARD")
               print("3) UPI PAYMENT ")

               mode_trans=int(input("ENTER (1/2/3) : "))

               if mode_trans==1:
                   print("X------------CHOOSE BANK---------------X")
                   sbi_trans="1) STATE BANK OF INDIA"
                   ib_trans="2) INDIAN BANK"
                   iob_trans="3) INDIAN OVERSEAS BANK"
                   cb_trans="4) CANARA BANK"
                   icici_trans="5) ICICI BANK"
                   hdfc_trans="6) HDFC BANK"
                   ub_trans="7) UNION BANK"
                   print(sbi_trans)
                   print(ib_trans)
                   print(iob_trans)
                   print(cb_trans)
                   print(icici_trans)
                   print(hdfc_trans)
                   print(ub_trans)
                   bank_trans=int(input("ENTER (1/2/3/4/5/6/7) : "))
                   if bank_trans==1:
                         bank_name="STATE BANK OF INDIA"
                   elif bank_trans==2:
                       bank_name="INDIAN BANK"
                   elif bank_trans==3:
                       bank_name="INDIAN OVERSEAS BANK"
                   elif bank_trans==4:
                       bank_name="CANARA BANK"
                   elif bank_trans==5:
                       bank_name="ICICI BANK"
                   elif bank_trans==6:
                       bank_name="HDFC BANK"
                   elif bank_trans==7:
                       bank_name="UNION BANK"
                   if bank_trans==1 or 2 or 3 or 4 or 5 or 6 or 7:
                       userid_trans=input("USERNAME : ")
                       password_trans=input("ENTER PASSWORD : ")

                       print("X-----------------------------------",bank_name,"----------------------------------------X")
                       print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
                       print("|                                                                                        ")
                       print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
                       print("|                                                                                        ")
                       print("| DATE : ",date,"                                                                        ")
                       print("|                                                                                        ")
                       print("| USERNAME : ",userid_trans,"                                                            ")
                       print("|                                                                                        ")
                       print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
                       print("|                                                                                        ")

                       confirm=input("Do you agree to the payment?(y/n)")
                       if confirm=="y":
                           while True:
                               print("OTP will be generated ...")
                               time.sleep(2)
                               otp=random.randint(10000,90000)
                               print(otp)
                               time.sleep(2)
                               otp_copy=int(input("ENTER OTP : "))
                               if otp==otp_copy:
                                   print("YOUR AMOUNT HAS BEEN REFUNDED AND THE TICKET HAS BEEN CANCELLED")
                                   print("|                                                                                        ")
                                   print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")
                                   cancel_pd = "delete from pd where B_NO = %s"
                                   val_pd = (pnr_code,)
                                   cursor.execute(cancel_pd,val_pd)
                                   mycon.commit()
                                   cancel_da="delete from da where S_NO = %s"
                                   val_da=(pnr_code,)
                                   cursor.execute(cancel_da,val_da)
                                   mycon.commit()
                                   cancel_td="delete from td where B_NO = %s"
                                   val_td=(pnr_code,)
                                   cursor.execute(cancel_td,val_td)
                                   mycon.commit()

                                   break
                               else:
                                   print("INCORRECT OTP!! TRY AGAIN!!")
                       elif confirm=="n":
                           print("exit")

               if mode_trans==2:
                    cardcode_trans=input("ENTER CARD NUMBER : ")
                    securitycode_trans=input("ENTER 3-DIGIT SECURITY CODE : ")
                    cardholder_trans=input("ENTER CARD HOLDER'S NAME : ")
                    expirydate_trans=int(input("ENTER CARD'S EXPIRY DATE (DDMMYYYY) : "))
                    print("X-----------------------------------","CREDIT/DEBIT CARD","----------------------------------------X")
                    print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
                    print("|                                                                                        ")
                    print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
                    print("|                                                                                        ")
                    print("| DATE : ",date,"                                                                        ")
                    print("|                                                                                        ")
                    print("| CARD NUMBER : ",cardcode_trans,"                                                       ")
                    print("|                                                                                        ")
                    print("| 3 DIGIT SECURITY CODE : ",securitycode_trans,"                                         ")
                    print("|                                                                                        ")
                    print("| NAME OF CARD HOLDER : ",cardholder_trans,"                                             ")
                    print("|                                                                                        ")
                    print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
                    print("|                                                                                        ")

                    confirm=input("Do you agree to the payment?(y/n)")
                    if confirm=="y":
                         while True:
                              print("OTP will be generated ...")
                              time.sleep(2)
                              otp=random.randint(10000,90000)
                              print(otp)
                              time.sleep(2)
                              otp_copy=int(input("ENTER OTP : "))
                              if otp==otp_copy:
                                   print("YOUR AMOUNT HAS BEEN REFUNDED AND THE TICKET HAS BEEN CANCELLED")
                                   print("|                                                                                        ")
                                   print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")
                                   cancel_pd = "delete from pd where B_NO = %s"
                                   val_pd = (pnr_code,)
                                   cursor.execute(cancel_pd,val_pd)
                                   mycon.commit()
                                   cancel_da="delete from da where S_NO = %s"
                                   val_da=(pnr_code,)
                                   cursor.execute(cancel_da,val_da)
                                   mycon.commit()
                                   cancel_td="delete from td where B_NO = %s"
                                   val_td=(pnr_code,)
                                   cursor.execute(cancel_td,val_td)
                                   mycon.commit()
                                   break
                              else:
                                   print("INCORRECT OTP!! TRY AGAIN!!")
                    elif confirm=="n":
                         print("exit")




               if mode_trans==3:
                   print("X------------CHOOSE UPI PAYMENT METHOD---------------X")
                   gpay_trans="GOOGLE PAY"
                   paypal_trans="PAYPAL"
                   phonepe_trans="PHONEPE "
                   paytm_trans="PAYTM"
                   print("1)",gpay_trans)
                   print("2)",paypal_trans)
                   print("3)",phonepe_trans)
                   print("4)",paytm_trans)
                   upi_trans=int(input("ENTER (1/2/3/4) : "))
                   if upi_trans==1:
                       upi_name=gpay_trans
                   elif upi_trans==2:
                       upi_name=paypal_trans
                   elif upi_trans==3:
                       upi_name=phonepe_trans
                   elif upi_trans==4:
                       upi_name=paytm_trans

                   if upi_trans==1 or 2 or 3 or 4:
                       upiid_trans=input("ENTER YOUR UPI ID : ")
                       print("X-----------------------------------",upi_name,"----------------------------------------X")
                       print("| ACKNOWLEDGEMENT NUMBER : xxxxxxxxxxx                                                   ")
                       print("|                                                                                        ")
                       print("| TRANSFER NUMBER : xxxxxxxx                                                             ")
                       print("|                                                                                        ")
                       print("| DATE : ",date,"                                                                        ")
                       print("|                                                                                        ")
                       print("| TOTAL AMOUNT TO BE TRANSFERRED : ",total_amt,"                                         ")
                       print("|                                                                                        ")

                       confirm=input("Do you agree to the payment?(y/n)")
                       if confirm=="y":
                               mpin=input("ENTER YOUR MPIN : ")
                               time.sleep(2)
                               print("YOUR AMOUNT HAS BEEN REFUNDED AND THE TICKET HAS BEEN CANCELLED")
                               print("|                                                                                        ")
                               print("x--------------------THANK YOU FOR USING OUR SERVICES----------------x")
                               cancel_pd = "delete from pd where B_NO = %s"
                               val_pd = (pnr_code,)
                               cursor.execute(cancel_pd,val_pd)
                               mycon.commit()
                               cancel_da="delete from da where S_NO = %s"
                               val_da=(pnr_code,)
                               cursor.execute(cancel_da,val_da)
                               mycon.commit()
                               cancel_td="delete from td where B_NO = %s"
                               val_td=(pnr_code,)
                               cursor.execute(cancel_td,val_td)
                               mycon.commit()

                       elif confirm=="n":
                           print("exit")
                           pass

               x=input("Press any key to go to main page:")
               if x== "^":
                    continue
     elif choice==4:
         break
