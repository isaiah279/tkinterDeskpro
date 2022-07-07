from tkinter import *
import  tkinter

window = Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')


# page to be show when launched

def show_frame(frame):
    frame.tkraise()
show_frame(page1)


#######page log in form############


page1_labe = Label(page1, text='UserName', font=('Arial', 15, 'bold'))
page1_labe.place(x=50, y=100)
page1_entry = Entry(page1)
page1_entry.place(x=170, y=106)

window.mainloop()
