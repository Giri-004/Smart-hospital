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
root.geometry("1500x1000")
i=0
#cur=c.execute("create table appoinment6(id INTEGER,name text,Department text,appoinment_time text,appoinment_date text)")
cur=c.execute("insert into appoinment6 values(1,'ragul','feaver','12.30pm','16.03.2019')")
cur=c.execute("insert into appoinment6 values(1,'deepak','back pain','4.00pm','18.03.2019')")
cur=c.execute("insert into appoinment6 values(1,'kesavan','short temper','4.00pm','18.03.2019')")
cur=c.execute("select * from appoinment6")
def sub():
    root.destroy()
    root.quit()
    import Doctorpage
for row in cur:
        lable1 = Label(text='Doctor ID:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=50)
        lable1 = Label(text=row[0], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=50)
        lable1 = Label(text='Name:', height=1,font=("Helvetica", 14))
        lable1.place(x=100+i, y=100)
        lable1 = Label(text=row[1], height=1,font=("Helvetica", 14))
        lable1.place(x=300+i, y=100)
        lable1 = Label(text='reson', height=1,font=("Helvetica", 14))
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
        lable1 = Button( text='apporve',height=1,font=("Helvetica", 14),command=sub)
        lable1.place(x=200+i, y=400)
        
        i=i+350

root.mainloop()
