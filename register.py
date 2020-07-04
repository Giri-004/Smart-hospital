from tkinter import *
import tkinter.messagebox
import sqlite3
con=sqlite3.connect('register.db')
root = Tk()
def Back():
    root.destroy()
    root.quit()
    from Home import Home
    next = Home()
name = Label(root, text="Name:", bg='gray').grid(row=0)
name1 = Entry(root, text="Name:", bg='yellow').grid(row=0, column=1)
Age = Label(root, text="Age:", bg='gray').grid(row=1)
Age1 = Entry(root, text="Age:", bg='yellow').grid(row=1, column=1)
Sex = Label(root, text="Sex:", bg='gray').grid(row=2)
Sex1 = Entry(root, text="Sex", bg='yellow').grid(row=2, column=1)
Blood_Group = Label(root, text="Blood_Group:", bg='gray').grid(row=3)
Blood_Group1 = Entry(root, text="Blood_Group:", bg='yellow').grid(row=3, column=1)
Address = Label(root, text="Address:", bg='gray').grid(row=4)
Address1 = Entry(root, text="Address", bg='yellow').grid(row=4, column=1)
Phone_NO = Label(root, text="Phone_NO:", bg='gray').grid(row=5)
Phone_NO1 = Entry(root, text="name:", bg='yellow').grid(row=5, column=1)
Password = Label(root, text="Password:", bg='gray').grid(row=6)
Password1 = Entry(root, text="Password:", bg='yellow', show='*').grid(row=6, column=1)
def submit():
    con.execute("insert into register values(1,'name1','Age1','Sex1','Blood_Group1','Address1','Phome_No1','Password1')")
    print('insert success')
submit=Button(root,text='Submit',bg='green',command=submit).grid(row=7,column=1)
back = Button(root, text='Back', bg='green', command=Back).grid(row=7)
root.mainloop()

