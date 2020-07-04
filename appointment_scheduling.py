from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("1500x1000")
def submit():
    root.destroy()
    root.quit()
    from appointment_scheduling1 import appointment_scheduling1
def back():
    root.destroy()
    root.quit()
    from Doctorpage import Doctorpage
class appointment_scheduling():
    
    labelTop = Label(root,
                  text = "Patient Name:",font=("Helvetica", 14))
    labelTop.place(x=350,y=200)

    comboExample = ttk.Combobox(root, 
                            values=[
                                    "Deepak kumar", 
                                    "Santhosh",
                                    "Prabhu"],font=("Helvetica", 14))
    comboExample.place(x=500,y=200)
    comboExample.current(1)
    back = Button(text="Back", command=back,font=("Helvetica", 14)).place(x=350,y=250)
    submit = Button(text="Submit", command=submit,font=("Helvetica", 14)).place(x=500,y=250)
    root.mainloop()