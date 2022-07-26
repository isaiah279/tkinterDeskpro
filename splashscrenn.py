from tkinter import *
from tkinter import messagebox

splash_root = Tk()

splash_root.title("Splash screen")

splash_root.geometry("1200x800")

splash_label = Label(splash_root, text="Splaced Screen", font=46)
splash_label.pack(pady=20)


def main_window():
    splash_root.destroy()
    root = Tk()
    root.title("Mainsceren Splash Screens")
    root.iconbitmap("")
    root.geometry("1200x800")
    mainlabel = Label(root, text="Main Screen In the Column circle ")
    mainlabel.pack(pady=50, padx=30)

    # splashed screen timer


splash_root.after(5000, main_window)

mainloop()
