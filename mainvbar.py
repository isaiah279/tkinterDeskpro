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
file=filedialog.askopenfilename()











