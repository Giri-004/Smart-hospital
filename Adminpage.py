from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("1500x1000")
def userdetails():
    root.destroy()
    root.quit()
    from manage_user_details import details
    next=details()
def doctordetails():
    root.destroy()
    root.quit()
    import manage_doctor_details
def staffdetails():
    root.destroy()
    root.quit()
    import  manage_staff_details
def feedback():
    root.destroy()
    root.quit()
    import viewfeed

def Logout():
    root.destroy()
    root.quit()
    import Home
class page():
      Canvas = Canvas(root, width=1500, height=700)
      Canvas.place(x=50, y=0)
      lable1 = Label(text='Welcome Admin!!!!!!!!!!', bg='light blue', height=1,font=("Helvetica", 24))
      lable1.place(x=570, y=50)
      a=Button(text="user details",command=userdetails, bg='pale green',width=12,padx=10,font=("Helvetica", 14))
      a.place(x=1090, y=100)
      b = Button(text="Doctor details", command=doctordetails, bg='pale green',width=12,padx=10,font=("Helvetica", 14))
      b.place(x=1090, y=180)
      c = Button(text="staff details", command=staffdetails, bg='pale green',width=12,padx=10,font=("Helvetica", 14))
      c.place(x=1090, y=260)
      d = Button(text="feedbacks", command=feedback, bg='pale green',width=12,padx=10,font=("Helvetica", 14))
      d.place(x=1090, y=340)
      d = Button(text="Logout", command=Logout, bg='pale green',width=12,padx=10,font=("Helvetica", 14))
      d.place(x=1090, y=420)
      im = Image.open('45.jpg')
      Canvas.image = ImageTk.PhotoImage(im)
      Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
      root.mainloop()