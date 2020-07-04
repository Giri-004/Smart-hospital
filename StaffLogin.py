import tkinter as tk
root=tk.Tk()
root.geometry("1500x1000")
passwords = [('Staff', 'lab')]
failure_max=3
def Back():
    root.destroy()
    root.quit()
    from Home import Home
    next = Home()
def submit(failures=[]):
    print(User_Name1.get(), Password1.get())
    if (User_Name1.get(), Password1.get()) in passwords:
        root.destroy()
        import Staffpage
        print('Logged in')
        return
    failures.append(1)
    if sum(failures) >= failure_max:
        root.destroy()
        import Home
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (sum(failures) + 1, failure_max))

User_Name =tk.Label(root, text="User_Name:",padx=4,font=("Helvetica", 14))
User_Name.place(x=450, y=50)
User_Name1 =tk.Entry(root, text="User_Name", bg='yellow',font=("Helvetica", 14))
User_Name1.place(x=570, y=50)
Password = tk.Label(root, text="Password :",padx=4,font=("Helvetica", 14))
Password.place(x=450, y=100)
Password1 = tk.Entry(root, text="Password :", bg='yellow', show='*',font=("Helvetica", 14))
Password1.place(x=570, y=100)
submit = tk.Button(root, text='Submit', bg='green', command = submit,border=0,font=("Helvetica", 14)).place(x=655, y=150)
back = tk.Button(root, text='Back', bg='green', command=Back,font=("Helvetica", 14)).place(x=510, y=150)
root.mainloop()