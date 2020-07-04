from tkinter import *
import sqlite3
con=sqlite3.connect('staff2.db')
c=con.cursor()
root=Tk()
root.geometry("1500x1000")
i=0
#cur=c.execute("create table staff1(id INTEGER,name text,Department text,DOB text,Gender text,phone INTEGER,salary INTEGER,address text)")
cur=c.execute("insert into staff1 values(1,'deepak','lab','27-10-2000','male',9976512521,5000,'sathy')")
def Back():
    root.destroy()
    root.quit()
    from Adminpage import page
    next = page()
a=Label(root,text="Staff I'd",font=("Helvetica", 16)).grid(row=0)
d=Entry(root,font=("Helvetica", 16))
d.grid(row=0,column=1)

def details():

    s=d.get()
    s=9
    root.destroy()
    cur = c.execute("select * from staff1 where id=1")
    for row in cur:
        i=1
        a = Label(text="I'd",font=("Helvetica", 16)).grid(row=1)
        b = Label(text=row[0],font=("Helvetica", 16)).grid(row=1, column=1)
        a  =Label(text="Name",font=("Helvetica", 16)).grid(row=1)
        b =Label(text=row[1],font=("Helvetica", 16)).grid(row=1,column=1)
        a = Label(text="Department",font=("Helvetica", 16)).grid(row=2)
        b = Label(text=row[2],font=("Helvetica", 16)).grid(row=2, column=1)
        a = Label(text="DOB",font=("Helvetica", 16)).grid(row=3)
        b = Label(text=row[3],font=("Helvetica", 16)).grid(row=3, column=1)
        a = Label(text="Gender",font=("Helvetica", 16)).grid(row=4)
        b = Label(text=row[4],font=("Helvetica", 16)).grid(row=4, column=1)
        a = Label(text="Phone Number",font=("Helvetica", 16)).grid(row=5)
        b = Label(text=row[5],font=("Helvetica", 16)).grid(row=5, column=1)
        a = Label(text="Salary",font=("Helvetica", 16)).grid(row=6)
        b = Label(text=row[6],font=("Helvetica", 16)).grid(row=6, column=1)
        a = Label(text="Address",font=("Helvetica", 16)).grid(row=7)
        b = Label(text=row[7],font=("Helvetica", 16)).grid(row=7, column=1)
        g=Button(text='back',command=Back,font=("Helvetica", 16)).grid(row=8)
    if i != 1:
        print("Nothing to show")
def ok():

    root.quit()
    import manage_staff_details
    next=manage_staff_details
def Update():

    root.quit()
    r=Tk()
    l=Label(r,text="successfully add",font=("Helvetica", 16)).grid(row=1)
    b=Button(r,text='ok',command=ok,font=("Helvetica", 16)).grid(row=2)
    r.mainloop()
def db():
    root.quit()
    cur = c.execute("insert into staff values('b.get()','c.get()','d.get()','d.get()','d.get()','d.get()','h.get()','i.get()')")
    Update()
def add():
    root.destroy()
    a = Label(text="I'd",font=("Helvetica", 16)).grid(row=1)
    b = Entry(font=("Helvetica", 16))
    b.grid(row=1, column=1)
    a = Label(text="Name",font=("Helvetica", 16)).grid(row=1)
    c = Entry(font=("Helvetica", 16))
    c.grid(row=1, column=1)
    a = Label(text="Department",font=("Helvetica", 16)).grid(row=2)
    d = Entry(font=("Helvetica", 16))
    d.grid(row=2, column=1)
    a = Label(text="DOB",font=("Helvetica", 16)).grid(row=3)
    e = Entry(font=("Helvetica", 16))
    e.grid(row=3, column=1)
    a = Label(text="Gender",font=("Helvetica", 16)).grid(row=4)
    f = Entry(font=("Helvetica", 16))
    f.grid(row=4, column=1)
    a = Label(text="Phone Number",font=("Helvetica", 16)).grid(row=5)
    g= Entry(font=("Helvetica", 16))
    g.grid(row=5, column=1)
    a = Label(text="Salary",font=("Helvetica", 16)).grid(row=6)
    h = Entry(font=("Helvetica", 16))
    h.grid(row=6, column=1)

    Button(text="Add",command=db,font=("Helvetica", 16)).grid(row=8)
Button(root,text="submit",command=details,font=("Helvetica", 16)).grid(row=1)
Button(root,text="Add person",command=add,font=("Helvetica", 16)).grid(row=1,column=1)
root.mainloop()