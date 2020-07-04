# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *
import sqlite3
class register():
    # opening the existing excel file
    con = sqlite3.connect('test.db')
    c = con.cursor()
    con.execute("CREATE TABLE giri (name TEXT PRIMARY KEY,content  TEXT,oldShape INT )")
    print('create successfully')
    con.execute("insert into giri values('giri','ji',8)")
    print('insert successfully')
    cursor = con.execute('select * from giri')
    for row in cursor:
        print('name:', row[0])
        print('content:', row[1])
        print('oldShape:', row[2])

    print('select successfully')


