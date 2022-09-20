from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

# msql=mysql.connector.connect(host="localhost",user="root",password="",database="mysampledb")
connection = mysql.connector.connect(host='localhost',
                                     database='basecare_db',
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
    ccomments = ent1.delete(0, END)
    cemail = ent2.delete(0, END)


"""def clear():
    query = "SELECT name,email,phonenumber,location,issue FROM details_table"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)"""


def getrowComments(event):
    rowid = trvz.identify_row(event.y)
    item = trvz.item(trvz.focus())
    # grabbing all items and setting them t's
    ent1.insert(1.0, item['values'][0])
    t8.set(item['values'][1])


def update_customerComments():
    comments = ent1.get()
    email = t8.get()
    '''phone = t3.get()
    location = t4.get()
    issue = t5.get()'''
    if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
        query = "UPDATE details_table SET comment=%s,email=%s WHERE email=%s"
        cursor.execute(query, (comments, email,))
        mydb.commit()
        clearComments()
    else:
        return True


print("the is the main job is good ")


def add_newComments():
    comments = ent1.get(1.0, 'end')
    email = t8.get()

    if messagebox.askyesno("Confirm adding Data", "Are you sure Your Want to add Customer to Database Customer"):
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


# frontend ::::::::::::::::::::::::::::::::::::::::::::
mydb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
cursor = mydb.cursor()

root = Tk()

root.title()
root.geometry("800x700")
root.title("timOketch@tech")
root.config(bg="green")
qc = StringVar()
ent1 = StringVar()
t8 = StringVar()

# wrapper1 = LabelFrame(root, text="Customer List")
# wrapper2 = LabelFrame(root, text="Search ")
wrapper3 = LabelFrame(root, text="Customer Data")

# wrapper1.pack(fill="both", expand="yes", padx=40, pady=10)
# wrapper2.pack(fill="both", expand="yes", padx=40, pady=10)
wrapper3.place(x=0, y=490, width=1400, height=400)
trvz = ttk.Treeview()
# textarea.get(1.0, 'end')
trvz = ttk.Treeview(root, columns=(1, 2), show="headings", height="18")
trvz.place(x=600, y=50)
trvz.heading(1, text="comments")
trvz.heading(2, text="Email")

trvz.bind('<Double 1>', getrowComments)
# querying

query = "SELECT comment,email from comments"
cursor.execute(query)
rows = cursor.fetchall()
updateComments(rows)

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
ent = Entry(root, textvariable=qc)
ent.place(x=1145, y=10)
btn = tk.Button(root, text="search", command=searchComments)
btn.place(x=1270, y=10)
cbtn = tk.Button(root, text="Clear", command=clearComments)
cbtn.place(x=1320, y=10)

# user data section

lbl1 = Label(wrapper3, text="comments")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Text(wrapper3, width=50, height=10)
ent1.place(x=600, y=0)

lbl2 = Label(wrapper3, text="Email")
lbl2.place(x=1010, y=0)
ent2 = Entry(wrapper3, textvariable=t8,width=50)
ent2.place(x=1050, y=0)

update_btn = Button(wrapper3, text="Updatec", command=update_customerComments)
add_btn = Button(wrapper3, text="Add Newc", command=add_newComments)
delete_btn = Button(wrapper3, text="Deletec", command=delete_customerComments)
clear_btn = Button(wrapper3, text="clearc", command=clearComments)


update_btn.place(x=600, y=170)
add_btn.place(x=680, y=170)
delete_btn.place(x=760, y=170)
clear_btn.place(x=840, y=170)

root.mainloop()
root.geometry("800x700")
