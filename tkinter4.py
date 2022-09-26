from tkinter import *
import os
from tkinter import messagebox


def register_user():
    db = open('usersInfo.txt', 'r')
    username_info = username.get()
    password_info = password.get()
    password2_info = password2.get()
    """print(username_info,password_info,password2_info)
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))"""
    if password_info!=password2_info:
        messagebox.showerror("Password not mach","restart")

    else:
        if len(password_info)<2:
            messagebox.showerror("password less than 6 char","Enter more than 6")
            register()
        elif username_info in db:
            messagebox.showerror("User exist")

    db = open('usersInfo.txt', 'a')
    db.write(username_info+","+password_info+"," +password2_info+ '\n')

    db.close()

def verify():
    db = open("usersInfo.txt", "r")
    username1=user_verify.get()
    password1=password_verify.get()
    os_list=os.listdir()
    if username1 in os_list:

        file.read("usersInfo.txt",'r')
        v=file.read().split()
        if password1 in v:
            messagebox.showinfo("success",'Login success')
        else:
            messagebox.showerror("Not foung","user password is wrong")
    else:
        messagebox.showinfo("No user please register your self")
        '''try:
            if data[username1]:
                try:
                    if password1==data[username1]:
                        print("Login Success")
                        print("Hi,welcome",username1)
                    else:
                        print("Password or Username Incorrect")
                except:
                    print("incorect password or username")
            else:
                print("User name doesn't exist")
        except:
            print("User name doesn't existr")
    else:
        messagebox.showerror("Please enter a value :")'''

def login():
    global screen2
    global user_verify
    global password_verify


    user_verify = StringVar()
    password_verify = StringVar()
    screen2 = Toplevel(screen)
    screen2.geometry('500x300')
    screen2.title("Login Screen")
    Label(text="Login").pack()
    usernalabel=Label(screen2,text="User name")
    usernalabel.place(x=50,y=50)

    user_entry=Entry(screen2,textvariable=user_verify)
    user_entry.place(x=150,y=50)

    passwordLabel=Label(screen2,text="password")
    passwordLabel.place(x=50,y=100)
    passwordEntry=Entry(screen2,textvariable=password_verify)
    passwordEntry.place(x=150,y=100)

    login_btn=Button(screen2,text="Login",height=2,width=15,command=verify)
    login_btn.place(x=150,y=200)


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry('350x250')
    global username
    global password
    global password2
    global username_entry
    global password_entry
    global password_entry2

    username = StringVar()
    password = StringVar()
    password2 = StringVar()

    userlab = Label(text="Username")
    userlab.place(x=50, y=50)
    username_entry = Entry(screen1, textvariable=username)
    username_entry.place(x=70, y=70)
    paswrdlab = Label(text="password")
    paswrdlab.place(x=50, y=80)
    password_entry = Entry(screen1, textvariable=password)
    password_entry.place(x=90, y=90)
    conflabel = Label(text="Confirm password")
    conflabel.place(x=50, y=110)
    password_entry2 = Entry(screen1, textvariable=password2)
    password_entry2.place(x=90, y=110)

    reg_userbtn = Button(screen1, text="register", height=3, width=15, command=register_user)
    reg_userbtn.place(x=100, y=130)


def main():
    global screen
    screen = Tk()
    Label(text="login Form").pack()
    screen.geometry('400x400')
    Button(text="Login", width=15, height=3, command=login).pack()
    Button(text="Register", width=15, height=3, command=register).pack()

    screen.mainloop()


main()
