from tkinter import *
import sqlite3
con=sqlite3.connect('operation.db')
c=con.cursor()
#c.execute("create table operation1(date text,time text,venue text)")
#c.execute("insert into operation1 values('07.03.2019','10.30AM','operation theater')")
#cds=c.execute("select * from operation1")
root=Tk()
root.geometry("1500x1000")
def back():
    root.destroy()
    root.quit()
    import Userpage
for row in cds:
    lable1 = Label(text=' your operation schedule is', height=1,font=("Helvetica", 14)).grid()
    lable1 = Label(text='Date:', bg='light blue', height=1,width=10,font=("Helvetica", 14)).grid(row=1)
    lable1 = Label(text=row[0], bg='light blue', height=1,width=15,font=("Helvetica", 14)).grid(row=1,column=1)
    lable1 = Label(text='Time', bg='light blue', height=1,width=10,font=("Helvetica", 14)).grid(row=2)
    lable1 = Label(text=row[1], bg='light blue', height=1,width=15,font=("Helvetica", 14)).grid(row=2,column=1)
    lable1 = Label(text='Venue:', bg='light blue', height=1,width=10,font=("Helvetica", 14)).grid(row=3)
    lable1 = Label(text=row[2], bg='light blue', height=1,width=15,font=("Helvetica", 14)).grid(row=3,column=1)
    medicine = Button(root, text="back", command=back, bg='blue',font=("Helvetica", 14)).grid(row=4,column=1)
    root.mainloop()