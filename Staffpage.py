from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("1500x1000")
def pharmacy():
    root.destroy()
    root.quit()
    from pharmacy import pharmacy
    next=pharmacy()
def medical_stock():
    root.destroy()
    root.quit()
    import medical_stock
    next=medical_stock()
def nurse():
    root.destroy()
    root.quit()
    from nurse import nurse
    next=nurse()
def logout():
    root.destroy()
    root.quit()
class Staffpage():
    Canvas = Canvas(root, width=1500, height=700)
    Canvas.place(x=50, y=0)
    lable1 = Label(text='Welcome Staff!!!!!!!!!!',  height=1,font=("Helvetica", 24))
    lable1.place(x=560, y=50)
    pharmacy=Button(text="pharmacy",command=pharmacy, bg='pale green',font=("Helvetica", 14))
    pharmacy.place(x=160, y=100)
    medical_stock=Button(text="Medical stock", command=medical_stock, bg='pale green',font=("Helvetica", 14))
    medical_stock.place(x=160, y=200)
    nurse=Button(text="Nurse", command=nurse, bg='pale green',font=("Helvetica", 14))
    nurse.place(x=160, y=300)
    logout=Button(text="logout", command=logout, bg='pale green',font=("Helvetica", 14))
    logout.place(x=160, y=400)
    im = Image.open('33.jpg')
    Canvas.image = ImageTk.PhotoImage(im)
    Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
    root.mainloop()
