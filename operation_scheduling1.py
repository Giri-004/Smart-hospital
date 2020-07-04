from tkinter import *
root=Tk()
def submit():
    root.destroy()
    root.quit()
    print('Date and Time scheduled Suceessfully')
def back():
    root.destroy()
    root.quit()
    from operation_scheduling import operation_scheduling
    next = operation_scheduling()
class operation_scheduling1():
    first=Label(root,text="Date").grid(row=0)
    a=Entry(root).grid(row=0,column=1)
    second=Label(text="Time").grid(row=1)
    b=Entry(root).grid(row=1,column=1)
    back=Button(text="Back",command=back).grid(row=2,column=0)
    submit = Button(text="Submit", command=submit).grid(row=2,column=1)
    root.mainloop()
