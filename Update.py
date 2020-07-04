from tkinter import *
root=Tk()
def Back():
    root.destroy()
    root.quit()
    import details
    next = details()
def ok():
    root.destroy()
    root.quit()
    import details
    next = details()
def Update():
    root.destroy()
    root.quit()
    r=Tk()
    l=Label(r,text="successfully edit").grid(row=1)
    b=Button(r,text='ok',command=ok).grid(row=2)
    r.mainloop()

class update():
    name = Label(root, text="Name:", bg='gray',width=10,padx=4).grid(row=0)
    name1 = Entry(root, text="Name:", bg='yellow').grid(row=0, column=1)
    Age = Label(root, text="Age:", bg='gray',width=10,padx=4).grid(row=1)
    Age1 = Entry(root, text="Age:", bg='yellow').grid(row=1, column=1)
    Sex = Label(root, text="Sex:", bg='gray',width=10,padx=4).grid(row=2)
    Sex1 = Entry(root, text="Sex", bg='yellow').grid(row=2, column=1)
    Blood_Group = Label(root, text="Blood_Group:", bg='gray',width=10,padx=4).grid(row=3)
    Blood_Group1 = Entry(root, text="Blood_Group:", bg='yellow').grid(row=3, column=1)
    Address = Label(root, text="Address:", bg='gray',width=10,padx=4).grid(row=4)
    Address1 = Entry(root, text="Name:", bg='yellow').grid(row=4, column=1)
    Phone_NO = Label(root, text="Phone_NO:", bg='gray',width=10,padx=4).grid(row=5)
    Phone_NO1 = Entry(root, text="Phone_NO:", bg='yellow').grid(row=5, column=1)
    Password = Label(root, text="Password:", bg='gray',width=10,padx=4).grid(row=6)
    Password1 = Entry(root, text="Password:", bg='yellow', show='*').grid(row=6, column=1)
    back = Button(root, text='Back', bg='green', command=Back).grid(row=7)
    back = Button(root, text='Update', bg='green', command=Update).grid(row=7, column=1)
    root.mainloop()