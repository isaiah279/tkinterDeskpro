""""from tkinter import PhotoImage
import tkinter as tk

color = {"nero": "#272736", "orange": "#FF8700", "darkorange": "#FE6109"}
root = tk.Tk()
root.title("Tkinternav bar")

root.config(bg="gray17")
root.geometry("400x600+850+50")
# setting switch state:
btnState = False

# loading navbar image

navIcon = PhotoImage(file="menue.png")
#closeIcon = PhotoImage(file="menue.png")

# top navigation bar:

topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)
# header label

homeLabel = tk.Label(topFrame, text="PE", font="gray17", height=2, padx=20)
homeLabel.pack(side="right")

root.mainloop()
"""


from tkinter import filedialog

#file=filedialog.askopenfilename()

#dir=filedialog.askdirectory()

from os import path
#file=filedialog.askopenfilename()
import tkinter as tk

from tkinter import ttk
root=tk.Tk()
tvar = tk.StringVar()

def swaptext():
    na=tvar.get()


myent=tk.Entry(root,width=30,textvariable=tvar)
myent.place(x=100,y=0)
my_button = ttk.Button(root, command=swaptext)
my_button.pack()

root.mainloop()









############
class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        # function to add data to the treeview.

        q = tk.StringVar()
        namet1=tk.StringVar()
        emailt2=tk.StringVar()
        phonet3=tk.StringVar()
        locationt4=tk.StringVar()
        issuet5=tk.StringVar()

        def update(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end', values=i)
        '''def view_alldetails():
            query = "SELECT name,email,phonenumber,issue,location FROM details_table"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            update(rows)'''

        def search():
            q2=q.get()
            query = "SELECT name,email,phonenumber,issue,location FROM details_table WHERE name Like'%" + q2 + "%' "
            mycursor.execute(query)
            rows = mycursor.fetchall()
            update(rows)
        def clear():
            ent1.delete(0,END)
            ent2.delete(0,END)

        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            # grabbing all items and setting them t's
            namet1.set(item['values'][0])

            emailt2.set(item['values'][1])
            phonet3.set(item['values'][2])
            issuet5.set(item['values'][3])
            locationt4.set(item['values'][4])



        def update_details():
            name = namet1.get()
            email = emailt2.get()
            phone = phonet3.get()
            issue = issuet5.get()
            location=locationt4.get()
            if messagebox.askyesno("Confirm Please ", 'Are you sure you want to Update'):
                query = "UPDATE details_table SET name=%s,email=%s,issue=%s,phonenumber=%s,location=%s WHERE email=%s"
                mycursor.execute(query, (name, email, phone, issue, location,))
                mysqldb.commit()

            else:
                return True
        def add_new():
            name_add=namet1.get()
            email_add=emailt2.get()
            phone_add=phonet3.get()
            location_add=locationt4.get()
            issue_add=issuet5.get()
            self.val_add = (name_add, email_add, phone_add, location_add, issue_add, name_add,)
            mysqldb = mysql.connector.connect(host='localhost', database='basecare_db', user='root', password="")
            mycursor = mysqldb.cursor()
            if name_add != "" and email_add != "" and issue_add != "" and phone_add != "" and location_add != "":
                sql = "INSERT INTO  details_table (name,email,issue,phonenumber,location) values (%s, %s, %s, %s,%s)"
                val = (name_add, email_add, issue_add, phone_add, location_add)
                if '@' not in email_add and '.com' not in email_add:
                    messagebox.showwarning("warning ", "enter valid Email  address")

                else:
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    clear()

                    messagebox.showinfo("information", "Employee inserted successfully...")

                    # mysqldb.rollback()
                    mysqldb.close()
            else:
                messagebox.showwarning("Error Warning", "Fill in the blank entries")





        def delete_details():
            email = emailt2.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete from this customer"):
                query = "DELETE FROM details_table WHERE email=" + email
                mycursor.execute(query)
                mysqldb.commit()
                clear()
            else:
                return True
        def edit(event):
            select_item=trv.focus()
            itemdetails=trv.item(select_item)
            #ent1.insert(0,itemdetails)
            print(itemdetails)





        self.configure(bg="blue")
        self.textlabel = tk.Label(self, text="ADMINISTRATION PAGE", font=("Script MT Bold", 30, 'bold'), bg='blue')
        self.textlabel.place(x=400, y=6)
        trv = ttk.Treeview()

        trv = ttk.Treeview(self, columns=(1, 2, 3, 4, 5), show="headings", height="10")
        trv.place(x=0, y=100)

        trv.heading(1, text="Name")
        trv.heading(2, text="Email")
        trv.heading(3, text="phone Number")
        trv.heading(4, text="Location")
        trv.heading(5, text='Issue')


        #trv.bind('<Double 1>', getrow)
        trv.bind('<Double 1>',getrow)
        #trv.bind('<<TreeviewSelect>>',edit)
        # querying

        query = "SELECT name,email,phonenumber,issue,location from details_table"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

        # comments

        trv = ttk.Treeview(self, columns=(1, 2), show="headings", height="10")
        trv.place(x=1050, y=100)

        trv.heading(1, text="Email")
        trv.heading(2, text="Comment")



        #search sections
        lbl = Label(self, text='search')
        lbl.place(x=900, y=50)
        ent = Entry(self, textvariable=q)
        ent.place(x=970, y=50)
        btn = tk.Button(self, text="search", command=search)
        btn.place(x=1100, y=50)
        cbtn = tk.Button(self, text="Clear", command=clear)
        cbtn.place(x=1200, y=50)



        wrapper1 = LabelFrame(self, text="Acrions")
        wrapper1.pack(fill="both", expand='yes', padx=0, pady=400,ipady=50)

        #update entries
        lbl1 = Label(wrapper1, text="Name")
        lbl1.grid(row=0, column=0, padx=5, pady=3)
        ent1 = Entry(wrapper1, textvariable=namet1)
        ent1.grid(row=0, column=1, padx=5, pady=3,ipadx=30)

        lbl2 = Label(wrapper1, text="Email")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = Entry(wrapper1, textvariable=emailt2)
        ent2.grid(row=1, column=1, padx=5, pady=3,ipadx=30)

        lbl3 = Label(wrapper1, text="Phone Number")
        lbl3.grid(row=0, column=2, padx=5, pady=3)
        ent3 = Entry(wrapper1, textvariable=phonet3)
        ent3.grid(row=0, column=3, padx=5, pady=3,ipadx=30)

        lbl4 = Label(wrapper1, text="Location")
        lbl4.grid(row=1, column=2, padx=5, pady=3)
        ent4 = Entry(wrapper1, textvariable=locationt4)
        ent4.grid(row=1, column=3, padx=5, pady=3,ipadx=30)

        lbl5 = Label(wrapper1, text="Issue")
        lbl5.grid(row=0, column=4, padx=5, pady=3)
        ent5 = Entry(wrapper1, textvariable=issuet5)
        ent5.grid(row=0, column=5, padx=5, pady=3,ipadx=30)

        #buttons in use
        update_btn = tk.Button(self, text="Update", command=update_details)
        update_btn.place(x=5,y=600,width=100)
        add_btn = tk.Button(self, text="Add New", command=add_new)
        add_btn.place(x=100,y=600,width=100)
        delete_btn = tk.Button(self, text="Delete", command=delete_details)
        delete_btn.place(x=200,y=600,width=100)
        edit_btn = tk.Button(self, text="Edit", command=edit)
        edit_btn.place(x=300, y=600, width=100)



        ################


        Button = tk.Button(self, text="Third Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=50)  # x=100, y=450
        Button = tk.Button(self, text="Second Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=120, y=50)
        Button = tk.Button(self, text="Third Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage))
        Button = tk.Button(self, text="Fourth Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FouthPage))
        Button.place(x=240, y=50)
        Button = tk.Button(self, text="Admin Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(AdminPage))
        Button.place(x=365, y=50)
        Button = tk.Button(self, text="login Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=480, y=50)







