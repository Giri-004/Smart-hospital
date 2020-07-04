from tkinter import *
import sqlite3
import sys
con=sqlite3.connect('staff.db')
c=con.cursor()
root=Tk()
root.geometry("1500x1000")
i=0
#cur=c.execute("create table staff1(id INTEGER,name text,Department text,DOB text,Gender text,phone INTEGER,salary INTEGER,address text)")
cur=c.execute("insert into staff1 values(1,'giri','lab','27-10-2000','male',9976,5000,'sathy')")
def Back():
    root.destroy()
    root.quit()
    import Adminpage
def submit():
    root.destroy()
    root.quit()
    mainloop()
def giri():
    ID=Label(root,text="Patient I'd",font=("Helvetica", 16))
    ID.place(x=515, y=200)
    ans=Entry(root,font=("Helvetica", 16))
    ans.place(x=620, y=210)
def details(failures=[]):
    e=ans.get()
    root.destroy()
    cur = con.execute("select * from staff1 where id==1")
    for row in cur:
        i = 1
        a = Label(text="I'd",font=("Helvetica", 14)).grid(row=1)
        b = Label(text=row[0],font=("Helvetica", 16)).grid(row=1, column=1)
        a = Label(text="Name",font=("Helvetica", 14)).grid(row=1)
        b = Label(text=row[1],font=("Helvetica", 16)).grid(row=1, column=1)
        a = Label(text="Department",font=("Helvetica", 14)).grid(row=2)
        b = Label(text=row[2],font=("Helvetica", 16)).grid(row=2, column=1)
        a = Label(text="DOB",font=("Helvetica", 14)).grid(row=3)
        b = Label(text=row[3],font=("Helvetica", 16)).grid(row=3, column=1)
        a = Label(text="Gender",font=("Helvetica", 14)).grid(row=4)
        b = Label(text=row[4],font=("Helvetica", 16)).grid(row=4, column=1)
        a = Label(text="Phone Number",font=("Helvetica", 14)).grid(row=5)
        b = Label(text=row[5],font=("Helvetica", 16)).grid(row=5, column=1)
        a = Label(text="Salary",font=("Helvetica", 14)).grid(row=6)
        b = Label(text=row[6],font=("Helvetica", 16)).grid(row=6, column=1)
        a = Label(text="Address",font=("Helvetica", 14)).grid(row=7)
        b = Label(text=row[7],font=("Helvetica", 16)).grid(row=7, column=1)
        g = Button(text='back', command=Back,font=("Helvetica", 14)).grid(row=8)
        g = Button(text='ok', command=submit,font=("Helvetica", 14)).grid(row=8,column=1)
        if i != 1:
            print("Nothing to show")
        return 0
g = Button(text='Submit', command=details,font=("Helvetica", 14)).place(x=515, y=240)
class details():
    giri()
root.mainloop()
