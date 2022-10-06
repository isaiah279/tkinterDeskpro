from tkinter import ttk, colorchooser
import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import os
import webbrowser
import shutil
import phonenumbers
from phonenumbers import geocoder
from selenium import webdriver  # automation proceess library
from time import sleep
import folium
import phonenumbers
from phonenumbers import geocoder
import folium
from tkinter import messagebox
from PIL import Image, ImageTk
# mysql connections
import mysql.connector
from mysql.connector import Error
from tkinter import *

try:
    from PIL import Image
except ImportError:
    import Image
import os
import math
import random
import smtplib

global locatingV
global namet1
global emailt2
global issuet5
global phonet3
global locationt4
global name
global confirmPassword
global issue
global phone
global location

global ename
global eemail
global eissue
global ephone
global elocation

mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="basecare_db")
mycursor = mysqldb.cursor()


class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def submit(self):
            pass

        bordering = tk.LabelFrame(self, text="", font=("Arial Bold", 20), bd=1, fg="Lightgreen")
        bordering.pack(fill="both", expand='yes')
        bg = ImageTk.PhotoImage(
            file='C:\\Users\\User\\Downloads\\depositphotos_24645511-stock-photo-nurse-making-notes-during-home.jpg')
        # Create a Canvas
        canvas = Canvas(width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        # Add Image inside the Canvas
        canvas.create_image(0, 0, image=bg, anchor='nw')

        def clearlog():
            useremail_entry.delete(0, END)
            passwordEntry.delete(0, END)
        def verify_login():
            # file = open("usersInfo.txt", "r")
            useremail_infoLogin = useremail_entry.get()
            password_infoLogin = passwordEntry.get()
            if useremail_infoLogin == '' or password_infoLogin == '':
                messagebox.showerror('Error', 'All Fields Are Required')
            else:
                con = mysql.connector.connect(host='localhost', user='root', password='', database='basecare_db')
                cur = con.cursor()
                cur.execute('select * from register where email=%s and passwords=%s',
                            (useremail_infoLogin, password_infoLogin))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('error', 'Invalid Email or Password')
                    screen1.destroy()
                    login()
                    clearlog()
                else:
                    messagebox.showinfo('Success', 'Welcome')
                    messagebox.showinfo(" success ", f"You Logged in with {useremail_infoLogin}")
                    Next = Button(bordering, text="Press Next to continue", bg='orange', cursor='hand2', borderwidth=0,
                                  width=20, height=2,
                                  command=lambda: controller.show_frame(FouthPage))
                    Next.place(x=500, y=300)
                    clearlog()

                con.close()

            '''if username_infoLogin == "" and password_infoLogin == "":
                messagebox.showerror("enter data", "can't be empty")
                login()
            elif username_infoLogin and password_infoLogin in open("newfile.txt").read():
                messagebox.showinfo("sucess", f"You Logged in as {username_infoLogin}")
                Next = Button(bordering, text="press Next", command=lambda: controller.show_frame(FouthPage))
                Next.place(x=500, y=200)
            else:
                messagebox.showwarning("user doesn't exit ", "sign up to proceed")
                login()'''

        def login():
            global screen2
            screen2 = Tk()
            screen2.geometry('500x200+400+150')
            label = Label(screen2, text="Login Page", bg="skyblue", fg="black", padx=5, pady=5,
                          font=("Algerian", 18))
            label.place(x=220, y=2)
            global user_verify
            global password_verify
            global useremail_entry
            global passwordEntry
            useremail_verify = StringVar()
            password_verify = StringVar()
            screen2.resizable(False, False)
            screen2.geometry('550x350')
            screen2.config(bg='skyblue')
            screen2.title("Login Screen")
            Label(text="Login").pack()
            usernalabel = Label(screen2, text="User Email:", bg='SkyBlue', font=12)
            usernalabel.place(x=50, y=80)
            useremail_entry = Entry(screen2, textvariable=useremail_verify, width=30, font=12)
            useremail_entry.place(x=150, y=80, height=25)
            passwordLabel = Label(screen2, text="password:", font=12, bg='SkyBlue')
            passwordLabel.place(x=50, y=130)
            passwordEntry = Entry(screen2, textvariable=password_verify, width=30, font=12, show="*")
            passwordEntry.place(x=150, y=130)
            login_btn = Button(screen2, text="Login", command=verify_login, height=1, width=15)
            login_btn.place(x=150, y=180)

        def clearReg():
            username_entry.delete(0, END)
            useremail_entry.delete(0, END)
            password_entry.delete(0, END)
            password_entry2.delete(0, END)

        def register_user():
            # db = open('usersInfo.txt', 'r')
            username_info = username_entry.get()
            userEmail_info = useremail_entry.get()
            password_info = password_entry.get()
            password2_info = password_entry2.get()
            data = (userEmail_info, username_info, password_info)
            tokensql = 'insert into register (email,username,passwords)values(%s,%s,%s)'
            con = mysql.connector.connect(host='localhost', user='root', password='', database='basecare_db')
            cur = con.cursor()
            try:
                if username_info != '' or password_info != '' or password2_info != '' or useremail_entry != "":
                    if '@' in userEmail_info and '.com' in userEmail_info:
                        messagebox.showinfo(" Proceed  ", f"Are you sure you want to proceed with{userEmail_info}")
                        if password_info != password2_info:
                            messagebox.showerror("hey", "check your password not matching")
                            clearReg()

                            register()
                        else:
                            # try:
                            cur.execute(tokensql, data)
                            con.commit()
                            con.close()
                            messagebox.showinfo('Success', "Registration Successful")
                            clearReg()

                            login()
                    else:
                        messagebox.showerror("Hey check", "you entered invalid email")
                        clearlog()

                        register()
                else:
                    messagebox.showerror("Hey check", "you can't submit invalid entries")

                    register()
            except:
                messagebox.showerror("Contact administrator", "Either you have registered \n"
                                                              "or You have entered incorrect details")
                # Exception as e
                '''except :
                    messagebox.showerror("not sent")'''
            '''if username_info == '' or password_info == '' or password2_info == '':
                messagebox.showwarning("fill the empty field!!!","hey you can't send empty field")
                register()
            elif username_info in open("newfile.txt").read():
                messagebox.showerror("data exits in the file")
                register()
            elif password_info != password2_info:
                messagebox.showwarning("Passwprd not mach")
                register()
            else:
                # opening of file to store data
                db = open("newfile.txt", "a")  # here a means append
                username_info = username_entry.get()
                password_info = password_entry.get()
                password2_info = password_entry2.get()
                db = open("newfile.txt", "a")
                db.write(username_info + "," + password_info + "," + password2_info + "\n")
                messagebox.showinfo("Logged in as",f"Name:{username_info}\n password:{password_info}")'''
            login()
            '''file=open('usersInfo.txt', 'a')
            file.write(username_info+"\n")
            file.write(password_info+"\n")
            file.write(password2_info+"\n")'''

        def register():

            global screen1
            screen1 = Tk()
            screen1.config(bg='SkyBlue')
            screen1.geometry('500x200+400+150')
            screen1.geometry('550x350')
            screen1.resizable(False, False)
            global username
            global password
            global password2
            global username_entry
            global password_entry
            global password_entry2
            global useremail_entry
            global emailing

            username = StringVar()
            password = StringVar()
            password2 = StringVar()
            emailing = StringVar()

            label = Label(screen1, text="Registration Page", bg="skyblue", fg="black", padx=5, pady=5,
                          font=("Algerian", 18))
            label.place(x=220, y=2)

            userlab = Label(screen1, text="Username", bg='SkyBlue', font=12)
            userlab.place(x=50, y=20 + 30)
            username_entry = Entry(screen1, textvariable=username, width=30, font=12)
            username_entry.place(x=200, y=20 + 30)

            userlabemail = Label(screen1, text="Email", bg='SkyBlue', font=12)
            userlabemail.place(x=50, y=50 + 30)
            useremail_entry = Entry(screen1, textvariable=emailing, width=30, font=12)
            useremail_entry.place(x=200, y=50 + 30)

            paswrdlab = Label(screen1, text="password", bg='SkyBlue', font=12)
            paswrdlab.place(x=50, y=80 + 30)
            password_entry = Entry(screen1, textvariable=password, width=30, font=12, show="*")
            password_entry.place(x=200, y=80 + 30)
            conflabel = Label(screen1, text="Confirm password", bg='SkyBlue', font=12)
            conflabel.place(x=50, y=110 + 30)
            password_entry2 = Entry(screen1, textvariable=password2, width=30, font=12, show="*")
            password_entry2.place(x=200, y=110 + 30)
            reg_userbtn = Button(screen1, text="register", height=1, width=15, command=register_user)
            reg_userbtn.place(x=200, y=170 + 30)

        # IMAGE INSERTED HERE
        # Open the Image File
        bg = ImageTk.PhotoImage(
            file='C:\\Users\\User\\Downloads\\depositphotos_24645511-stock-photo-nurse-making-notes-during-home.jpg')
        # Create a Canvas
        canvas = Canvas(bordering, width=700, height=500)
        canvas.pack(fill=BOTH, expand=True)
        # Add Image inside the Canvas
        canvas.create_image(0, 0, image=bg, anchor='nw')

        # Function to resize the window
        def resize_image(e):
            global image, resized, image2
            # open image to resize it
            image = Image.open(
                'C:\\Users\\User\\Downloads\\depositphotos_24645511-stock-photo-nurse-making-notes-during-home.jpg')
            # resize the image with width and height of root
            resized = image.resize((e.width, e.height), Image.Resampling.LANCZOS)

            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')

        # Bind the function to configure the parent window
        bordering.bind("<Configure>", resize_image)
        # TITLE
        headinhLabel = Label(bordering,
                             text="Welcome to the Home Based Care Assiatance App \n Log in Or Signup For more Information",
                             font=('Algerian', 20), fg='Orange')
        headinhLabel.place(x=300, y=0)

        login_btn = tk.Button(bordering, text="Login", command=login, font=('Algerian', 16))
        login_btn.place(x=500, y=500, width=170, height=30)

        register_btn = tk.Button(bordering, text="Register", bg="orange", command=register, font=('Algerian', 16))
        register_btn.place(x=700, y=500, width=170, height=30)
        # register button


# self.after(5000,FouthPage)
# SecondPage.destroy()
class ThirdPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #####proceedig to admin##############
        def verifying_admin():

            admin_name = adminlogin_entry.get()
            admin_password = adminlogin_entrypasswordEntry.get()
            password_adminn = password_admin.get()

            if admin_name == "" and admin_password == "":
                messagebox.showerror("Enty Entries", "Provide your Details")
            elif admin_name == 'Admin' and admin_password == "123":
                btn = tk.Button(self, text="Proceed to Admin", font=("Arial", 15), bg="yellow",
                                command=lambda: controller.show_frame(AdminPage))
                btn.place(x=1100, y=10, width=250, height=50)
                window1.destroy()
            else:
                messagebox.showerror("Error", "Contact Developer")
                loginAdmin()

        def loginAdmin():
            global T1, T2
            global window1
            global admin_verifier
            global adminlogin_entry
            global adminlogin_entrypasswordEntry
            global password_admin
            password_admin = StringVar()
            admin_verifier = StringVar()

            window1 = tk.Tk()
            window1.geometry('500x300+400+250')
            window1.config(bg='skyblue')
            label = Label(window1, text="Admin Login", bg="skyblue", fg="black", padx=5, pady=5,
                          font=("Algerian", 18))
            label.place(x=220, y=2)
            Label(text="Login").pack()
            adminloginlabel = Label(window1, text="User name", bg='SkyBlue', font=12)
            adminloginlabel.place(x=50, y=80)

            adminlogin_entry = Entry(window1, textvariable=admin_verifier, width=30, font=12)
            adminlogin_entry.place(x=150, y=80, height=25)

            adminlogin_entrypasswordLabel = Label(window1, text="password", font=12, bg='SkyBlue')
            adminlogin_entrypasswordLabel.place(x=50, y=130)
            adminlogin_entrypasswordEntry = Entry(window1, textvariable=password_admin, width=30, font=12, show="*")
            adminlogin_entrypasswordEntry.place(x=150, y=130)

            login_btn = tk.Button(window1, text="Login here", command=verifying_admin, height=1, width=20)
            login_btn.place(x=150, y=180)

        # def comments():
        self.config(bg='indigo')
        self.texting = tk.StringVar()
        self.email = tk.StringVar()

        self.na = tk.Label(self, text="Leave A Message", bg='#39789c', font=('Algerian', 26, 'bold'))
        self.na.pack(pady=20)
        self.wrapper1 = tk.LabelFrame(self, text="Write Comment", fg="White", bg='#1a2c3d', font=('Arial', 14),
                                      border=1)

        self.wrapper1.pack(fill="both", expand="true", padx=0, pady=80, ipady=2)
        textarea = tk.Text(self.wrapper1, width=25, height=10, font=20, fg="green")
        textarea.pack(ipady=50, ipadx=200, anchor='center', pady=20)
        self.lemail = tk.Label(self.wrapper1, text="Enter Your Email", font=10, bg='#1a2c3d')
        self.lemail.place(x=360, y=330)
        email = tk.Entry(self.wrapper1, textvariable=self.email, width=20)
        email.pack(ipadx=50, ipady=10, anchor='center')
        # IMAGE INSERTED HERE
        # Open the Image File
        bg = ImageTk.PhotoImage(
            file='C:\\Users\\User\\Downloads\\depositphotos_24645511-stock-photo-nurse-making-notes-during-home.jpg')
        # Create a Canvas
        canvas = Canvas(width=700, height=500)
        canvas.pack(fill=BOTH, expand=True)
        # Add Image inside the Canvas
        canvas.create_image(0, 0, image=bg, anchor='nw')

        # Function to resize the window
        def resize_image(e):
            global image, resized, image2
            # open image to resize it
            image = Image.open(
                'C:\\Users\\User\\Downloads\\depositphotos_24645511-stock-photo-nurse-making-notes-during-home.jpg')
            # resize the image with width and height of root
            resized = image.resize((e.width, e.height), Image.Resampling.LANCZOS)

            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')

        # image bachground

        #################
        def clear():
            textarea.delete(1.0, END)
            email.delete(0, END)

        def send_comment():
            mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
            mycursor = mysqldb.cursor()
            comment = textarea.get(1.0, 'end')
            send_Email = self.email.get()
            try:
                if send_Email != "" and comment != "":
                    sql = "INSERT INTO  comments (email,comment) values (%s,%s)"
                    val = (send_Email, comment)
                    if '@' not in send_Email and '.com' not in send_Email:
                        messagebox.showwarning("warning ", "enter valid Email  address")
                    else:
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        clear()
                        messagebox.showinfo("success Message", "Comment Sent  successfully...")
                        mysqldb.close()
                        clear()
                else:
                    messagebox.showwarning("Error Warning", "Fill in the blank entries")
            except:
                messagebox.showerror("Hey Look !!", "Your data are not in Harmony with database")

        def clear_btn():
            clear()

        def exit_btn():
            self.destroy()

        def showgialogs():
            self.colorchooser.askcolor()
            Button(self, text="Color Pick Dialog", padx=10, pady=10, bg="#C0392B", fg="white",
                   command=showgialogs)

        # action buttons
        send_btn = tk.Button(self.wrapper1, text="send Comment", command=send_comment, width=15, bg='green',
                             relief='flat')
        send_btn.place(x=350 + 15, y=400, height=20 + 20)
        clear_btn = tk.Button(self.wrapper1, text="Clear Comment", command=clear_btn, width=15, bg='orange',
                              relief='sunken')
        clear_btn.place(x=500 + 15, y=400, height=20 + 20)
        exit_btn = tk.Button(self.wrapper1, text="Exit page", command=exit_btn, width=15, bg='red', relief='flat',
                             cursor='cross')
        exit_btn.place(x=650 + 15, y=400, height=20 + 20)

        Button = tk.Button(self, text="Home", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=1, y=0, width=100, height=60)
        Button = tk.Button(self, text="For Services", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FouthPage))
        Button.place(x=100, y=0, width=150, height=60)
        Button = tk.Button(self, text="Admin", font=("Arial", 15), bg='blue',
                           command=loginAdmin)
        Button.place(x=230, y=0, width=150, height=60)  # x=100, y=450
        # x=100, y=450


class FouthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #####Admin login
        def clearLogindetails():

            adminlogin_entry.delete(0, END)
            adminlogin_entrypasswordEntry.delete(0, END)

        def verifying_admin():

            admin_name = adminlogin_entry.get()
            admin_password = adminlogin_entrypasswordEntry.get()
            password_adminn = password_admin.get()

            if admin_name == "" and admin_password == "":
                messagebox.showerror("Enty Entries", "Provide your Details")
            elif admin_name == 'Admin' and admin_password == "123":
                btn = tk.Button(self, text="Proceed to Admin", font=("Arial", 15), bg="yellow",
                                command=lambda: controller.show_frame(AdminPage))
                btn.place(x=1100, y=10, width=250, height=50)
                window1.destroy()
            else:
                messagebox.showerror("Error", "Contact Developer")
                loginAdmin()

        def loginAdmin():
            global T1, T2
            global window1
            global admin_verifier
            global adminlogin_entry
            global adminlogin_entrypasswordEntry
            global password_admin
            password_admin = StringVar()
            admin_verifier = StringVar()

            window1 = tk.Tk()
            window1.geometry('500x300+400+250')
            window1.config(bg='skyblue')
            label = Label(window1, text="Admin Login", bg="skyblue", fg="black", padx=5, pady=5,
                          font=("Algerian", 18))
            label.place(x=220, y=2)
            Label(text="Login").pack()
            adminloginlabel = Label(window1, text="User name", bg='SkyBlue', font=12)
            adminloginlabel.place(x=50, y=80)

            adminlogin_entry = Entry(window1, textvariable=admin_verifier, width=30, font=12)
            adminlogin_entry.place(x=150, y=80, height=25)

            adminlogin_entrypasswordLabel = Label(window1, text="password", font=12, bg='SkyBlue')
            adminlogin_entrypasswordLabel.place(x=50, y=130)
            adminlogin_entrypasswordEntry = Entry(window1, textvariable=password_admin, width=30, font=12, show="*")
            adminlogin_entrypasswordEntry.place(x=150, y=130)

            login_btn = tk.Button(window1, text="Login here", command=verifying_admin, height=1, width=20)
            login_btn.place(x=150, y=180)

        # def comments():
        # varaible declaration
        self.configure(bg="purple")

        # self.spamVar = tk.StringVar()

        namet1 = tk.StringVar()
        emailt2 = tk.StringVar()
        phonet3 = tk.IntVar()
        locationt4 = tk.StringVar()
        issuet5 = tk.StringVar()

        def clear():
            ename.delete(0, END)
            eemail.delete(0, END)
            eissue.delete(0, END)
            ephone.delete(0, END)
            elocation.delete(0, END)

        def add_information():
            # getting inputs from the entry points

            name = namet1.get()
            email = emailt2.get()
            phone = phonet3.get()
            location = locationt4.get()
            issue = issuet5.get()
            global mysqldb
            global mycursor
            self.val = (name, email, phone, location, issue, name,)
            mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
            mycursor = mysqldb.cursor()

            # Empty Validation
            try:
                if name != "" and email != "" and issue != "" and phone != "" and location != "":
                    sql = "INSERT INTO  details_table (name,email,issue,phonenumber,location) values (%s, %s, %s, %s,%s)"
                    val = (name, email, issue, phone, location)
                    if '@' not in email and '.com' not in email:
                        messagebox.showwarning("warning ", "enter valid Email  address")
                    else:
                        mycursor.execute(sql, val)
                        mysqldb.commit()
                        clear()
                        clear()
                        messagebox.showinfo("information", "Employee inserted successfully...")
                        # mysqldb.rollback()
                        mysqldb.close()
                else:
                    messagebox.showwarning("Error Warning", "Fill in the blank entries")
            except:
                messagebox.showerror("Hey check !", "your data is not in the harmony with database")

            # data issertion goes here

        def clear_information():
            clear()

        def cancel_information():
            clear()

        # phone, email, name, location, issue
        wrapper1 = tk.LabelFrame(self, text="Enter Details", bg="#E86850")
        wrapper2 = tk.LabelFrame(self, text="Actions Required")

        wrapper2.config(bg="green")
        wrapper1.pack(fill="both", expand='yes', pady=50)

        # actions
        add_btn = tk.Button(wrapper1, text="Submit Request", command=add_information, bg="#E86850", width=15,font=12)
        delete_btn = tk.Button(wrapper1, text="Clear", command=clear_information, bg="#E86850", width=15,font=12)
        cancel_btn = tk.Button(wrapper1, text="Cancel", command=cancel_information, bg="#E86850", width=15,font=12)

        # labels
        lname = tk.Label(wrapper1, text="Name:", bg='#E86850',font=11)
        lemail = tk.Label(wrapper1, text="Email:", bg='#E86850',font=11)
        lphone = tk.Label(wrapper1, text="Phone:", bg='#E86850',font=11)
        lissue = tk.Label(wrapper1, text="Issue:", bg='#E86850',font=11)
        llocation = tk.Label(wrapper1, text="Location", bg='#E86850',font=11)
        id_number = tk.Label(wrapper1, text="Location", bg='#E86850',font=11)

        # grids

        lname.grid(row=1, column=0, padx=20, pady=60)
        lemail.grid(row=2, column=0, padx=20)
        lphone.grid(row=1, column=3, padx=20, pady=20)
        llocation.grid(row=2, column=3, padx=20, pady=20)
        lissue.grid(row=3, column=0, padx=20, pady=40)

        # Setting variable into the entry points
        ename = tk.Entry(wrapper1, textvariable=namet1,font=11)
        eemail = tk.Entry(wrapper1, textvariable=emailt2,font=11)
        ephone = tk.Entry(wrapper1, textvariable=phonet3,font=11)
        elocation = tk.Entry(wrapper1, textvariable=locationt4,font=11)
        eissue = tk.Entry(wrapper1, textvariable=issuet5,font=11)

        ename.grid(row=1, column=1, ipady=5, ipadx=60)
        eemail.grid(row=2, column=1, ipady=5, ipadx=60)
        ephone.grid(row=1, column=4, ipady=5, ipadx=60)
        eissue.grid(row=2, column=4, ipady=5, ipadx=60)
        elocation.grid(row=3, column=1, ipady=5, ipadx=60)

        add_btn.grid(row=4, column=0, pady=40, ipadx=20,padx=40+40)
        delete_btn.grid(row=4, column=1, pady=40, ipadx=30,padx=40)
        cancel_btn.grid(row=4, column=2, pady=40, ipadx=30,padx=20)

        Button = tk.Button(self, text="Register", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage), relief=FLAT, cursor='hand2')
        Button.place(x=0, y=5, width=300, height=50)  # x=100, y=450
        '''Button = tk.Button(self, text="User Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=120, y=5)'''
        Button = tk.Button(self, text="Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage), relief=FLAT, cursor='hand2')
        Button.place(x=300, y=5, width=250, height=50)
        Button = tk.Button(self, text="Admin Page", font=("Arial", 15), bg="dark blue",
                           command=loginAdmin, relief=FLAT, cursor='hand2')
        Button.place(x=500, y=5, width=250, height=50)

        # image bachground

        # Add Image inside the Canvas


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="blue")

        def clearLoginD():

            adminlogin_entry.delete(0, END)
            adminlogin_entrypasswordEntry.delete(0, END)

        ####admin login
        def verifying_admin():
            admin = adminlogin_entry.get()
            password_admin = adminlogin_entrypasswordEntry.get()
            if adminlogin_entry == "" and adminlogin_entrypasswordEntry == "":
                messagebox.showerror("Enty Entries", "Provide your Details")
            elif adminlogin_entry == 'Admin' and adminlogin_entrypasswordEntry == "123":
                btn = Button(self, text="Admin", font=("Arial", 15), bg="dark blue",
                             command=lambda: controller.show_frame(self.AdminPage))
                btn.place(x=600, y=10)
                clearLoginD()
            else:
                messagebox.showerror("Error", "Contact Developer")
                loginAdmin()

        def loginAdmin():
            global T1, T2
            global window1
            global admin_verifier
            global adminlogin_entry
            global adminlogin_entrypasswordEntry
            global password_admin
            password_admin = StringVar()
            admin_verifier = StringVar()

            window1 = tk.Tk()
            window1.geometry('500x300+400+250')
            window1.config(bg='skyblue')
            label = Label(window1, text="Admin Login", bg="skyblue", fg="black", padx=5, pady=5,
                          font=("Algerian", 18))
            label.place(x=220, y=2)
            Label(text="Login").pack()
            adminloginlabel = Label(window1, text="User name", bg='SkyBlue', font=12)
            adminloginlabel.place(x=50, y=80)

            adminlogin_entry = Entry(window1, textvariable=admin_verifier, width=30, font=12)
            adminlogin_entry.place(x=150, y=80, height=25)

            adminlogin_entrypasswordLabel = Label(window1, text="password", font=12, bg='SkyBlue')
            adminlogin_entrypasswordLabel.place(x=50, y=130)
            adminlogin_entrypasswordEntry = Entry(window1, textvariable=password_admin, width=30, font=12, show="*")
            adminlogin_entrypasswordEntry.place(x=150, y=130)
            login_btn = Button(window1, text="Login here", command=verifying_admin, height=1, width=20)
            login_btn.place(x=150, y=180)

        def browsing():
            global root21
            locating=ent_location.get()
            dd=print(locating)
            root21=Tk()
            map_widget = TkinterMapView(root21, width=500, height=300, corner_radius=0)
            map_widget.pack(fill="both", expand=True)

            # google normal tile server
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

            map_widget.set_address(dd, marker=True)
            root21.mainloop()

        def locate_onmap():
            global root20

            locating = ent_location.get()

            driver = webdriver.Chrome(
                "C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe")
            driver.get(f"https://www.google.com/maps/@0.1768696,37.9083264z")
            sleep(2)

            # xpath is stand for XML path language, uses path expression to identify and navigate nodes in an XML document can be use to
            # select  one/more nodes in the document by using absolute / relative path

            def searchplace():
                Place = driver.find_element_by_class_name('tactile-searchbox-input')
                Place.send_keys(locating)
                submit = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
                submit.click()

            searchplace()

            def direction():
                sleep(10)
                direction = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button")
                direction.click()

            direction()

            def find():
                sleep(10)
                find = driver.find_element_by_xpath(
                    '/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
                find.send_keys("London")
                search = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                search.click()

            find()

            def distancetime():
                sleep(8)
                distance = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div")
                print("Total Distance: ", distance.text)

                car = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[1]/span[1]")
                print("Time Take by Vehcile: ", car.text)

                train = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[2]/div[1]/div")
                print("Time Take by Train: ", train.text)

                aroplane = driver.find_element_by_xpath(
                    "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[3]/div/div[4]/div[1]/div/div[1]")
                print("Time Take by Aroplane: ", aroplane.text)

            distancetime()

            '''map_widget = TkinterMapView(root20, width=800, height=500, corner_radius=0)
            map_widget.pack(fill="both", expand=True)

            # google normal tile server
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=80)

            map_widget.set_address(locating, marker=True)'''



        connection = mysql.connector.connect(host='localhost',
                                             database='basecare_db',
                                             user='root',
                                             password="")
        mycursor = connection.cursor()

        # mycursor.execute("CREATE TABLE customers ( customer_Id VARCHAR(50), FirstName VARCHAR(50)),LastName VARCHAR(50),AGE VARCHAR(3)")

        # database connection ,,,Age
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='basecare_db',
                                                 user='root',
                                                 password="")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        # function to add data to the treeview.
        def update(rows):
            self.trv.delete(*self.trv.get_children())
            for i in rows:
                self.trv.insert('', 'end', values=i)

        def clearind_inAdminaerea():
            et1.delete(0, END)
            et2.delete(0, END)
            et3.delete(0, END)
            et4.delete(0, END)
            et5.delete(0, END)

            # for admin

        def search_comment():
            pass

        def search_details():
            q_details = ent_details.get()

            print(q_details)
            query = "SELECT name,email,phonenumber,location,issue FROM details_table WHERE email Like'%" + q_details + "%' OR name Like'%" + q_details + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)

        def view_record():
            search_details()

        # clear function
        def getrow(event):
            rowid = self.trv.identify_row(event.y)
            item = self.trv.item(self.trv.focus())
            # grabbing all items and setting them t's
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])
            t5.set(item['values'][4])
        def update_customer():
            name = t1.get()
            email = t2.get()
            phone = t3.get()
            location = t4.get()
            issue = t5.get()
            try:
                if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
                    query = ("UPDATE\
                     details_table SET name=%s,email=%s,phonenumber=%s,location=%s,issue=%s WHERE email=%s")
                    valuess = (name, email, phone, location, issue, email)
                    cursor.execute(query, valuess)
                    mydb.commit()
                    clearind_inAdminaerea()
                    messagebox.showinfo("Success", "updated successfully")
                else:

                    messagebox.showerror("canceled", "You cancelled Succefully")
            except:
                messagebox.showerror("Hey look ", "your data are not submitted")

        def add_new():
            name = t1.get()
            email = t2.get()
            phone = t3.get()
            location = t4.get()
            issue = t5.get()

            if messagebox.askyesno("Confirm adding Data",
                                   "Are you sure Your Want to add Customer to Database Customer"):
                query = "INSERT INTO details_table (name,email,phonenumber,location,issue ) VALUES(%s,%s,%s,%s,%s)"
                clearind_inAdminaerea()
                if name == "" and email == "" and issue == "" and phone == "" and location == "":
                    messagebox.showwarning("You can't add Empty ")
                    if '@' not in email and '.com' not in email:
                        messagebox.showwarning("warning ", "enter valid Email  address")
                else:
                    cursor.execute(query, (name, email, phone, location, issue))
                    try:
                        mydb.commit()
                        clearind_inAdminaerea()
                        messagebox.showinfo("information", "Employee inserted successfully...")
                        self.trv.insert('', 'end', values=(name, email, phone, location, issue))
                    except:
                        messagebox.showerror("hey look", "Your data are not Sumitted")
                        mydb.rollback()
                    mydb.close()
            else:
                return True

        def delete_customer():
            email = t2.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
                query = "DELETE FROM details_table WHERE email =%s"
                val = (email,)
                cursor.execute(query, val)
                clearind_inAdminaerea()
                mydb.commit()
                messagebox.showinfo("success", "You have deleted the comment successfully")

            else:
                return True

        # frontend :::::::::::::::::::::
        mydb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
        cursor = mydb.cursor()
        q = StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()
        locatingV = StringVar()
        wrapper3 = LabelFrame(self, text="Customer Data")
        wrapper3.place(x=0, y=480, width=1900, height=240)
        self.trv = ttk.Treeview()
        # treeview for client details
        s = ttk.Style()
        s.theme_use('clam')
        s.configure(self.trv, font=12)
        self.trv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5), show="headings", height="18")
        self.trv.place(x=0, y=50)
        self.trv.heading(1, text="Name")
        self.trv.column(1, minwidth=100, width=120)
        self.trv.heading(2, text="Email")
        self.trv.column(2, minwidth=100, width=120)
        self.trv.heading(3, text="Phone")
        self.trv.column(3, minwidth=0, width=120)
        self.trv.heading(4, text="Location")
        self.trv.column(4, minwidth=0, width=120)
        self.trv.heading(5, text='Issue')
        self.trv.column(5, minwidth=0, width=100)
        # adding v scrollbar
        treescroll = ttk.Scrollbar(self.trv)
        treescroll.configure(command=self.trv.yview)
        self.trv.configure(yscrollcommand=treescroll.set)
        treescroll.place(x=570, y=50, height=300)

        self.trv.bind('<Double 1>', getrow)

        # querying
        query = "SELECT name,email,phonenumber,location,issue from details_table"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)

        # search section
        # REMOVED IN THE PROGRAM
        def clear_search():
            ent_details.delete(0, END)
            qc_searchEntry.delete(0, END)

        # search sections in the detail area
        global q_details
        global ent_details
        q_details = StringVar()
        lbl = tk.Button(wrapper3, text='Search', command=search_details, cursor='wait', relief='flat', bg='orange')
        lbl.place(x=0, y=130)
        ent_details = tk.Entry(wrapper3, textvariable=q_details, width=40, )
        ent_details.place(x=70, y=130, height=26)

        btn = tk.Button(self, text="Search", command=search_comment)
        btn.place(x=1200, y=5)
        # user data section
        lbl1 = Label(wrapper3, text="Name")
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        et1 = Entry(wrapper3, textvariable=t1)
        et1.grid(row=0, column=1, padx=5, pady=3, ipadx=25)
        lbl2 = Label(wrapper3, text="Email")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        et2 = Entry(wrapper3, textvariable=t2)
        et2.grid(row=1, column=1, padx=5, pady=3, ipadx=25)

        lbl3 = Label(wrapper3, text="Phone")
        lbl3.grid(row=0, column=2, padx=5, pady=3)
        et3 = Entry(wrapper3, textvariable=t3)
        et3.grid(row=0, column=3, padx=5, pady=3, ipadx=25)

        lbl4 = Label(wrapper3, text="Location")
        lbl4.grid(row=1, column=2, padx=5, pady=3)
        et4 = Entry(wrapper3, textvariable=t4)
        et4.grid(row=1, column=3, padx=5, pady=3, ipadx=25)

        lbl5 = Label(wrapper3, text="Issue")
        lbl5.grid(row=5, column=0, padx=5, pady=3)
        et5 = Entry(wrapper3, textvariable=t5)
        et5.grid(row=5, column=1, padx=5, pady=3, ipadx=30)

        # LOCATION BUTTON
        ent_location = Entry(self, textvariable=locatingV)
        ent_location.place(x=250, y=450, width=335, height=25)
        url_btn = tk.Button(self, text="Search Location", command=locate_onmap)
        url_btn.place(x=150, y=450)
        locatin = tk.Button(self, text='Browz Location',
                            command=browsing)
        locatin.place(x=0, y=450)

        update_btn = tk.Button(wrapper3, text="Update", command=update_customer)
        add_btn = tk.Button(wrapper3, text="Add New", command=add_new)
        delete_btn = tk.Button(wrapper3, text="Delete", command=delete_customer)
        clear_btn = tk.Button(wrapper3, text="Clear", command=clearind_inAdminaerea)
        viewrecord_btn = tk.Button(wrapper3, text="view", command=view_record)

        add_btn.place(x=0, y=170, width=80)
        update_btn.place(x=80, y=170, width=80)
        delete_btn.place(x=160, y=170, width=80)
        clear_btn.place(x=240, y=170, width=80)
        viewrecord_btn.place(x=320, y=170, width=80)

        #############

        Button = tk.Button(self, text="Register", font=("Arial", 15), bg="dark blue", width=10,
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=0)  # x=100, y=450
        '''Button = tk.Button(self, text="Second Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=113, y=0)'''
        Button = tk.Button(self, text="User Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=100, y=0)
        Button = tk.Button(self, text="User Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FouthPage), width=100)
        Button.place(x=240, y=0)

        Button = tk.Button(self, text="Admin", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(AdminPage))
        Button.place(x=365, y=0, width=150)
        Button = tk.Button(self, text="login ", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage), relief=FLAT)
        Button.place(x=480, y=0)
        from time import strftime
        def time():
            string = strftime('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)

        label = Label(self, font=("Algerian", 40), background="white", foreground="cyan")
        label.place(x=1050, y=50)
        time()

        #   COMMENT SECTION AND TREEVIEW

        connection = mysql.connector.connect(host='localhost',
                                             database='basecare_db',
                                             user='root',
                                             password="")
        mycursor = connection.cursor()

        # mycursor.execute("CREATE TABLE customers ( customer_Id VARCHAR(50), FirstName VARCHAR(50)),LastName VARCHAR(50),AGE VARCHAR(3)")
        # database connection ,,,Age
        # function to add data to the treeview.
        def updateComments(rows):
            trvz.delete(*trvz.get_children())
            for i in rows:
                trvz.insert('', 'end', values=i)

        def searchComments():
            q2 = qc_searchEntry.get()
            query = "SELECT comment,email FROM comments WHERE email Like'%" + q2 + "%' OR email Like'%" + q2 + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            updateComments(rows)

        # clear function
        def clearComments():
            ccomments = comment.delete(1.0, END)
            cemail = ent2.delete(0, END)

        def getrowComments(event):
            rowid = trvz.identify_row(event.y)
            item = trvz.item(trvz.focus())
            # grabbing all items and setting them t's
            comment.insert(1.0, item['values'][0])
            t8.set(item['values'][1])

        def update_customerComments():
            comments = ent1.get()
            email = t8.get()
            try:
                if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
                    query = "UPDATE comments SET comment=%s,email=%s WHERE email=%s"
                    val = (comments, email)
                    cursor.execute(query, val)
                    mydb.commit()
                    clearComments()
                    messagebox.showinfo("Success", "The data is successfully updated")
                else:
                    return True
            except:
                messagebox.showerror("Check your details ", "Check before You  update")

        def add_newComments():
            comments = ent1.get()
            email = t8.get()
            if '@' not in email and '.com' not in email:
                messagebox.showwarning("warning ", "enter valid Email  address")
            elif comments != "" and email != "":
                messagebox.showwarning("You can't add Empty ")
                query = "INSERT INTO comments (comment,email ) VALUES(%s,%s)"
                cursor.execute(query, (comments, email))
                mydb.commit()
                clearComments()
                messagebox.showinfo("information", "Employee inserted successfully...")
                clearComments()
            else:
                messagebox.showwarning("check it", "Check your details")

        def delete_customerComments():
            email = t8.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
                query = "DELETE FROM comments WHERE email=%s"
                val = (email,)
                cursor.execute(query, val)
                mydb.commit()
                clearComments()
                messagebox.showinfo("success deletion", "you have deleted the data successfully")
            else:
                return True

        def view_comment():
            searchComments()

        # frontend ::::::::::::::::::::::::::::::::::::::::::::
        mydb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
        cursor = mydb.cursor()
        qc = StringVar()
        ent1 = StringVar()
        t8 = StringVar()
        # wrapper1 = LabelFrame(root, text="Customer List")
        # wrapper2 = LabelFrame(root, text="Search ")
        trvz = ttk.Treeview()
        # textarea.get(1.0, 'end')
        trvz = ttk.Treeview(self, columns=(1, 2), show="headings", height="20")
        trvz.place(x=590, y=50)
        trvz.heading(1, text="comments")
        trvz.column(1, minwidth=20, )
        trvz.heading(2, text="Email")
        trvz.column(2, minwidth=20, anchor='center')
        trvz.bind('<Double 1>', getrowComments)
        # querying
        query = "SELECT comment,email from comments"
        cursor.execute(query)
        rows = cursor.fetchall()
        updateComments(rows)
        # search section
        # search sections
        global qc_searchEntry
        qc = StringVar()
        btn = tk.Button(self, text="Search", command=searchComments, relief='flat', cursor='hand2', bg='blue', width=10,
                        height=1)
        btn.place(x=920 + 75, y=10)
        qc_searchEntry = Entry(self, textvariable=qc, width=30)
        qc_searchEntry.place(x=1000 + 80, y=10, height=25)
        cbtn = tk.Button(self, text="Clear", command=clear_search, width=10, height=1, bg='blue', cursor='hand2')
        cbtn.place(x=1300 - 30, y=10)
        # user data section
        lbl1 = Label(wrapper3, text="comments")
        lbl1.place(x=500, y=0)
        comment = tk.Text(wrapper3, width=55, height=10, font=('Calibri', 10))
        comment.place(x=600, y=0)
        lbl2 = Label(wrapper3, text="Email")
        lbl2.place(x=1030, y=0)
        ent2 = Entry(wrapper3, textvariable=t8, width=40)
        ent2.place(x=1070, y=0, height=30)
        update_btn = tk.Button(wrapper3, text="Updatec", command=update_customerComments)
        add_btn = tk.Button(wrapper3, text="Add Newc", command=add_newComments)
        delete_btn = tk.Button(wrapper3, text="Deletec", command=delete_customerComments)
        clear_btn = tk.Button(wrapper3, text="clearc", command=clearComments)
        viewcomment_btn = tk.Button(wrapper3, text="view", command=view_comment)
        update_btn.place(x=600, y=170, width=80)
        add_btn.place(x=680, y=170, width=80)
        delete_btn.place(x=760, y=170, width=80)
        clear_btn.place(x=840, y=170, width=80)
        viewcomment_btn.place(x=920, y=170, width=80)
        # adding scrollbar to text
        v = tk.Scrollbar(wrapper3, orient='vertical')
        v.place(x=1005, y=0, height=170)
        v.config(command=comment.yview)
        comment.config(yscrollcommand=v.set)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=750)
        window.grid_columnconfigure(0, minsize=1365)
        self.frames = {}
        for F in ( AdminPage,FirstPage, ThirdPage, FouthPage,):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(AdminPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()
