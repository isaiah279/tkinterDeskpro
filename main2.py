from tkinter import ttk
import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image,ImageTk
import  os
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
global email
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


def loginAdmin():
    window = tk.Tk()
    L1 = tk.Label(window, text="User name", font=("Arial Bold", 15), bg='blue')
    L1.place(x=50, y=20)

    T1 = tk.Entry(window, width=30, bd=0)
    T1.place(x=180, y=20)

    L2 = tk.Label(window, text="Password", font=("Arial Bold", 15), bg='blue')
    L2.place(x=50, y=80)

    T2 = tk.Entry(window, width=30, bd=0, show="*")
    T2.place(x=180, y=80)


    def verifying():
        if T1.get() == 'isaiah' and T2.get() == "12345":
            window.show_frame(FouthPage)
        else:
            messagebox.showinfo("Error", "provide correct details")


            messagebox.showinfo("Error ", "please provide correct user name")

        login_btn = tk.Button(window, text="Login", command=verifying)
        login_btn.place(x=180, y=130, width=70)


class FirstPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="tomato")
        emailAddress=StringVar()
        password1=StringVar()
        password2=StringVar()

        def submit(self):
            pass

        bordering = tk.LabelFrame(self, text="Login", font=("Arial Bold", 20), bd=1, bg="Blue", fg="orange")
        bordering.pack(fill="both", expand='yes', padx=150, pady=150)

        L1 = tk.Label(bordering, text="User name", font=("Arial Bold", 15),bg='blue')
        L1.place(x=50, y=20)

        T1 = tk.Entry(bordering, width=30, bd=0)
        T1.place(x=180, y=20)

        L2 = tk.Label(bordering, text="Password", font=("Arial Bold", 15),bg='blue')
        L2.place(x=50, y=80)

        T2 = tk.Entry(bordering, width=30, bd=0, show="*")
        T2.place(x=180, y=80)

        def verify_user():
            global  emailAddress
            global  password1
            global password2
            emailAddress = StringVar()
            password1 = StringVar()
            password2 = StringVar()
            email_verify=emailAddress.get()
            password1_verify=password1.get()
            password2_verify=password2.get()
            os_list=os.listdir()
            if email_verify in os_list:
                file=open("userInfo.txt","r")
                v=file.read().split()
                if password1_verify in v:
                    messagebox.showinfo("Success","Login Success")
                else:
                    messagebox.showinfo("not found","Wrong password used")
            else:
                messagebox.showerror("error","You have not registered")

            """if T1.get() == 'isaiah' and T2.get() == "12345":
                controller.show_frame(SecondPage)
            else:
                messagebox.showinfo("Error", "provide correct details")
            """


        login_btn = tk.Button(bordering, text="Login", command=verify_user)
        login_btn.place(x=180, y=130,width=70)

        def otp_fuction():
            pass
        # register button


        def register():

            window = tk.Tk()
            window.title("Register")
            #window.eval('tk::PlaceWindow.center')
            window.geometry('+500+300')
            window.configure(bg="deep sky blue")
            window.resizable(0, 0)

            username_label = tk.Label(window, text="Email Address", font=("Arial", 12), bg="deep sky blue")
            username_label.place(x=10, y=10)
            username_ent = tk.Entry(window, width=30,textvariable=emailAddress)
            username_ent.place(x=150, y=10)

            password_label = tk.Label(window, text="Password", font=("Arial", 12), bg="deep sky blue")
            password_label.place(x=10, y=50)
            password_ent = tk.Entry(window, text="Password", width=30, show="*",textvariable=password1)
            password_ent.place(x=150, y=50)
            password_conf_label = tk.Label(window, text="Confirm Password", font=("Arial", 12), bg="deep sky blue")
            password_conf_label.place(x=10, y=100)
            password_conf_ent = tk.Entry(window, width=30, show="*",textvariable=password2)
            password_conf_ent.place(x=150, y=110)


                #OTP generation




            def check():
                emailget=emailAddress.get()
                passwordget1=str(password1.get())
                passwordget2 = str(password2.get())

                file=open("userInfo.txt","w")
                file.write(emailget)
                file.write(passwordget1)
                file.write(passwordget2)
                file.close()

                print("User registered successfully")


                """emailget=self.emailAddress.get()
                passwordget1=self.password1.get()
                passwordget2=self.password2.get()
                s='\n'+  emailget + '\t' + passwordget1 + '\t ' + passwordget2
                f=open(('regdetails.txt'),'a')
                f.write(s)
                f.close()"""

                '''vals = (emailget, passwordget1,passwordget2)
                mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
                mycursor = mysqldb.cursor()
                if messagebox.askyesno("Confirm adding Data",
                                       "Are you sure Your Want to add Customer to Database Customer"):
                    query = "INSERT INTO registration (useremail,password1,password2 ) VALUES(%s,%s,%s)"

                    if self.emailAddress == "" and self.password2 == "" and self.password1 == "" :
                        messagebox.showwarning("You can't add Empty ")
                        if '@' not in emailget and '.com' not in emailget:
                            messagebox.showwarning("warning ", "enter valid Email  address")
                    else:
                        mycursor.execute(query, (emailget,passwordget1,passwordget2))
                        try:
                            mysqldb.commit()

                            messagebox.showinfo("information", "Employee inserted successfully...")
                        except:
                            mysqldb.rollback()
                        mysqldb.close()'''


            #register()

            b1 = tk.Button(window, text="Register now ", bg="orange", command=check)
            b1.place(x=230, y=150)

            window.geometry("470x220")

        register_btn = tk.Button(bordering, text="Register",  bg="orange", command=register)
        register_btn.place(x=300, y=130,width=70)

        Next_btn = tk.Button(self, text="Next", command=lambda: controller.show_frame(FouthPage))
        Next_btn.place(x=750, y=0)
        finder = tk.Label(self, text="First Page")
        finder.place(x=1250, y=0)

