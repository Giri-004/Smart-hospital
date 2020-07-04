import sqlite3

class admin():

    con = sqlite3.connect('database.db')
    #con.execute("create table admindatabase(username text,password text)")
    print("table created")
    con.execute("insert into admindatabase values('deepak','ji')")
    print('insert successfully')
    cursor = con.execute('select * from admindatabase')
    for row in cursor:
        print('name:', row[0])
        print('content:', row[1])


    print('select successfully')
    def check(self):
        print("check success")




