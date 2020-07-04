from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("1500x1000")
def appointment_scheduling():
    root.destroy()
    root.quit()
    from appointment_scheduling1 import appointment_scheduling1
def prescription():
    root.destroy()
    root.quit()
    from prescription import prescription
def operation_scheduling():
    root.destroy()
    root.quit()
    from operation_scheduling import operation_scheduling
def vaccine():
    root.destroy()
    root.quit()
    from vaccine import vaccine
def logout():
    root.destroy()
    root.quit()
    import Home
class Doctorpage():
    Canvas = Canvas(root, width=1500, height=700)
    Canvas.place(x=50, y=0)
    lable1 = Label(text='Welcome Doctor!!!!!!!!!!', height=1,font=("Helvetica", 24))
    lable1.place(x=550, y=50)
    a=Button(text="Schedule my Appointment",command=appointment_scheduling,font=("Helvetica", 14))
    a.place(x=50, y=100)
    prescription=Button(text="Prescription", command=prescription,font=("Helvetica", 14))
    prescription.place(x=50, y=200)
    os=Button(text="Schedule Operation", command=operation_scheduling,font=("Helvetica", 14))
    os.place(x=50, y=300)
    vaccine=Button(text="Vaccine", command=vaccine,font=("Helvetica", 14))
    vaccine.place(x=50, y=400)
    logout=Button(text="logout", command=logout,font=("Helvetica", 14))
    logout.place(x=50, y=500)
    im = Image.open('3.jpg')
    Canvas.image = ImageTk.PhotoImage(im)
    Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
    root.mainloop()
