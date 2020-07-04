from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("1500x1000")

def details():
    root.destroy()
    root.quit()
    import details
def Appointment():
    root.destroy()
    root.quit()
    from Appointment import page
def Operation():
    root.destroy()
    root.quit()
    import Operation
def Lab():
    root.destroy()
    root.quit()
    import Lab
def medicine():
    root.destroy()
    root.quit()
    from medicine import medicine
def feedback():
    root.destroy()
    root.quit()
    from feedback import feedback
def back():
    roo=Tk()
    roo.destroy()
    roo.quit()
    import details
def bill():
    root.destroy()
    root.quit()

    roo.geometry('200x200')
    Label(roo,text='Bill_amount').place(x=50, y=0)
    Label(roo, text='500').place(x=150, y=0)
    medicine2 = Button(roo, text="back", command=back, bg='light blue').place(x=100, y=50)
    roo.mainloop()
def Logout():
    root.destroy()
    root.quit()
    import UserLogin


class userpage():
    Canvas = Canvas(root, width=1500, height=700)
    Canvas.place(x=50, y=0)
    lable1 = Label(text='Welcome User!!!!!!!!!!',bg='light blue', height=1,font=("Helvetica", 24))
    lable1.place(x=450, y=50)
    details=Button(root,text="Get my Details",bg='light blue',command=details,font=("Helvetica", 14))
    details.place(x=450, y=100)
    appointment = Button(root, text="Appointment", command=Appointment,bg='light blue',font=("Helvetica", 14))
    appointment.place(x=450, y=150)
    lab = Button(root, text="Lab", command=Lab,bg='light blue',font=("Helvetica", 14))
    lab.place(x=450, y=200)
    medicine = Button(root, text="medicine", command=medicine,bg='light blue',font=("Helvetica", 14))
    medicine.place(x=450, y=250)
    medicine1 = Button(root, text="Any feedback", command=feedback,bg='light blue',font=("Helvetica", 14))
    medicine1.place(x=450, y=300)
    medicine2 = Button(root, text="bill", command=bill, bg='light blue',font=("Helvetica", 14))
    medicine2.place(x=450, y=350)
    medicine2 = Button(root, text="Logout", command=Logout,bg='light blue',font=("Helvetica", 14))
    medicine2.place(x=450, y=400)
    im = Image.open('patient.jpg')
    Canvas.image = ImageTk.PhotoImage(im)
    Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
    root.mainloop()

