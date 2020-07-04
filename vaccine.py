from tkinter import *
root=Tk()
root.geometry("1500x1000")
def submit():
    root.destroy()
    root.quit()
def back():
    root.destroy()
    root.quit()
    from Doctorpage import Doctorpage
    next = Doctorpage()
class vaccine():
    first=Label(root,text="Name of the Injection",font=("Helvetica", 14)).place(x=350,y=200)
    a=Entry(root,font=("Helvetica", 14)).place(x=550,y=200)
    back = Button(text="Back", command=back,font=("Helvetica", 14)).place(x=350,y=250)
    submit = Button(text="Submit", command=submit,font=("Helvetica", 14)).place(x=550,y=250)
    root.mainloop()