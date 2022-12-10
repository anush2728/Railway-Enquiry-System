import mysql.connector
import tkinter as tk
from tkinter import *
from datetime import date
from datetime import time 

def connectionfunc():
    cnxn=mysql.connector.connect(host="localhost",user="root",passwd="PASSWORD",database="mysql")
    c = cnxn.cursor()
    return cnxn, c

def passengerlogin():
    def newpassengerlogin():
        def newpass():
            cnxn, c =connectionfunc()
            usr=str(username.get())
            pas=str(password.get())

            add=("INSERT INTO loginp"
                    "(username,password) "
                    "VALUES (%s, %s)") 
            data=(usr,pas)
            c.execute(add,data)
            cnxn.commit()
            cnxn.close()
            username.delete(0, END)
            password.delete(0, END)
            scs=tk.Label(root,text="Registration Successful!",fg='green',bg="white")
            scs.place(x=140, y= 270)
            displaypassenger()
            
        cnxn, c =connectionfunc()    
        root = tk.Tk()
        root.geometry("500x500")
        root.title("NEW PASSENGER LOGIN")
        root.configure(bg="#209aa7")
        firstrow = tk.Label(root, text="Username", fg='#cc0000',bg='#ffd700' )
        firstrow.place(x=60,y=100,width=90,height=30)
        username = tk.Entry(root,bg="#ffffff")
        username.place(x=190, y=100, width=150,height=30)
        secrow = tk.Label(root, text="Password",fg='#cc0000',bg='#ffd700')
        secrow.place(x=60,y=140,width=90,height=30)
        password = tk.Entry(root,show="*" ,bg="#ffffff")
        password.place(x=190, y=140, width=150,height=30)
        btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=newpass)
        btn.place(x=140,y=200,width=100,height=30)
        root.mainloop() 

    def expassengerlogin():
        def expass():
            flag=0
            usr=str(eusername.get())
            pas=str(epassword.get())
            cnxn, c =connectionfunc()
            chk=("SELECT * FROM LOGINP")
            #dt=(usr,pas)
            c.execute(chk)
            for i in c:
                if usr==i[0] and pas==i[1]:
                    flag=1
                    scs=tk.Label(root,text="Login Successful!",fg='green',bg="white")
                    scs.place(x=140, y= 270)
                    displaypassenger()
            if flag==0:
                scs=tk.Label(root,text="Login failed! RE ENTER",fg='red',bg="white")
                scs.place(x=140, y= 270)
            cnxn.commit()
            cnxn.close()
            eusername.delete(0, END)
            epassword.delete(0, END) 

        root = tk.Tk()
        root.geometry("500x500")
        root.title("EXISTING PASSENGER LOGIN")
        root.configure(bg="#209aa7")
        firstrow = tk.Label(root, text="Username", fg='#cc0000',bg='#ffd700' )
        firstrow.place(x=60,y=100,width=90,height=30)
        eusername = tk.Entry(root,bg="#ffffff")
        eusername.place(x=190, y=100, width=150,height=30)
        secrow = tk.Label(root, text="Password",fg='#cc0000',bg='#ffd700')
        secrow.place(x=60,y=140,width=90,height=30)
        epassword = tk.Entry(root,show="*", bg="#ffffff")
        epassword.place(x=190, y=140, width=150,height=30)
        btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=expass)
        btn.place(x=140,y=200,width=100,height=30)
        root.mainloop() 

    root=tk.Tk()
    root.geometry("500x500")
    root.configure(bg="#209aa7")
    root.title(" PASSENGER LOGIN")
    nbtn=tk.Button(root,text="New Passenger Login", bg='#ffd700' , fg='#cc0000',command=newpassengerlogin)
    nbtn.place(x=90,y=110,width=300,height=40)
    pbtn=tk.Button(root,text="Existing Passenger Login", bg='#ffd700' , fg='#cc0000',command=expassengerlogin)
    pbtn.place(x=90,y=200,width=300,height=40)

