from tkinter import *
root=Tk()
root.geometry("1500x1000")
def submit():
    root.destroy()
    root.quit()
    from pharmacy1 import pharmacy1
    next=pharmacy1()
def back():
    root.destroy()
    root.quit()
    from Staffpage import Staffpage
    next=Staffpage()
class pharmacy():
    first=Label(root,text="ID",font=("Helvetica", 16)).grid(row=0)
    a=Entry(root,font=("Helvetica", 16)).grid(row=0,column=1)
    back = Button(text="Back", command=back,font=("Helvetica", 16)).grid(row=2, column=0)
    submit = Button(text="Submit", command=submit,font=("Helvetica", 16)).grid(row=2, column=1)
    root.mainloop()