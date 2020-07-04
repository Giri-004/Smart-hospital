from tkinter import *
import sqlite3
root = Tk()
root.geometry("1500x1000")
con=sqlite3.connect('medicine7.db')
c=con.cursor()
c.execute("create table medicine1(name text,available text)")
c.execute("insert into medicine1 values('paracitamal','10')")
c.execute("insert into medicine1 values('Lotrel','10')")
cur=c.execute("select * from medicine1")
i=0
def Back():
    root.destroy()
    root.quit()
    import Staffpage
for row in cur:
    a=Label(root,text=row[0],font=("Helvetica", 24)).grid(row=i)
    a = Label(root, text=row[1],font=("Helvetica", 24)).grid(row=i,column=1)
    i+=1
s=Button(root,text='back',command=Back,font=("Helvetica", 24)).grid(row=i)
root.mainloop()
class med():
    c.execute("insert into medicine1 values('Lotrel','10')")
    cur = c.execute("select * from medicine1")