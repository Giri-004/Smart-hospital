# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:10:30 2019

@author: Giri
"""
from tkinter import *
import sqlite3
con=sqlite3.connect('appoinment.db')
c=con.cursor()
root=Tk()   
i=0
#cur=c.execute("create table appoinment1(id INTEGER,name text,Department text,appoinment_time text,DATE TEXT,status text,venue text)")
cur=c.execute("insert into appoinment1 values(1,'Dr.Mythily','surgerey','12.30pm','16.03.2019','apporved','mainhall')")
cur=c.execute("insert into appoinment1 values(1,'Dr.Mythily','surgerey','4.00pm','18.03.2019','pending','null')")
cur=c.execute("insert into appoinment1 values(1,'Dr.Mythily','surgerey','4.00pm','18.03.2019','pending','null')")
cur=c.execute("select * from appoinment1")
for row in cur:
        lable1 = Label(text='Doctor ID:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=50)
        lable1 = Label(text=row[0], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=50)
        lable1 = Label(text='Name:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=100)
        lable1 = Label(text=row[1], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=100)
        lable1 = Label(text='Speclist:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=150)
        lable1 = Label(text=row[2], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=150)
        lable1 = Label(text='Appoinmenr_time:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=200)
        lable1 = Label(text=row[3], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=200)
        lable1 = Label(text='Appoinmenr_date:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=250)
        lable1 = Label(text=row[4], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=250)
        lable1 = Label(text='status:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=300)
        lable1 = Label(text=row[5], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=300)
        lable1 = Label(text='venue', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=350)
        lable1 = Label(text=row[6], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=350)
        
        i=i+350
lable1 = Button( text='OK',height=1,font=("Helvetica", 14))
lable1.place(x=200, y=400)
root.mainloop()
