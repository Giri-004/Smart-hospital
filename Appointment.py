from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("1500x1000")
def ok():
    root.destroy()
    root.quit()
    import Userpage
def submit():
    root.destroy()
    root.quit()
    roo=Tk()
    ro = Label(roo, text="appointment request send").grid(row=0)
    submit = Button(roo, text='ok', command=ok).grid(row=1, column=0)
    roo.mainloop()
def Back():
    root.destroy()
    root.quit()
    from Userpage import userpage
class page():
    
    labelTop = Label(root,text = "Doctor's name",font=("Helvetica", 16))
    labelTop.grid(column=0, row=5)

    comboExample = ttk.Combobox(root, 
                            values=[
                                    "Dr.kesavan(genaral)", 
                                    "Dr.Anusha(artho)",
                                    "Dr.Mythily(surgery)"],font=("Helvetica", 16))
    comboExample.grid(column=1, row=5)
    comboExample.current(1)
    def oh():
        ro = Label(root, text="Name:",font=("Helvetica", 16)).grid(row=4,column=5)
        ro = Label(root, text="Dr.Mythily",font=("Helvetica", 16)).grid(row=4,column=6)
        ro = Label(root, text="I'D:",font=("Helvetica", 16)).grid(row=5,column=5)
        ro = Label(root, text="23",font=("Helvetica", 16)).grid(row=5,column=6)
        ro = Label(root, text="DOB:",font=("Helvetica", 16)).grid(row=6,column=5)
        ro = Label(root, text="04.11.1999",font=("Helvetica", 16)).grid(row=6,column=6)
        ro = Label(root, text="Speclist",font=("Helvetica", 16)).grid(row=7,column=5)
        ro = Label(root, text="surgery",font=("Helvetica", 16)).grid(row=7,column=6)
        ro = Label(root, text="Phone no",font=("Helvetica", 16)).grid(row=8,column=5)
        ro = Label(root, text="8321498563",font=("Helvetica", 16)).grid(row=8,column=6)
        ro = Label(root, text="Date:",font=("Helvetica", 16)).grid(row=10,column=5)
        d=Entry(font=("Helvetica", 16)).grid(row=10,column=6)
        ro = Label(root, text="Time",font=("Helvetica", 16)).grid(row=11,column=5)
        d=Entry(font=("Helvetica", 16)).grid(row=11,column=6)
        ro = Label(root, text="Reason",font=("Helvetica", 16)).grid(row=12,column=5)
        d=Entry(font=("Helvetica", 16)).grid(row=12,column=6)
        sub=Button(root,text="submit",command=submit,font=("Helvetica", 16)).grid(row=13,column=6)
        subt = Button(root, text="back", command=Back,font=("Helvetica", 16)).grid(row=13, column=5)
    
    submit=Button(root,text='ok',command=oh,font=("Helvetica", 16)).grid(row=7,column=1)
    root.mainloop()