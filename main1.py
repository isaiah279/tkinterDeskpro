from tkinter import ttk
from tkinter import *
import tkinter
from tkinter import messagebox

splash_root = Tk()

splash_root.title("Splash screen")

splash_root.geometry("1200x800")

splash_label = Label(splash_root, text="Splaced Screen", font=46)
splash_label.pack(pady=20)


def main_window():
    splash_root.destroy()
    main_window = Tk()
    main_window.geometry("1200x800")

    main_window.title("Desk App")

    def add_information():
        pass

    def delete_information():
        pass

    def cancel_information():
        pass

    # phone, email, name, location, issue
    wrapper1 = LabelFrame(main_window, text="Enter Details")
    wrapper2 = LabelFrame(main_window, text="Actions Required")

    wrapper2.config(bg="green")
    wrapper1.pack(fill="both", expand='yes', padx=40, pady=10)
    wrapper2.pack(fill="both", expand='yes', padx=40, pady=10)

    # actions
    add_btn = Button(wrapper2, text="Add New", command=add_information)
    delete_btn = Button(wrapper2, text="Delete", command=delete_information)
    cancel_btn = Button(wrapper2, text="Cancel", command=cancel_information)

    # labels
    lname = Label(wrapper1, text="Name:")
    lemail = Label(wrapper1, text="Email:")
    lphone = Label(wrapper1, text="Phone:")
    lissue = Label(wrapper1, text="Issue:")
    llocation = Label(wrapper1, text="Location")

    # grids
    lname.grid(row=1, column=0, padx=20, pady=60)
    lemail.grid(row=2, column=0, padx=20)
    lphone.grid(row=1, column=3, padx=20, pady=20)
    llocation.grid(row=2, column=3, padx=20, pady=20)
    lissue.grid(row=3, column=0, padx=20, pady=40)

    ename = Entry(wrapper1)
    eemail = Entry(wrapper1)
    ephone = Entry(wrapper1)
    elocation = Entry(wrapper1)
    eissue = Entry(wrapper1)

    ename.grid(row=1, column=1, ipadx=20, ipady=5)
    eemail.grid(row=2, column=1, ipady=5, ipadx=20)
    ephone.grid(row=1, column=4, ipady=5, ipadx=20)
    eissue.grid(row=2, column=4, ipady=5, ipadx=20)
    elocation.grid(row=3, column=1, ipady=5, ipadx=20)

    add_btn.grid(row=4, column=2, padx=5, pady=3)
    delete_btn.grid(row=4, column=4, padx=5, pady=3)
    cancel_btn.grid(row=4, column=6, padx=5, pady=3)


splash_root.after(3000, main_window)

mainloop()
