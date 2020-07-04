from tkinter import *
root=Tk()
root.geometry("1500x1000")
def submit():
    root.destroy()
    root.quit()
    from operation_scheduling1 import operation_scheduling1
    next=operation_scheduling1()
def back():
    root.destroy()
    root.quit()
    from Doctorpage import Doctorpage
    next=Doctorpage()
class operation_scheduling():
    first=Label(root,text="ID",font=("Helvetica", 14)).place(x=400,y=200)
    a=Entry(root,font=("Helvetica", 14)).place(x=450,y=200)
    back = Button(text="Back", command=back,font=("Helvetica", 14)).place(x=400,y=250)
    submit = Button(text="Submit", command=submit,font=("Helvetica", 14)).place(x=600,y=250)
    root.mainloop()