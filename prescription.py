from tkinter import *
root=Tk()
root.geometry("1500x1000")
def submit():
    root.destroy()
    root.quit()

def med():
    root.destroy()
    root.quit()
def back():
    root.destroy()
    root.quit()
    from Doctorpage import Doctorpage
    next = Doctorpage()
class prescription():
    a=Label(text="Enter how many Tablets and tonics",font=("Helvetica", 14)).grid(row=0,column=0)
    z= Entry(root)
    z.grid(row=0, column=1)
    b=z.get()

    for i in range(0,3):
        c=Label(root,text="Tablets",font=("Helvetica", 14)).grid(row=1+i,column=0)
        d=Entry(root).grid(row=1+i,column=1)
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        C1 = Checkbutton(text="Morning", variable=CheckVar1,font=("Helvetica", 14)).grid(row=1+i,column=2)
        C2 = Checkbutton(text="Afternoon", variable=CheckVar2,font=("Helvetica", 14)).grid(row=1+i, column=3)
        C3 = Checkbutton(text="Night", variable=CheckVar3,font=("Helvetica", 14)).grid(row=1+i, column=4)
    back = Button(text="Back", command=back,font=("Helvetica", 14)).grid(row=3+1, column=0)
    submit = Button(text="Submit", command=submit,font=("Helvetica", 14)).grid(row=3+1,column=1)
    root.mainloop()