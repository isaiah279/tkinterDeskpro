from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

# msql=mysql.connector.connect(host="localhost",user="root",password="",database="mysampledb")
connection = mysql.connector.connect(host='localhost',
                                     database='mysampledb',
                                     user='root',
                                     password="")
mycursor = connection.cursor()

# mycursor.execute("CREATE TABLE customers ( customer_Id VARCHAR(50), FirstName VARCHAR(50)),LastName VARCHAR(50),AGE VARCHAR(3)")


# database connection ,,,Age
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mysampledb',
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
    cname=ent1.delete(0,END)
    cemail=ent2.delete(0,END)
    cphone=ent3.delete(0,END)
    clocation=ent4.delete(0,END)
    cissue=ent5.delete(0,END)
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
        query = "UPDATE details_table SET name=%s,email=%s,phonenumber=%s,location=%s,issue=%s WHERE email=%s"
        cursor.execute(query, (name, email, phone, location, issue,))
        mydb.commit()
        clear()
    else:
        return True


print("the is the main job is good ")


def add_new():
    name = t1.get()
    email = t2.get()
    phone = t3.get()
    location = t4.get()
    issue = t5.get()

    if messagebox.askyesno("Confirm adding Data", "Are you sure Your Want to add Customer to Database Customer"):
        query = "INSERT INTO details_table (name,email,phonenumber,location,issue ) VALUES(%s,%s,%s,%s,%s)"
        clear()
        if name == "" and email == "" and issue == "" and phone == "" and location == "":
            messagebox.showwarning("You can't add Empty ")
            if '@' not in email and '.com' not in email:
                messagebox.showwarning("warning ", "enter valid Email  address")
        else:
            cursor.execute(query, (name, email, phone, location, issue))
            mydb.commit()
            clear()
            messagebox.showinfo("information", "Employee inserted successfully...")

    else:
        return True


def delete_customer():
    email = t2.get()
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
        query = "DELETE FROM details_table WHERE email=" + email
        cursor.execute(query)
        mydb.commit()
        clear()
    else:
        return True


# frontend ::::::::::::::::::::::::::::::::::::::::::::
mydb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
cursor = mydb.cursor()

root = Tk()

root.title()
root.geometry("800x700")
root.title("timOketch@tech")
root.config(bg="green")
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
# wrapper1 = LabelFrame(root, text="Customer List")
# wrapper2 = LabelFrame(root, text="Search ")
wrapper3 = LabelFrame(root, text="Customer Data")

# wrapper1.pack(fill="both", expand="yes", padx=40, pady=10)
# wrapper2.pack(fill="both", expand="yes", padx=40, pady=10)
wrapper3.place(x=10, y=550, width=1000)
trv = ttk.Treeview()

trv = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), show="headings", height="4")
trv.place(x=0, y=50)
trv.heading(1, text="Name")
trv.heading(2, text="Email")
trv.heading(3, text="Phone")
trv.heading(4, text="Location")
trv.heading(5, text='Issue')
trv.bind('<Double 1>', getrow)
# querying

query = "SELECT name,email,phonenumber,location,issue from details_table"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

# search section
'''lbl = Label(wrapper2, text='search')
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=10, ipady=5)
btn = Button(wrapper2, text="search", command=search)
btn.pack(side=tk.LEFT, padx=10)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=10)'''
# search sections
lbl = Label(root, text='Search', bg='green', font=18)
lbl.place(x=1090, y=10)
ent = Entry(root, textvariable=q)
ent.place(x=1145, y=10)
btn = tk.Button(root, text="search", command=search)
btn.place(x=1270, y=10)
cbtn = tk.Button(root, text="Clear", command=clear)
cbtn.place(x=1320, y=10)

# user data section

lbl1 = Label(wrapper3, text="Name")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="Email")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="Phone")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="Location")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="Issue")
lbl5.grid(row=3, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=3, column=1, padx=5, pady=3)

update_btn = Button(wrapper3, text="Update", command=update_customer)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_customer)
clear_btn = Button(wrapper3, text="clear", command=clear)

add_btn.grid(row=4, column=0, padx=5, pady=3)
update_btn.grid(row=4, column=1, padx=5, pady=3)
delete_btn.grid(row=4, column=2, padx=5, pady=3)
clear_btn.grid(row=4, column=3, padx=5, pady=3)

root.mainloop()
root.geometry("800x700")
