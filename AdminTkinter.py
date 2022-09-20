from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView


class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="tomato")
        def submit(self):
            pass
        bordering = tk.LabelFrame(self, text="Login", font=("Arial Bold", 20), bd=1, bg="Blue", fg="orange")
        bordering.pack(fill="both", expand='yes', padx=150, pady=150)

        L1 = tk.Label(bordering, text="User name", font=("Arial Bold", 15))
        L1.place(x=50, y=20)

        T1 = tk.Entry(bordering, width=30, bd=0)
        T1.place(x=180, y=20)

        L2 = tk.Label(bordering, text="Password", font=("Arial Bold", 15))
        L2.place(x=50, y=80)

        T2 = tk.Entry(bordering, width=30, bd=0, show="*")
        T2.place(x=180, y=80)

        def verify():
            try:
                if T1.get() == "" and T2.get() == "":
                    controller.show_frame(SecondPage)
                else:
                    messagebox.showinfo("Error", "provide correct details")


            except:
                messagebox.showinfo("Error ", "please provide correct user name")

        login_btn = tk.Button(bordering, text="Login", font=("Arial", 15), command=verify)
        login_btn.place(x=180, y=130)

        # register button


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        self.configure(bg="deep sky blue")
        welcomelabel = tk.Label(self, text="View the Registered users  ", font=70, bg='deep sky blue')
        welcomelabel.place(x=2, y=70)

        Button = tk.Button(self, text="Home", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=5, y=15)
        Button = tk.Button(self, text="FirstPage", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=80, y=15)
        Button = tk.Button(self, text="Navigate", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=190, y=15)

        Button = tk.Button(self, text="FouthPage", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame())
        Button.place(x=295 - 10, y=15)  # x=100, y=450

        Button = tk.Button(self, text="Find Location", font=("Arial", 15), bg='blue',
                           command=lambda: controller.show_frame(FindLocation))
        Button.place(x=295 + 80, y=15)  # x=100, y=450

        finder = tk.Label(self, text="Third Page")
        finder.place(x=1250, y=0)


class FouthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        self.configure(bg="blue")

        def add_information():
            pass

        def clear_information():
            pass

        def cancel_information():
            pass

        # phone, email, name, location, issue
        wrapper1 = tk.LabelFrame(self, text="Enter Details", bg="blue")
        wrapper2 = tk.LabelFrame(self, text="Actions Required")

        wrapper2.config(bg="green")
        wrapper1.pack(fill="both", expand='yes', pady=50)

        # actions
        add_btn = tk.Button(wrapper1, text="Submit Request", command=add_information)
        delete_btn = tk.Button(wrapper1, text="Clear", command=clear_information)
        cancel_btn = tk.Button(wrapper1, text="Cancel", command=cancel_information)

        add_btn.grid(row=4, column=1, pady=40, ipadx=20)
        delete_btn.grid(row=4, column=2, pady=40, ipadx=20)
        cancel_btn.grid(row=4, column=3, pady=40, ipadx=20, padx=5)

        Button = tk.Button(self, text="Third Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=5)  # x=100, y=450
        Button = tk.Button(self, text="Third Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=120, y=5)

        Button = tk.Button(self, text="Third Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=240, y=5)

        Button = tk.Button(self, text="Admin Page", font=("Arial", 15), bg="dark blue",
                           command=lambda: controller.show_frame(AdminPage))
        Button.place(x=360, y=5)

        finder = tk.Label(self, text="Fouth Page")
        finder.place(x=1250, y=0)


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments()
        Button = tk.Button(self, text="Second page", font=("Arial", 15),
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=0, y=0)
        self.configure(bg="blue")
        self.textlabel = tk.Label(self, text="Administration page", font=("arial", 30, 'bold'), bg='blue')
        self.textlabel.place(x=400, y=10)


class FindLocation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        self.configure(bg="blue")

        def add_information():
            pass
        self.locatevar=tk.StringVar()
        def find_location(self,location):
            location=locationEntry.get()

            map_widget = TkinterMapView(self, width=600, height=400, corner_radius=0)
            map_widget.pack(fill="both", expand=True)

            # google normal tile server
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

            map_widget.set_address(self, marker=True)
            find_location(map_widget)

        pagetitle = tk.Label(self, text="Location", font=40, bg='blue')
        pagetitle.grid(row=0, column=5, padx=200, pady=20)
        locatelabel = tk.Label(self, text="Paste Location Url:", bg='blue', font=18)
        locatelabel.place(x=300,y=200)

        locationEntry = tk.Entry(self, width=30,textvariable=self.locatevar)
        locationEntry.place(x=500,y=200,height=30,width=300)
        locate_btn = tk.Button(text="Find Location", bg='orange', command=find_location)
        locate_btn.place(x=520, y=360, width=150)

        finder = tk.Label(self, text="Location Page")
        finder.place(x=1250, y=0)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=750)
        window.grid_columnconfigure(0, minsize=1365)

        self.frames = {}
        for F in (FindLocation, FirstPage, SecondPage, FouthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(FindLocation)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()

app.mainloop()