def adminlogin():
    def adminc():
        flag=0
        ausr=int(aid.get())
        apas=str(apassword.get())
        cnxn, c =connectionfunc()
        ahk=("SELECT * FROM ADMINCRD")
        c.execute(ahk)
    
        for j in c:
            if ausr==j[0] and apas==j[1]:
                flag=1
                acs=tk.Label(root,text="Login Successful!",fg='green',bg="white")
                acs.place(x=140, y= 270)
                insertadmin()
        if flag==0:
            bcs=tk.Label(root,text="Login failed! RE ENTER",fg='red',bg="white")
            bcs.place(x=140, y= 270)        
        cnxn.commit()
        cnxn.close()
        aid.delete(0, END)
        apassword.delete(0, END) 

    root = tk.Tk()
    root.geometry("500x500")
    root.title("ADMIN LOGIN")
    root.configure(bg="#209aa7")
    firstrow = tk.Label(root, text="Admin ID", fg='#cc0000',bg='#ffd700' )
    firstrow.place(x=60,y=100,width=110,height=30)
    aid = tk.Entry(root,bg="#ffffff")
    aid.place(x=200, y=100, width=150,height=30)
    secrow = tk.Label(root, text="Admin password",fg='#cc0000',bg='#ffd700')
    secrow.place(x=60,y=140,width=110,height=30)
    apassword = tk.Entry(root,show="*", bg="#ffffff")
    apassword.place(x=200, y=140, width=150,height=30)
    btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=adminc)
    btn.place(x=140,y=200,width=100,height=30)
    root.mainloop() 

  
