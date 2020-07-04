from tkinter import *
root=Tk()
root.geometry("1500x1000")
import sqlite3
con=sqlite3.connect('staff1.db')
c=con.cursor()
#cur=c.execute("create table details1(id INTEGER,name text,age text,sex text,blood_group text,address text,phone INTEGER,password text)")
cur=c.execute("insert into details1 values(1,'ragul','35','male','B+','erode',9976512521,'sathy')")
cu=c.execute("select * from details1")

for row in cu:
    name = Label(root, text="Name:",font=("Helvetica", 14)).grid(row=1)
    name1 = Label(root,text=row[0],font=("Helvetica", 14)).grid(row=1, column=1)
    Age = Label(root, text="Age:",font=("Helvetica", 14)).grid(row=2)
    Sex1 = Label(root,font=("Helvetica", 14),text=row[1]).grid(row=2, column=1)
    Sex = Label(root, text="sex:",font=("Helvetica", 14)).grid(row=3)
    Sex1 = Label(root,font=("Helvetica", 14),text=row[2]).grid(row=3, column=1)
    Blood_Group = Label(root, text="Blood_Group:",font=("Helvetica", 14)).grid(row=4)
    Blood_Group1 = Label(root,font=("Helvetica", 14),text=row[3]).grid(row=4, column=1)
    Address = Label(root, text="Address:",font=("Helvetica", 14)).grid(row=5)
    Address1 =Label(root,font=("Helvetica", 14),text=row[4]).grid(row=5, column=1)
    Phone_NO = Label(root, text="Phone_No:",font=("Helvetica", 14)).grid(row=6)
    Phone_NO1 = Label(root,font=("Helvetica", 14),text=row[5]).grid(row=6, column=1)
    Password = Label(root, text="Password:",font=("Helvetica", 14)).grid(row=7)
    Password1 = Label(root,font=("Helvetica", 14),text=row[6]).grid(row=7, column=1)


    def Back():
        root.destroy()
        root.quit()
        from Userpage import userpage
        next = userpage()


    def Edit():
        root.destroy()
        root.quit()
        from Update import update
        next = update()


    back = Button(root, text='Back', bg='light blue', command=Back,font=("Helvetica", 14)).grid(row=8)
    back = Button(root, text='Edit', bg='light blue', command=Edit,font=("Helvetica", 14)).grid(row=8,column=1)
root.mainloop()