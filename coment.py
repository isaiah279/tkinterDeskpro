from tkinter import ttk
from tkinter import *
import tkinter  as tk
from tkinter import messagebox

root = Tk()


root.title("commenting")
na=Label(text="The commenting page of the System",font=('Helvetica',26,'bold'))
na.pack(pady=20)
wrapper1 = LabelFrame(root, text="Comments",fg="red")
wrapper2 = LabelFrame(root, text="Comments",fg="red")


wrapper1.pack(fill="both", expand="true", padx=40, pady=70)
wrapper2.pack(fill="both", expand="true", padx=40, pady=10,ipady=20)
lcoment = Label(wrapper1, text=" Actions")
textarea = tk.Text(wrapper1, width=30, height=8,font=20,fg="green")
textarea.pack(ipady=50,ipadx=200,anchor=SW)




lcoment.place()
root.mainloop()