def insertadmin():
    def insertroutemain():
        def insertroute():
            rid = int(route_id.get())
            ori = str(origin.get())
            des= str(dest.get())
            fa=int(fare.get())
            dis=int(dist.get())
            cnxn, c =connectionfunc()
            add=("INSERT INTO ROUTE "
                    "(ROUTE_ID,ORIGIN,DESTINATION,FARE,DISTANCE) "
                    "VALUES (%s, %s,%s,%s,%s)")
            data=(rid,ori,des,fa,dis)
            c.execute(add,data)
            cnxn.commit()
            cnxn.close()
            route_id.delete(0, END)
            origin.delete(0, END)
            dest.delete(0, END)
            fare.delete(0, END)
            dist.delete(0,END)

        cnxn, c =connectionfunc()
        root = tk.Tk()
        root.geometry("500x500")
        root.title("ADD ROUTE DETAILS")
        root.configure(bg="#209aa7")

        box1 = tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
        box1.place(x=90,y=80,width=80,height=30)
        route_id = tk.Entry(root,bg='#ffffff')
        route_id.place(x=200,y=80,width=150,height=30)

        box2 = tk.Label(root, text="Origin",fg="#cc0000",bg="#ffd700")
        box2.place(x=90,y=130,width=80,height=30)
        origin = tk.Entry(root,bg='#ffffff')
        origin.place(x=200,y=130,width=150,height=30)

        box3 = tk.Label(root, text="Destination",fg="#cc0000",bg="#ffd700")
        box3.place(x=90,y=180,width=80,height=30)
        dest = tk.Entry(root,bg='#ffffff')
        dest.place(x=200,y=180,width=150,height=30)

        box4 = tk.Label(root, text="Fare",fg="#cc0000",bg="#ffd700")
        box4.place(x=90,y=230,width=80,height=30)
        fare = tk.Entry(root,bg='#ffffff')
        fare.place(x=200,y=230,width=150,height=30)

        box5 = tk.Label(root, text="Distance",fg="#cc0000",bg="#ffd700")
        box5.place(x=90,y=280,width=80,height=30)
        dist = tk.Entry(root,bg='#ffffff')
        dist.place(x=200,y=280,width=150,height=30)

        btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=insertroute)
        btn.place(x=150,y=350,width=150,height=30)
        root.mainloop()

    def insertstationmain():
        def insertstation():
            rid = int(route_id.get())
            sid = str(station_id.get())
            sname= str(station_name.get())
            cnxn, c =connectionfunc()
            add=("INSERT INTO STATION "
                    "(ROUTE_ID,STATION_ID,STATION_NAME) "
                    "VALUES (%s, %s,%s)")
            data=(rid,sid,sname)
            c.execute(add,data)
            cnxn.commit()
            cnxn.close()
            route_id.delete(0, END)
            station_id.delete(0, END)
            station_name.delete(0, END)
            

        cnxn, c =connectionfunc()
        root = tk.Tk()
        root.geometry("500x500")
        root.title("ADD STATION DETAILS")
        root.configure(bg="#209aa7")

        box1 = tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
        box1.place(x=90,y=80,width=80,height=30)
        route_id = tk.Entry(root,bg='#ffffff')
        route_id.place(x=200,y=80,width=150,height=30)

        box2 = tk.Label(root, text="Station ID",fg="#cc0000",bg="#ffd700")
        box2.place(x=90,y=130,width=80,height=30)
        station_id = tk.Entry(root,bg='#ffffff')
        station_id.place(x=200,y=130,width=150,height=30)

        box3 = tk.Label(root, text="Station Name",fg="#cc0000",bg="#ffd700")
        box3.place(x=90,y=180,width=80,height=30)
        station_name = tk.Entry(root,bg='#ffffff')
        station_name.place(x=200,y=180,width=150,height=30)


        btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=insertstation)
        btn.place(x=150,y=300,width=150,height=30)
        root.mainloop()


    def inserttrainmain():
        def inserttrain():
            tid=int(t_no.get())
            rid = int(r_id.get())
            tna = str(t_name.get())
            o= str(origin.get())
            d= str(desti.get())
            dtime= str(dep_time.get())
            atime= str(arr_time.get())
            date1= str(date.get())
            cap= int(capacity.get())
            cnxn, c =connectionfunc()
            add=("INSERT INTO TRAIN "
                    "(TRAIN_NO,ROUTE_ID,TRAIN_NAME,ORIGIN,DESTINATION,DEP_TIME,ARR_TIME,TRAVEL_DATE,CAPACITY) "
                    "VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)")
            data=(tid,rid,tna,o,d,dtime,atime,date1,cap)
            c.execute(add,data)
            cnxn.commit()
            cnxn.close()
            t_no.delete(0, END)
            r_id.delete(0, END)
            t_name.delete(0, END)
            origin.delete(0, END)
            desti.delete(0, END)
            dep_time.delete(0, END)
            arr_time.delete(0, END)
            date.delete(0, END)
            capacity.delete(0, END)

        cnxn, c =connectionfunc()
        root = tk.Tk()
        root.geometry("500x500")
        root.title("ADD TRAIN DETAILS")
        root.configure(bg="#209aa7")

        box1 = tk.Label(root, text="Train No.",fg="#cc0000",bg="#ffd700")
        box1.place(x=40,y=20,width=100,height=30)
        t_no = tk.Entry(root,bg='#ffffff')
        t_no.place(x=170,y=20,width=200,height=30)

        box2 = tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
        box2.place(x=40,y=60,width=100,height=30)
        r_id = tk.Entry(root,bg='#ffffff')
        r_id.place(x=170,y=60,width=200,height=30)

        box3 = tk.Label(root, text="Train Name",fg="#cc0000",bg="#ffd700")
        box3.place(x=40,y=100,width=100,height=30)
        t_name = tk.Entry(root,bg='#ffffff')
        t_name.place(x=170,y=100,width=200,height=30)

        box4 = tk.Label(root, text="Origin",fg="#cc0000",bg="#ffd700")
        box4.place(x=40,y=140,width=100,height=30)
        origin = tk.Entry(root,bg='#ffffff')
        origin.place(x=170,y=140,width=200,height=30)

        box5 = tk.Label(root, text="Destination",fg="#cc0000",bg="#ffd700")
        box5.place(x=40,y=180,width=100,height=30)
        desti = tk.Entry(root,bg='#ffffff')
        desti.place(x=170,y=180,width=200,height=30)

        box6 = tk.Label(root, text="Departure Time",fg="#cc0000",bg="#ffd700")
        box6.place(x=40,y=220,width=100,height=30)
        dep_time = tk.Entry(root,bg='#ffffff')
        dep_time.place(x=170,y=220,width=200,height=30)

        box7 = tk.Label(root, text="Arrival Time",fg="#cc0000",bg="#ffd700")
        box7.place(x=40,y=260,width=100,height=30)
        arr_time = tk.Entry(root,bg='#ffffff')
        arr_time.place(x=170,y=260,width=200,height=30)

        box8 = tk.Label(root, text="Date",fg="#cc0000",bg="#ffd700")
        box8.place(x=40,y=300,width=100,height=30)
        date = tk.Entry(root,bg='#ffffff')
        date.place(x=170,y=300,width=200,height=30)

        box9 = tk.Label(root, text="Capacity",fg="#cc0000",bg="#ffd700")
        box9.place(x=40,y=340,width=100,height=30)
        capacity = tk.Entry(root,bg='#ffffff')
        capacity.place(x=170,y=340,width=200,height=30)

        btn = tk.Button(root, text="Enter", bg='#e0bed3' , fg='#cc0000', command=inserttrain)
        btn.place(x=120,y=400,width=100,height=30)
        root.mainloop()

    cnxn, c =connectionfunc()
    root = tk.Tk()
    root.geometry("500x500")
    root.title("ADMIN UPDATE OPTIONS")
    root.configure(bg="#209aa7")
    btn1 = tk.Button(root, text="Update Route", bg='#ffd700' , fg='#cc0000', command=insertroutemain)
    btn1.place(x=90,y=110,width=300,height=40)
    btn2 = tk.Button(root, text="Update Station", bg='#ffd700' , fg='#cc0000', command=insertstationmain)
    btn2.place(x=90,y=200,width=300,height=40)
    btn3 = tk.Button(root, text="Update Train", bg='#ffd700' , fg='#cc0000', command=inserttrainmain)
    btn3.place(x=90,y=290,width=300,height=40)
    root.mainloop()

