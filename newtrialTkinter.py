from tkinter import *
from tkinter import messagebox

global root
import os


global root
root=Tk()

def registernow():
    userInfo=useremail.get()
    password=password1.get()
    passwords=password2.get()
    print(userInfo)

    db = open("trial2.txt", 'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append()
        f.append()
    data = dict(zip(d, f))
    print(data)
    if str(password) != passwords:
        messagebox.showerror("Password not mach", "restart")

    else:
        if len(password) < 6:
            print("not inserted")

        elif userInfo in d:
            messagebox.showerror("User exist")

        else:
            db = open("trial2.txt", "a")
            db.write(userInfo + "," + passwords + "\n")
            print("Success")

def register():
    global  window
    global useremail
    global password1
    global password2
    global usernameEntry
    global password1Entr
    global password2Entry
    useremail = StringVar()
    password1 = StringVar()
    password2 = StringVar()

    window =Tk()
    window.geometry('600x300')
    window.configure(background="green")

    userlabel =Label(window, text="user name:")
    passwordlabe1 =Label(window, text="Password:")
    passwordlabe2 =Label(window, text="Conform password:")

    userlabel.place(x=100, y=100)
    passwordlabe1.place(x=100, y=150)
    passwordlabe2.place(x=100, y=200)
    usernameEntry =Entry(window, width=40,textvariable=useremail)
    password1Entry =Entry(window, width=40,textvariable=password1)
    password2Entry =Entry(window, width=40,textvariable=password2)

    usernameEntry.place(x=300, y=100, height=23 )
    password1Entry.place(x=300, y=150, height=23 )
    password2Entry.place(x=300, y=200, height=23 )
    sub_btn=Button(window,text="registenow",command=registernow)
    sub_btn.place(x=350,y=250)




'''def access(useremail, password1, password2):
    win2 = Tk()
    userlabel =Label(win2, text="user name:")
    passwordlabe1 = Label(win2, text="Password:")
    userlabel.place(x=100, y=100)
    passwordlabe1.place(x=100, y=150)
    usernameEntry = Entry(win2, width=40)
    password1Entry = Entry(win2, width=40)
    usernameEntry.place(x=300, y=100, height=23, textvariable=useremail)
    password1Entry.place(x=300, y=150, height=23, textvariable=password1)

    db = open("trial2.txt", "r")
    useremail = input("enter Username:")
    pas1 = input("enter your passsword password:")
    if not len(useremail or pas1) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[useremail]:
                try:
                    if pas1 == data[useremail]:
                        print("Login Success")
                        print("Hi,welcome", useremail)
                    else:
                        print("Password or Username Incorrect")

                except:
                    print("incorect password or username")
            else:
                print("User name doesn't exist")

        except:
            print("User name doesn't existr")
    else:
        messagebox.showerror("Please enter a value :")
        win2.mainloop()
login=Button(root,text="Login",command= access)
login.place(x=200,y=100)
'''
register=Button(root,text="register",command=register)
register.place(x=200,y=200)

root.mainloop()





