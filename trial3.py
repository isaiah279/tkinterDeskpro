from tkinter import *

global app
def save_info():

    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()

    print(firstname_info, lastname_info, age_info)

    file = open("user.txt", "w")

    file.write("Your First Name " + firstname_info)

    file.write("\n")

    file.write("Your Last Name " + lastname_info)

    file.write("\n")

    file.write("Your Age " + str(age_info))

    file.close()

    def   regi():
        app = Tk()

        app.geometry("500x500")

        app.title("Python File Handling in Forms")

        heading = Label(text="Python File Handling in Forms", fg="black", bg="yellow", width="500", height="3", font="10")

        heading.pack()

        firstname_text = Label(text="FirstName :")
        lastname_text = Label(text="LastName :")
        age_text = Label(text="Age :")

        firstname_text.place(x=15, y=70)
        lastname_text.place(x=15, y=140)
        age_text.place(x=15, y=210)

        firstname = StringVar()
        lastname = StringVar()
        age = IntVar()

        first_name_entry = Entry(textvariable=firstname, width="30")
        last_name_entry = Entry(textvariable=lastname, width="30")
        age_entry = Entry(textvariable=age, width="30")

        first_name_entry.place(x=15, y=100)
        last_name_entry.place(x=15, y=180)
        age_entry.place(x=15, y=240)

        button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="grey")

        button.place(x=15, y=290)

        mainloop()
