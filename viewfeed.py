from tkinter import *
import sqlite3
root=Tk()
def back():
    root.destroy()
    root.quit()
    import Adminpage
con=sqlite3.connect('staff.db')
c=con.cursor()
i=0
cur=c.execute("create table feedback(id INTEGER,message text)")
cur=c.execute("insert into feedback values(1,'Hospital is good')")
cur=c.execute("insert into feedback values(90,'Hospital is not bad')")
cursor=c.execute("select * from feedback")
for row in cursor:
    a=Label(root,text=row[0]).grid(row=i)
    a = Label(root, text=row[1]).grid(row=i,column=1)
    i+=1
Button(root,text='back',command=back).grid(row=i)
root.mainloop()