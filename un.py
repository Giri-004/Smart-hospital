import tkinter as tk
from tkinter import ttk
from sqlalchemy.sql.expression import column
from PIL import ImageTk,Image
import sys
import os
 
app = tk.Tk() 
app.geometry('200x100')
Canvas = tk.Canvas(app, width=1500, height=700)
Canvas.place(x=50, y=0)
im = Image.open('C:\\Users\\Deepak kumar M\\Desktop\\mini project\\health.jpg')
Canvas.image = ImageTk.PhotoImage(im)
Canvas.create_image(0, 0, image=Canvas.image)
import sys

labelTop = tk.Label(app,
                    text = "Select your Hospital")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "CMC", 
                                    "Apollo Hospital",
                                    "G.H coimbatore"])
comboExample.grid(column=0, row=1)
comboExample.current(1)
def hi():
    print(comboExample.current(), comboExample.get())
    app.destroy()
    import Home
b=tk.Button(app,text='submit',command=hi).grid(column=0, row=2)


app.mainloop()