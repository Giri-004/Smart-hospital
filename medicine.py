from tkinter import *
import sqlite3
con=sqlite3.connect('operation.db')
c=con.cursor()
#c.execute("create table medicine2(date text,time text)")
c.execute("insert into medicine2 values('Lipitor','morning,evening')")
c.execute("insert into medicine2 values('tenormin','night')")
cds=c.execute("select * from medicine2")
root=Tk()
root.geometry("1500x1000")
i=0
def back():
    root.destroy()
    root.quit()
    import Userpage
lable1 = Label(text=' your medicine details is', height=1,font=("Helvetica", 14)).grid()
lable1 = Label(text='medicine name', bg='blue', height=1,width=15,font=("Helvetica", 14)).grid(row=1)
lable1 = Label(text='time', bg='blue', height=1,width=15,font=("Helvetica", 14)).grid(row=1,column=1)
for row in cds:
    lable1 = Label(text=row[0], bg='light blue', height=1,width=15,font=("Helvetica", 14)).grid(row=2+i)
    lable1 = Label(text=row[1], bg='light blue', height=1,width=15,font=("Helvetica", 14)).grid(row=2+i,column=1)
    i+=1
medicine = Button(root, text="back", command=back, bg='blue',font=("Helvetica", 14)).grid(row=3+i,column=1)
root.mainloop()