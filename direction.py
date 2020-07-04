from tkinter import *
import sqlite3
import speech_recognition
from PIL import ImageTk,Image
root=Tk()
root.geometry('600x200')
import sys
def Back():
    root.destroy()
    root.quit()
    from Home import Home
    next = Home()
def voi():
    import speech_recognition as s_r
    import pyttsx3
    import os

    Speech1 = s_r.Recognizer()

    try:
        engine=pyttsx3.init()
    except ImportError:
        print("Requested driver is not found")
    except RuntimeError:
        print("Driver fails to initialise")

    voices = engine.getProperty("voices")

# for voice in voices:
# print(voice.id)

    engine.setProperty("voices", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0")
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 50)

    engine.setProperty('voice', voices[0].id)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 5.0)
    def speak_text_cmd(cmd):
        engine.say(cmd)
        engine.runAndWait();
    speak_text_cmd("Hello Sir,I'M your Assistant")
    speak_text_cmd("This is the direction for go to emergency ward")
    speak_text_cmd("Go straight and turn right, go straight turn left there is emergency ward ")

def image():
    a = start.get()
    b=end.get()
    root.destroy()
    root.quit()
    if(a=='reception' and b=='emergency'):
        id=1
    else:
        id=2
    if(id==1):
        import tkinter
        from tkinter import Canvas
        from PIL import ImageTk,Image
        import sys
        import os
        roo = Tk()
        roo.geometry("1500x500")
        Canvas = Canvas(roo, width=500, height=500)
        Canvas.place(x=300, y=100)
        g=Button(roo,text="Get voice",command=voi).place(x=600, y=390)
        g=Button(roo,text="Back",command=Back).place(x=500, y=390)
        Canvas.pack()
        im = Image.open('2.jpg')
        Canvas.image = ImageTk.PhotoImage(im)
        Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
        roo.mainloop()
    else:
        import tkinter
        from tkinter import Canvas
        from PIL import ImageTk,Image
        import sys
        import os
        roo = Tk()
        roo.geometry("1500x500")
        Canvas = Canvas(roo, width=500, height=500)
        Canvas.place(x=300, y=100)
        g=Button(roo,text="Get voice",command=voi).place(x=600, y=190)
        g=Button(roo,text="Back",command=Back).place(x=500, y=190)
        Canvas.pack()
        im = Image.open('1.jpg')
        Canvas.image = ImageTk.PhotoImage(im)
        Canvas.create_image(0, 0, anchor=NW, image=Canvas.image)
        roo.mainloop()


lable1=Label(text='Starting Point',bg='green',width=12,padx=10)
start=Entry(root,bg='yellow')
start.place(x=250, y=50)
lable1.place(x=100, y=50)
lable2 = Label(text='end Point', bg='green',width=12,padx=10)
end=Entry(root,bg='yellow')
end.place(x=250, y=100)
lable2.place(x=100, y=100)
a=start.get()
b=end.get()
submit=Button(text='submit',bg='red',command=image,width=12)
back = Button(text='Back', bg='red', command=Back,width=12)
submit.place(x=250, y=150)
back.place(x=100, y=150)
root.mainloop()
