from tkinter import *
import sqlite3
con=sqlite3.connect('operation.db')
c=con.cursor()
#c.execute("create table lab1(bloo_group text,time text,venue text)")
c.execute("insert into lab1 values('B+','10.30AM','operation theater')")
cds=c.execute("select * from lab1")
root=Tk()
def back():
    root.destroy()
    root.quit()
    import Userpage
for row in cds:
    lable1 = Label(text=' your Lab details is', height=1).grid()
    lable1 = Label(text='Blood_group', bg='light blue', height=1,width=15).grid(row=1)
    lable1 = Label(text=row[0], bg='light blue', height=1,width=15).grid(row=1,column=1)
    lable1 = Label(text='Time', bg='light blue', height=1,width=15).grid(row=2)
    lable1 = Label(text=row[1], bg='light blue', height=1,width=15).grid(row=2,column=1)
    lable1 = Label(text='Venue:', bg='light blue', height=1,width=15).grid(row=3)
    lable1 = Label(text=row[2], bg='light blue', height=1,width=15).grid(row=3,column=1)
    medicine = Button(root, text="back", command=back, bg='blue').grid(row=4,column=1)
    root.mainloop()