def displaypassenger():
    def display_routes():
        root = tk.Tk()
        root.title("AVAILABLE ROUTES")
        root.geometry('600x600')
        root.configure(bg="#209aa7")
        root.resizable(width=False, height=False)
        label1=tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
        label1.place(x=10,y=30,width=100,height=30)
        label2=tk.Label(root, text="Origin",fg="#cc0000",bg="#ffd700")
        label2.place(x=130,y=30,width=100,height=30)
        label3=tk.Label(root, text="Destination",fg="#cc0000",bg="#ffd700")
        label3.place(x=250,y=30,width=100,height=30)
        label4=tk.Label(root, text="Distance",fg="#cc0000",bg="#ffd700")
        label4.place(x=370,y=30,width=100,height=30)
        label5=tk.Label(root, text="Fare",fg="#cc0000",bg="#ffd700")
        label5.place(x=490,y=30,width=100,height=30)
        
        lb1=tk.Listbox(root,bg='#ffffff')
        lb1.place(x=10,y=70,width=100,height=500)
        lb2=tk.Listbox(root,bg='#ffffff')
        lb2.place(x=130,y=70,width=100,height=500)
        lb3=tk.Listbox(root,bg='#ffffff')
        lb3.place(x=250,y=70,width=100,height=500)
        lb4=tk.Listbox(root,bg='#ffffff')
        lb4.place(x=370,y=70,width=100,height=500)
        lb5=tk.Listbox(root,bg='#ffffff')
        lb5.place(x=490,y=70,width=100,height=500)
        
        cnxn, c =connectionfunc()
        c.execute("SELECT * FROM ROUTE")
        for i in c:
            lb1.insert('end', i[0])
            lb2.insert('end', i[1])
            lb3.insert('end', i[2])
            lb4.insert('end', i[3])
            lb5.insert('end', i[4])
        root.mainloop()
        cnxn.close()

    def display_stations():
        root = tk.Tk()
        root.title("STATIONS COVERED")
        root.geometry('600x600')
        root.configure(bg="#209aa7")
        root.resizable(width=False, height=False)
        label1=tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
        label1.place(x=70,y=30,width=100,height=30)
        label2=tk.Label(root, text="Station ID",fg="#cc0000",bg="#ffd700")
        label2.place(x=240,y=30,width=100,height=30)
        label3=tk.Label(root, text="Station Name",fg="#cc0000",bg="#ffd700")
        label3.place(x=410,y=30,width=100,height=30)
        
        lb1=tk.Listbox(root,bg='#ffffff')
        lb1.place(x=70,y=70,width=100,height=500)
        lb2=tk.Listbox(root,bg='#ffffff')
        lb2.place(x=240,y=70,width=100,height=500)
        lb3=tk.Listbox(root,bg='#ffffff')
        lb3.place(x=410,y=70,width=100,height=500)
        
        cnxn, c =connectionfunc()
        c.execute("SELECT * FROM STATION")
        for i in c:
            lb1.insert('end', i[0])
            lb2.insert('end', i[1])
            lb3.insert('end', i[2])
        root.mainloop()
        cnxn.close()

    def outer_calc():
        def calc():

            root = tk.Tk()
            root.title("BOOKING DETAILS")
            root.geometry('600x600')
            root.configure(bg="#209aa7")
            root.resizable(width=False, height=False)
            label1=tk.Label(root, text="Passenger Name",fg="#cc0000",bg="#ffd700")
            label1.place(x=40,y=70,width=150,height=30)
            label3=tk.Label(root, text="Train No.",fg="#cc0000",bg="#ffd700")
            label3.place(x=40,y=120,width=150,height=30)
            label4=tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
            label4.place(x=40,y=170,width=150,height=30)
            label5=tk.Label(root, text="No. of Passengers",fg="#cc0000",bg="#ffd700")
            label5.place(x=40,y=220,width=150,height=30)
            label6=tk.Label(root, text="Origin",fg="#cc0000",bg="#ffd700")
            label6.place(x=40,y=270,width=150,height=30)
            label7=tk.Label(root, text="Destination",fg="#cc0000",bg="#ffd700")
            label7.place(x=40,y=320,width=150,height=30)
            label8=tk.Label(root, text="Date",fg="#cc0000",bg="#ffd700")
            label8.place(x=40,y=370,width=150,height=30)
            label9=tk.Label(root, text="Time",fg="#cc0000",bg="#ffd700")
            label9.place(x=40,y=420,width=150,height=30)
            label10=tk.Label(root, text="Total Fare",fg="#cc0000",bg="#ffd700")
            label10.place(x=40,y=470,width=150,height=30)
            
            lb1=tk.Listbox(root,bg='#ffffff')
            lb1.place(x=220,y=70,width=250,height=30)
            lb3=tk.Listbox(root,bg='#ffffff')
            lb3.place(x=220,y=120,width=250,height=30)
            lb4=tk.Listbox(root,bg='#ffffff')
            lb4.place(x=220,y=170,width=250,height=30)
            lb5=tk.Listbox(root,bg='#ffffff')
            lb5.place(x=220,y=220,width=250,height=30)
            lb6=tk.Listbox(root,bg='#ffffff')
            lb6.place(x=220,y=270,width=250,height=30)
            lb7=tk.Listbox(root,bg='#ffffff')
            lb7.place(x=220,y=320,width=250,height=30)
            lb8=tk.Listbox(root,bg='#ffffff')
            lb8.place(x=220,y=370,width=250,height=30)
            lb9=tk.Listbox(root,bg='#ffffff')
            lb9.place(x=220,y=420,width=250,height=30)
            lb10=tk.Listbox(root,bg='#ffffff')
            lb10.place(x=220,y=470,width=250,height=30)
            cnxn ,c=connectionfunc()
            rt=int(ur_id.get())
            no=int(unop.get())
            tid=int(utid.get())
            name=str(namep.get())
            print("name:",name)
            print("rt:",rt)
            fl=0
            cal=("SELECT * FROM ROUTE")
            c.execute(cal)
            for k in c:
                if k[0]==rt:
                    fl=1
                    amt=k[3]*no
            if fl==0:
                print("error")
            lb1.insert('end',name)
            lb3.insert('end', tid)
            lb4.insert('end', rt)
            lb5.insert('end', no)
            trn=("SELECT * FROM TRAIN ")
            c.execute(trn)
            for v in c:
                if v[1]==rt and v[0]==tid:
                    lb6.insert('end', v[3])
                    lb7.insert('end', v[4])
                    lb8.insert('end', v[5])
                    lb9.insert('end',v[6])
            lb10.insert('end', amt)
            cnxn.close()
            rt.delete(0, END)

        root = tk.Tk()
        root.title("DETAILS")
        root.geometry('500x500')
        root.configure(bg="#209aa7")
        root.resizable(width=False, height=False)

        b1 = tk.Label(root, text="Enter Train No. to Book",fg="#cc0000",bg="#ffd700")
        b1.place(x=100,y=40,width=280,height=30)
        utid = tk.Entry(root,bg='#ffffff')
        utid.place(x=140,y=90,width=200,height=30)

        b1 = tk.Label(root, text="Enter Passenger Name",fg="#cc0000",bg="#ffd700")
        b1.place(x=100,y=150,width=280,height=30)
        namep = tk.Entry(root,bg='#ffffff')
        namep.place(x=140,y=200,width=200,height=30)

        button1=tk.Button(root, text="Display Details", bg='#ffd700' , fg='#cc0000', command=calc)
        button1.place(x=150,y=300,width=180,height=30)

    def outerdisplay_trains():
        def display_trains():
            root = tk.Tk()
            root.title("AVAILABLE TRAINS")
            root.geometry('1000x700')
            root.configure(bg="#209aa7")
            root.resizable(width=False, height=False)
            label1=tk.Label(root, text="Train No.",fg="#cc0000",bg="#ffd700")
            label1.place(x=120,y=20,width=100,height=30)
            label2=tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
            label2.place(x=10,y=20,width=100,height=30)
            label3=tk.Label(root, text="Train Name",fg="#cc0000",bg="#ffd700")
            label3.place(x=230,y=20,width=100,height=30)
            label4=tk.Label(root, text="Origin",fg="#cc0000",bg="#ffd700")
            label4.place(x=340,y=20,width=100,height=30)
            label5=tk.Label(root, text="Destination",fg="#cc0000",bg="#ffd700")
            label5.place(x=450,y=20,width=100,height=30)
            label6=tk.Label(root, text="Depart.Time",fg="#cc0000",bg="#ffd700")
            label6.place(x=560,y=20,width=100,height=30)
            label7=tk.Label(root, text="Arrival Time",fg="#cc0000",bg="#ffd700")
            label7.place(x=670,y=20,width=100,height=30)
            label8=tk.Label(root, text="Date",fg="#cc0000",bg="#ffd700")
            label8.place(x=780,y=20,width=100,height=30)
            label9=tk.Label(root, text="Capacity",fg="#cc0000",bg="#ffd700")
            label9.place(x=890,y=20,width=100,height=30)
            
            lb1=tk.Listbox(root,bg='#ffffff')
            lb1.place(x=10,y=70,width=100,height=510)
            lb2=tk.Listbox(root,bg='#ffffff')
            lb2.place(x=120,y=70,width=100,height=510)
            lb3=tk.Listbox(root,bg='#ffffff')
            lb3.place(x=230,y=70,width=100,height=510)
            lb4=tk.Listbox(root,bg='#ffffff')
            lb4.place(x=340,y=70,width=100,height=510)
            lb5=tk.Listbox(root,bg='#ffffff')
            lb5.place(x=450,y=70,width=100,height=510)
            lb6=tk.Listbox(root,bg='#ffffff')
            lb6.place(x=560,y=70,width=100,height=510)
            lb7=tk.Listbox(root,bg='#ffffff')
            lb7.place(x=670,y=70,width=100,height=510)
            lb8=tk.Listbox(root,bg='#ffffff')
            lb8.place(x=780,y=70,width=100,height=510)
            lb9=tk.Listbox(root,bg='#ffffff')
            lb9.place(x=890,y=70,width=100,height=510)

            temp=0
            rt=int(ur_id.get())
            print("rt" , rt)
            no=int(unop.get())
            cnxn, c =connectionfunc()
            trn=("SELECT * FROM TRAIN ")
            c.execute(trn)
            for v in c:
                if v[1]==rt:
                    temp=1
                    if( v[8]-no)>0:
                        lb1.insert('end', v[1])
                        lb2.insert('end', v[0])
                        lb3.insert('end', v[2])
                        lb4.insert('end', v[3])
                        lb5.insert('end', v[4])
                        lb6.insert('end', v[5])
                        lb7.insert('end', v[6])
                        lb8.insert('end', v[7])
                        lb9.insert('end', v[8])
                    else:
                        war=tk.Label(root,text="No available seats!",fg="#cc0000",bg="#ffd700")
                        war.place(x=230,y=600, width=400,height=30)

            if temp==0:

                label10=tk.Label(root, text="No Trains Found",fg="#cc0000",bg="#ffd700")
                label10.place(x=230,y=600,width=400,height=30)
            
            root.mainloop()
            cnxn.close()
            ur_id.delete(0, END)
            unop.delete(0, END)

        rt=int(ur_id.get())
        print("rt:",rt)
        display_trains()
        ur_id.delete(0,END)

    cnxn, c =connectionfunc()
    root = tk.Tk()
    root.geometry("600x600")
    root.title("BOOKING")
    root.configure(bg="#209aa7")
    bttn1 = tk.Button(root, text="Avaialble Routes", bg='#ffd700' , fg='#cc0000', command=display_routes)
    bttn1.place(x=130,y=20,width=300,height=40)
    bttn2 = tk.Button(root, text="Stations Covered", bg='#ffd700' , fg='#cc0000', command=display_stations)
    bttn2.place(x=130,y=80,width=300,height=40)

    msg1=tk.Label(root, text="*** Check Available Routes and Stations Covered Before Booking ***",fg="#cc0000",bg="#ffffff")
    msg1.place(x=0,y=140,width=600,height=30)

    msg2=tk.Label(root, text="Enter Following Details to Check Trains",fg="#cc0000",bg="#ffd700")
    msg2.place(x=70,y=190,width=450,height=30)

    bx1 = tk.Label(root, text="Route ID",fg="#cc0000",bg="#ffd700")
    bx1.place(x=90,y=240,width=180,height=30)
    ur_id = tk.Entry(root,bg='#ffffff')
    ur_id.place(x=310,y=240,width=180,height=30)

    bx6 = tk.Label(root, text="No. of Passengers",fg="#cc0000",bg="#ffd700")
    bx6.place(x=90,y=310,width=180,height=30)
    unop = tk.Entry(root,bg='#ffffff')
    unop.place(x=310,y=310,width=180,height=30)

    bttn3=tk.Button(root, text="Check Trains", bg='#ffd700' , fg='#cc0000', command=outerdisplay_trains)
    bttn3.place(x=230,y=450,width=100,height=25)

    bttn4=tk.Button(root, text="Proceed To Next Step", bg='#ffd700' , fg='#cc0000', command=outer_calc)
    bttn4.place(x=230,y=500,width=150,height=25)
 
cnxn, c =connectionfunc()
root=tk.Tk()
root.geometry("500x500")
root.title("LOGIN")
root.configure(bg="#209aa7")
msg=tk.Label(root, text="WELCOME TO RAILWAY MANAGEMENT SYSTEM",fg="#cc0000")
msg.place(x=0,y=70,width=500,height=30)
abtn=tk.Button(root,text="ADMIN", bg='#ffd700' , fg='#cc0000',command=adminlogin)
abtn.place(x=90,y=160,width=300,height=40)
pbtn=tk.Button(root,text="PASSENGER", bg='#ffd700' , fg='#cc0000',command=passengerlogin)
pbtn.place(x=90,y=270,width=300,height=40)
root.mainloop()