#self.after(5000,FouthPage)
#SecondPage.destroy()


class ThirdPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        self.configure(bg="deep sky blue")
        self.texting = tk.StringVar()
        self.email = tk.StringVar()

        self.na = tk.Label(self,text="The commenting page of the System", font=('Helvetica', 26, 'bold'))
        self.na.pack(pady=20)
        self.wrapper1 = tk.LabelFrame(self, text="Write Comment", fg="White", bg="dark blue", font=('Arial', 14),
                                      border=10)
        self.wrapper1.pack(fill="both", expand="true", padx=0, pady=80, ipady=2)
        textarea = tk.Text(self.wrapper1, width=25, height=15, font=20, fg="green")
        textarea.pack(ipady=50, ipadx=200, anchor='center', pady=20)
        self.lemail = tk.Label(self.wrapper1, text="Enter Your Email", bg='dark blue', font=20)
        self.lemail.place(x=358, y=430)
        email = tk.Entry(self.wrapper1, textvariable=self.email, width=20)
        email.pack(ipadx=50, ipady=10, anchor='center')

        def clear():
            textarea.delete(1.0, END)
            email.delete(0, END)

        def send_comment():
            mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
            mycursor = mysqldb.cursor()
            comment = textarea.get(1.0, 'end')
            send_Email = self.email.get()
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

        def clear_btn():
            clear()

        def exit_btn():
            self.destroy()

        # action buttons
        send_btn = tk.Button(self.wrapper1, text="send Comment", command=send_comment)
        send_btn.place(x=350, y=500)
        clear_btn = tk.Button(self.wrapper1, text="Clear Comment", command=clear_btn)
        clear_btn.place(x=500, y=500)
        exit_btn = tk.Button(self.wrapper1, text="Exit page", command=exit_btn)
        exit_btn.place(x=650, y=500)

        Button = tk.Button(self, text="Home", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=5, y=15)
        Button = tk.Button(self, text="FirstPage", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=80, y=15)
        '''Button = tk.Button(self, text="Navigate", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=190, y=15)'''

        Button = tk.Button(self, text="FouthPage", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FouthPage))
        Button.place(x=295, y=15)  # x=100, y=450

        finder = tk.Label(self, text="Third Page")
        finder.place(x=1250, y=0)


class FouthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        # varaible declaration
        self.configure(bg="blue")
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
            global  mysqldb
            global mycursor
            self.val = (name, email, phone, location, issue, name,)
            mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
            mycursor = mysqldb.cursor()

            # Empty Validation
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

            # data issertion goes here

        def clear_information():
            clear()

        def cancel_information():
            clear()

        # phone, email, name, location, issue
        wrapper1 = tk.LabelFrame(self, text="Enter Details", bg="blue")
        wrapper2 = tk.LabelFrame(self, text="Actions Required")

        wrapper2.config(bg="green")
        wrapper1.pack(fill="both", expand='yes', pady=50)

        # actions
        add_btn = tk.Button(wrapper1, text="Submit Request", command=add_information)
        delete_btn = tk.Button(wrapper1, text="Clear", command=clear_information)
        cancel_btn = tk.Button(wrapper1, text="Cancel", command=cancel_information)

        # labels
        lname = tk.Label(wrapper1, text="Name:", bg='blue')
        lemail = tk.Label(wrapper1, text="Email:", bg='blue')
        lphone = tk.Label(wrapper1, text="Phone:", bg='blue')
        lissue = tk.Label(wrapper1, text="Issue:", bg='blue')
        llocation = tk.Label(wrapper1, text="Location", bg='blue')
        id_number = tk.Label(wrapper1, text="Location", bg='blue')

        # grids

        lname.grid(row=1, column=0, padx=20, pady=60)
        lemail.grid(row=2, column=0, padx=20)
        lphone.grid(row=1, column=3, padx=20, pady=20)
        llocation.grid(row=2, column=3, padx=20, pady=20)
        lissue.grid(row=3, column=0, padx=20, pady=40)

        # Setting variable into the entry points
        ename = tk.Entry(wrapper1, textvariable=namet1)
        eemail = tk.Entry(wrapper1, textvariable=emailt2)
        ephone = tk.Entry(wrapper1, textvariable=phonet3)
        elocation = tk.Entry(wrapper1, textvariable=locationt4)
        eissue = tk.Entry(wrapper1, textvariable=issuet5)

        ename.grid(row=1, column=1, ipady=5, ipadx=60)
        eemail.grid(row=2, column=1, ipady=5, ipadx=60)
        ephone.grid(row=1, column=4, ipady=5, ipadx=60)
        eissue.grid(row=2, column=4, ipady=5, ipadx=60)
        elocation.grid(row=3, column=1, ipady=5, ipadx=60)

        add_btn.grid(row=4, column=1, pady=40, ipadx=20)
        delete_btn.grid(row=4, column=2, pady=40, ipadx=20)
        cancel_btn.grid(row=4, column=3, pady=40, ipadx=20, padx=5)

        Button = tk.Button(self, text="Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=5)  # x=100, y=450
        '''Button = tk.Button(self, text="User Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=120, y=5)'''
        Button = tk.Button(self, text="Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=240, y=5)
        Button = tk.Button(self, text="Admin Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(AdminPage))
        Button.place(x=360, y=5)

        finder = tk.Label(self, text="Fouth Page")
        finder.place(x=1250, y=0)
        listing = [ename, eemail, ephone, eissue, elocation]


class AdminPage(tk.Frame):
    #loginAdmin()
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg="blue")




        def locate_onmap():

            locating = locatingV.get()
            if locating != "":
                root = Tk()
                map_widget = TkinterMapView(root, width=600, height=400, corner_radius=0)
                map_widget.pack(fill="both", expand=True)

                # google normal tile server
                map_widget.set_tile_server(root, "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                           max_zoom=22)

                map_widget.set_address(root, locating, marker=True)
                if locate_onmap() is False:
                    print()
            else:
                messagebox.showwarning("Error", "Paste the url ")
            root.mainloop()

        # def comments():
        # function to add data to the treeview.

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
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        # function to add data to the treeview.

        def update(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end', values=i)

        def search():
            q2 = q.get()
            query = "SELECT name,email,phonenumber,location,issue FROM details_table WHERE name Like'%" + q2 + "%' OR name Like'%" + q2 + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)

        # clear function
        def clear():
            pass
            #t1=ent.delete(0,END)
            #cname = ent1.delete(0, END)
            '''cemail = ent2.delete(0, END)
            cphone = ent3.delete(0, END)
            clocation = ent4.delete(0, END)
            cissue = ent5.delete(0, END)'''

        """def clear():
            query = "SELECT name,email,phonenumber,location,issue FROM details_table"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)"""

        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
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
            if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
                query =( "UPDATE\
                 details_table SET name=%s,email=%s,phonenumber=%s,location=%s,issue=%s WHERE email=%s")
                valuess=(name,email,phone,location,issue,email)
                cursor.execute(query,valuess)
                mydb.commit()
                clear()
                messagebox.showinfo("Success","updated successfully")
            else:

                messagebox.showerror("canceled","You cancelled Succefully")


        def add_new():
            name = t1.get()
            email = t2.get()
            phone = t3.get()
            location = t4.get()
            issue = t5.get()

            if messagebox.askyesno("Confirm adding Data",
                                   "Are you sure Your Want to add Customer to Database Customer"):
                query = "INSERT INTO details_table (name,email,phonenumber,location,issue ) VALUES(%s,%s,%s,%s,%s)"
                clear()
                if name == "" and email == "" and issue == "" and phone == "" and location == "":
                    messagebox.showwarning("You can't add Empty ")
                    if '@' not in email and '.com' not in email:
                        messagebox.showwarning("warning ", "enter valid Email  address")
                else:
                    cursor.execute(query, (name, email, phone, location, issue))
                    try:
                        mydb.commit()
                        clear()
                        messagebox.showinfo("information", "Employee inserted successfully...")
                    except:
                        mydb.rollback()
                    mydb.close()


            else:
                return True
        def view_record():
            pass



        def delete_customer():
            email = t2.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
                query = "DELETE FROM details_table WHERE email =%s"+email
                cursor.execute(query)
                mydb.commit()
                clear()
            else:
                return True

        # frontend ::::::::::::::::::::::::::::::::::::::::::::
        mydb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
        cursor = mydb.cursor()


        q = StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()


        locatingV = tk.StringVar()
        # wrapper1 = LabelFrame(root, text="Customer List")
        # wrapper2 = LabelFrame(root, text="Search ")
        wrapper3 = LabelFrame(self, text="Customer Data")

        # wrapper1.pack(fill="both", expand="yes", padx=40, pady=10)
        # wrapper2.pack(fill="both", expand="yes", padx=40, pady=10)
        wrapper3.place(x=0, y=480, width=1900, height=240)
        trv = ttk.Treeview()

        # treeview for client details
        s = ttk.Style()
        s.theme_use('clam')

        trv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5), show="headings", height="18")
        trv.place(x=0, y=50)
        trv.heading(1, text="Name")
        trv.column(1, minwidth=100, width=120)
        trv.heading(2, text="Email")
        trv.column(2, minwidth=100, width=120)
        trv.heading(3, text="Phone")
        trv.column(3, minwidth=0, width=120)
        trv.heading(4, text="Location")
        trv.column(4, minwidth=0, width=120)
        trv.heading(5, text='Issue')
        trv.column(5, minwidth=0, width=100)
        #adding v scrollbar
        treescroll=ttk.Scrollbar(trv)
        treescroll.configure(command=trv.yview)
        trv.configure(yscrollcommand=treescroll.set)
        treescroll.place(x=570, y=50,height=300)


        trv.bind('<Double 1>', getrow)
        # querying

        query = "SELECT name,email,phonenumber,location,issue from details_table"
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)

        # search section
        # REMOVED IN THE PROGRAM


        # search sections
        lbl = Label(self, text='Search', bg='green', font=18)
        lbl.place(x=1090, y=5)
        ent = Entry(self, textvariable=q)
        ent.place(x=1145, y=5)
        btn = tk.Button(self, text="search", command=search)
        btn.place(x=1270, y=5)
        cbtn = tk.Button(self, text="Clear", command=clear)
        cbtn.place(x=1320, y=5)

        # user data section

        lbl1 = Label(wrapper3, text="Name")
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        ent1 = Entry(wrapper3, textvariable=t1)
        ent1.grid(row=0, column=1, padx=5, pady=3, ipadx=25)

        lbl2 = Label(wrapper3, text="Email")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = Entry(wrapper3, textvariable=t2)
        ent2.grid(row=1, column=1, padx=5, pady=3, ipadx=25)

        lbl3 = Label(wrapper3, text="Phone")
        lbl3.grid(row=0, column=2, padx=5, pady=3)
        ent3 = Entry(wrapper3, textvariable=t3)
        ent3.grid(row=0, column=3, padx=5, pady=3, ipadx=25)

        lbl4 = Label(wrapper3, text="Location")
        lbl4.grid(row=1, column=2, padx=5, pady=3)
        ent4 = Entry(wrapper3, textvariable=t4)
        ent4.grid(row=1, column=3, padx=5, pady=3, ipadx=25)

        lbl5 = Label(wrapper3, text="Issue")
        lbl5.grid(row=5, column=0, padx=5, pady=3)
        ent5 = Entry(wrapper3, textvariable=t5)
        ent5.grid(row=5, column=1, padx=5, pady=3, ipadx=30)

        # LOCATION BUTTON

        location_label = tk.Label(self, text=" Locate The Client :", font=18, bg='blue')
        location_label.place(x=0, y=450)
        ent_location = tk.Entry(self, textvariable=locatingV)
        ent_location.place(x=250, y=450, width=335, height=25)
        url_btn = tk.Button(self, text="Search Location", command=locate_onmap)
        url_btn.place(x=150,y=450)

        update_btn = tk.Button(wrapper3, text="Update", command=update_customer)
        add_btn = tk.Button(wrapper3, text="Add New", command=add_new)
        delete_btn = tk.Button(wrapper3, text="Delete", command=delete_customer)
        clear_btn = tk.Button(wrapper3, text="Clear", command=clear)
        viewrecord_btn = tk.Button(wrapper3, text="view", command=view_record)

        add_btn.place(x=0, y=170,width=80)
        update_btn.place(x=80, y=170,width=80)
        delete_btn.place(x=160, y=170,width=80)
        clear_btn.place(x=240, y=170,width=80)
        viewrecord_btn.place(x=320, y=170, width=80)

        #############

        Button = tk.Button(self, text="Registration", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=0)  # x=100, y=450
        '''Button = tk.Button(self, text="Second Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=113, y=0)'''
        Button = tk.Button(self, text="User Comments", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage))
        Button = tk.Button(self, text="User Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FouthPage),width=100)
        Button.place(x=240, y=0)
        Button = tk.Button(self, text="Admin", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(AdminPage))
        Button.place(x=365, y=0,width=150)
        Button = tk.Button(self, text="login ", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=480, y=0)
        from time import strftime
        def time():
            string = strftime('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)

        label = Label(self, font=("Algerian", 40), background="white", foreground="cyan")
        label.place(x=1050,y=50)
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
            q2 = qc.get()
            query = "SELECT comment,email FROM comment WHERE email Like'%" + q2 + "%' OR email Like'%" + q2 + "%'"
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

            if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
                query = "UPDATE details_table SET comment=%s,email=%s WHERE email=%s"
                cursor.execute(query, (comments, email,))
                mydb.commit()
                clearComments()
            else:
                return True



        def add_newComments():
            comments = ent1.get(1.0, 'end')
            email = t8.get()

            if messagebox.askyesno("Confirm adding Data",
                                   "Are you sure Your Want to add Customer to Database Customer"):
                query = "INSERT INTO details_table (name,email,phonenumber,location,issue ) VALUES(%s,%s,%s,%s,%s)"
                clearComments()
                if comments == "" and email == "" and comments == "":
                    messagebox.showwarning("You can't add Empty ")
                    if '@' not in email and '.com' not in email:
                        messagebox.showwarning("warning ", "enter valid Email  address")
                else:
                    cursor.execute(query, (comments, email))
                    mydb.commit()
                    clearComments()
                    messagebox.showinfo("information", "Employee inserted successfully...")

            else:
                return True

        def delete_customerComments():
            email = t8.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
                query = "DELETE FROM details_table WHERE email=" + email
                cursor.execute(query)
                mydb.commit()
                clearComments()
            else:
                return True
        def view_comment():
            pass


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
        trvz.heading(2, text="Email")

        trvz.bind('<Double 1>', getrowComments)
        # querying

        query = "SELECT comment,email from comments"
        cursor.execute(query)
        rows = cursor.fetchall()
        updateComments(rows)

        # search section

        # search sections
        lbl = Label(self, text='Search', bg='green', font=18)
        lbl.place(x=1090, y=10)
        ent = Entry(self, textvariable=qc)
        ent.place(x=1145, y=10)
        btn = tk.Button(self, text="search", command=searchComments)
        btn.place(x=1270, y=10)
        cbtn = tk.Button(self, text="Clear", command=clearComments)
        cbtn.place(x=1320, y=10)

        # user data section

        lbl1 = Label(wrapper3, text="comments")
        lbl1.place(x=500, y=0)
        comment = tk.Text(wrapper3, width=50, height=10,font=('Calibri',10))
        comment.place(x=600, y=0)

        lbl2 = Label(wrapper3, text="Email")
        lbl2.place(x=1030, y=0)
        ent2 = Entry(wrapper3, textvariable=t8, width=40)
        ent2.place(x=1070, y=0,height=30)

        update_btn = tk.Button(wrapper3, text="Updatec", command=update_customerComments)
        add_btn = tk.Button(wrapper3, text="Add Newc", command=add_newComments)
        delete_btn = tk.Button(wrapper3, text="Deletec", command=delete_customerComments)
        clear_btn = tk.Button(wrapper3, text="clearc", command=clearComments)
        viewcomment_btn = tk.Button(wrapper3, text="view", command=view_comment)



        update_btn.place(x=600, y=170,width=80)
        add_btn.place(x=680, y=170,width=80)
        delete_btn.place(x=760, y=170,width=80)
        clear_btn.place(x=840, y=170,width=80)
        viewcomment_btn.place(x=920, y=170, width=80)

        # adding scrollbar to text

        v= tk.Scrollbar(wrapper3,orient='vertical')

        v.place(x=1005,y=0,height=170)
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
        for F in (FirstPage,AdminPage, ThirdPage, FouthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()
