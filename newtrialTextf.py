from tkinter import messagebox

def  register():
    db = open("databasenew.txt", "r")

    username=input("enter name:")
    pas1=input("ener password:")
    pas2 = input("ener password2:")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))


    if pas1!=pas2:
        messagebox.showerror("Password not mach","restart")
        register()
    else:
        if len(pas1)<2:
            messagebox.showerror("password less than 6 char","Enter more than 6")
            register()
        elif username in d:
            messagebox.showerror("User exist")
            register()
        else:
            db=open("databasenew.txt","a")
            db.write(username+","+pas1+"\n")
            print("Success")

def acccess():
    db = open("databasenew.txt", "r")
    username = input("enter Username:")
    pas1 = input("enter your passsword password:")
    if not len(username or pas1)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[username]:
                try:
                    if pas1==data[username]:
                        print("Login Success")
                        print("Hi,welcome",username)
                    else:
                        print("Password or Username Incorrect")
                        home()
                except:
                    print("incorect password or username")
            else:
                print("User name doesn't exist")
                home()
        except:
            print("User name doesn't existr")
            home()
    else:
        messagebox.showerror("Please enter a value :")
        acccess()

def home(option=None):
    option=input("Login | Signup:")
    if option=="Login":
        acccess()
    elif option=="Signup":
        register()
    else:
        print("enter an option")
        home()
home()

