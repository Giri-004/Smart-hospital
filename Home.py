from tkinter import *
from PIL import ImageTk,Image
import sys
import os
root = Tk()
root.geometry("1500x1000")
def UserLogin():
    try:
        root.destroy()
    except:
        pass
    root.quit()
    import UserLogin
def AdminLogin():
    root.destroy()
    root.quit()
    import AdminLogin

def DoctorLogin():
    root.destroy()
    root.quit()
    import DoctorLogin
def Quit():
    root.destroy()
    root.quit()
def StsffLogin():
    root.destroy()
    root.quit()
    import StaffLogin
def directions():
    root.destroy()
    root.quit()
    import direction

def speech():
    root.destroy()
    root.quit()
    os.system("python speech.py")
class Home():
    Canvas = Canvas(root, width=1500, height=700)
    Canvas.place(x=50, y=0)
    lable1 = Label(text='Welcome!!!!!!!!!!',height=1,font=("Helvetica", 24),bg='sky blue')
    lable1.place(x=555, y=50)
    button1 = Button(text='Admin', command=AdminLogin,bg='pale green',width=9,height=1,font=("Helvetica", 14))
    button1.place(x=435,y=100)
    button2 = Button(text='Doctor', command=DoctorLogin,bg='pale green',width=10,height=1,font=("Helvetica", 14))
    button2.place(x=555, y=100)
    button3 = Button(text='User', command=UserLogin,bg='pale green',width=10,height=1,font=("Helvetica", 14))
    button3.place(x=685, y=100)
    button4 = Button(text='Staffs', command=StsffLogin,bg='pale green',width=10,height=1,font=("Helvetica", 14))
    button4.place(x=815, y=100)
    button5 = Button(text='Get Directions', command=directions,bg='pale green',width=12,height=1,font=("Helvetica", 14))
    button5.place(x=510, y=150)
    button6 = Button(text="I'm your Friend here!!!!!!!", command=speech,bg='pale green',width=20,height=1,font=("Helvetica", 14))
    button6.place(x=660, y=150)
    Canvas.pack()
    im = Image.open('90.jpg')
    Canvas.image = ImageTk.PhotoImage(im)
    Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)

    root.mainloop()
