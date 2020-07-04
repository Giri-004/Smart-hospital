from tkinter import *
root=Tk()
root.geometry("1500x1000")
roo=Tk()
def submit():
    root.destroy()
    root.quit()
    Label(roo, text='your feedback send successfully',font=("Helvetica", 14)).place(x=50, y=0)
    medicine2 = Button(roo, text="ok", command=Back, bg='light blue',font=("Helvetica", 14)).place(x=100, y=50)
    roo.mainloop()
def Back():
    root.destroy()
    root.quit()
    from Userpage import userpage
    next=userpage()
class feedback():
    l=Label(text='Enter your feedback:',font=("Helvetica", 14)).grid(row=0,column=0)
    t = Entry(root,font=("Helvetica", 14)).grid(row=0,column=1)
    b=Button(text='Send',command=submit,font=("Helvetica", 14)).grid(row=1,column=1)
    b = Button(text='Back', command=Back,font=("Helvetica", 14)).grid(row=1,column=0)
    root.mainloop()