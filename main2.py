from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


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
            """if T1.get() == 'isaiah' and T2.get() == "12345":
                controller.show_frame(SecondPage)
            else:
                messagebox.showinfo("Error", "provide correct details")
            """
            try:
                with open("credential.txt", "r") as f:
                    info = f.readline()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u == T1.get() and p == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                        break
                    if i == 0:
                        messagebox.showinfo("Error ", "please provide correct user name")
            except:
                messagebox.showinfo("Error ", "please provide correct user name")

        login_btn = tk.Button(bordering, text="Login", font=("Arial", 15), command=verify)
        login_btn.place(x=180, y=130)

        # register button

        def register():
            window = tk.Tk()
            window.title("Register")
            window.configure(bg="deep sky blue")
            window.resizable(0, 0)

            username_label = tk.Label(window, text="Username", font=("Arial", 15),bg="blue")
            username_label.place(x=10, y=10,ipadx=30,ipady=10)
            username_ent = tk.Entry(window, width=30, bd=0,ipady=100)
            username_ent.place(x=200, y=10,ipady=100)

            password_label = tk.Label(window, text="Password", font=("Arial", 15))
            password_label.place(x=10, y=50)
            password_ent = tk.Entry(window, text="Password", width=30, show="*")
            password_ent.place(x=200, y=50)
            password_conf_label = tk.Label(window, text="Confirm Password", font=("Arial", 15))
            password_conf_label.place(x=10, y=100)
            password_conf_ent = tk.Entry(window, width=30, show="*")
            password_conf_ent.place(x=200, y=110)

            def check():
                if username_ent.get() != "" or password_ent.get() != "" or password_conf_ent.get() != "":
                    if password_ent.get() == password_conf_ent.get():
                        with open("credential.txt", "a") as f:
                            f.write(username_ent.get() + "," + password_ent.get() + "\n")
                            messagebox.showinfo("welcome", "You are registered successfully")
                    else:
                        messagebox.showinfo("Error ", "Your password didn't get match!")
                else:
                    messagebox.showinfo("Error ", "please complete your fild")

            b1 = tk.Button(window, text="Sign up ", bg="orange", command=check)
            b1.place(x=250, y=150)

            window.geometry("470x220")

        register_btn = tk.Button(bordering, text="Register", font=("Arial", 15), bg="orange", command=register)
        register_btn.place(x=300, y=130)

        Next_btn = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Next_btn.place(x=750, y=0)
        finder = tk.Label(self, text="First Page")
        finder.place(x=1250, y=0)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        L2 = tk.Label(self, text="my Second Page", font=("Arial Bold", 30))
        L2.grid(row=2, column=3)  # x=200, y=230

        Button = tk.Button(self, text="First Page", font=("Arial", 15),
                           command=lambda: controller.show_frame(FirstPage))
        Button.grid(row=5, column=5)  # x=100, y=450

        Button = tk.Button(self, text="Third Page", font=("Arial", 15),
                           command=lambda: controller.show_frame(ThirdPage))
        Button.grid(row=5, column=8)
        Button = tk.Button(self, text="Administrator", font=("Arial", 15),
                           command=lambda: controller.show_frame(AdminPage))
        Button.grid(row=5, column=8)
        Button = tk.Button(self, text="Fouth Page", font=("Arial", 15),
                           command=lambda: controller.show_frame(FouthPage))
        Button.grid(row=5, column=20)
        finder = tk.Label(self, text="Second Page")
        finder.place(x=1250, y=0)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        self.configure(bg="deep sky blue")

        na = tk.Label(text="The commenting page of the System", font=('Helvetica', 26, 'bold'))
        na.pack(pady=20)
        wrapper1 = tk.LabelFrame(self, text="Write Comment", fg="White",bg="dark blue",font=('Arial',14),border=10)
        wrapper1.pack(fill="both", expand="true", padx=0, pady=80,ipady=2)
        textarea = tk.Text(wrapper1, width=25, height=15, font=20, fg="green")
        textarea.pack(ipady=50, ipadx=200, anchor='center', pady=20)

        #action buttons
        send_btn=tk.Button(wrapper1,text="send Comment")
        send_btn.place(x=350,y=450)
        clear_btn = tk.Button(wrapper1, text="Clear Comment")
        clear_btn.place(x=500,y=450)
        clear_btn = tk.Button(wrapper1, text="Exit page")
        clear_btn.place(x=650, y=450)

        Button = tk.Button(self, text="Home", font=("Arial", 15),bg='blue', command=lambda: controller.show_frame(FirstPage))
        Button.place(x=5, y=15)
        Button = tk.Button(self, text="FirstPage", font=("Arial", 15),bg='blue',  command=lambda: controller.show_frame(FirstPage))
        Button.place(x=80, y=15)
        Button = tk.Button(self, text="Navigate", font=("Arial", 15),bg='blue',  command=lambda: controller.show_frame(SecondPage))
        Button.place(x=190, y=15)

        Button = tk.Button(self, text="FouthPage", font=("Arial", 15),bg='blue',  command=lambda: controller.show_frame(FouthPage))
        Button.place(x=295, y=15)  # x=100, y=450


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

        # labels
        lname = tk.Label(wrapper1, text="Name:",bg='blue')
        lemail = tk.Label(wrapper1, text="Email:",bg='blue')
        lphone = tk.Label(wrapper1, text="Phone:",bg='blue')
        lissue = tk.Label(wrapper1, text="Issue:",bg='blue')
        llocation = tk.Label(wrapper1, text="Location",bg='blue')

        # grids
        lname.grid(row=1, column=0, padx=20, pady=60)
        lemail.grid(row=2, column=0, padx=20)
        lphone.grid(row=1, column=3, padx=20, pady=20)
        llocation.grid(row=2, column=3, padx=20, pady=20)
        lissue.grid(row=3, column=0, padx=20, pady=40)

        ename = tk.Entry(wrapper1)
        eemail = tk.Entry(wrapper1)
        ephone = tk.Entry(wrapper1)
        elocation = tk.Entry(wrapper1)
        eissue = tk.Entry(wrapper1)

        ename.grid(row=1, column=1, ipady=5, ipadx=60)
        eemail.grid(row=2, column=1, ipady=5, ipadx=60)
        ephone.grid(row=1, column=4, ipady=5, ipadx=60)
        eissue.grid(row=2, column=4, ipady=5, ipadx=60)
        elocation.grid(row=3, column=1, ipady=5, ipadx=60)

        add_btn.grid(row=4, column=1,pady=40,ipadx=20)
        delete_btn.grid(row=4, column=2,pady=40,ipadx=20)
        cancel_btn.grid(row=4, column=3,pady=40,ipadx=20,padx=5)

        Button = tk.Button(self, text="Third Page", font=("Arial", 15),bg="dark blue",command=lambda: controller.show_frame(FirstPage))
        Button.place(x=0, y=5)  # x=100, y=450
        Button = tk.Button(self, text="Third Page", font=("Arial", 15),bg="dark blue", command=lambda: controller.show_frame(SecondPage))
        Button.place(x=120, y=5)
        Button = tk.Button(self, text="Third Page", font=("Arial", 15),bg="dark blue",  command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=240, y=5)
        Button = tk.Button(self, text="Admin Page", font=("Arial", 15),bg="dark blue", command=lambda: controller.show_frame(AdminPage))
        Button.place(x=360, y=5)


        finder = tk.Label(self, text="Fouth Page")
        finder.place(x=1250, y=0)


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def comments():
        Button = tk.Button(self, text="Second page", font=("Arial", 15),
                           command=lambda: controller.show_frame(SecondPage))
        Button.place(x=0, y=0)
        self.configure(bg="blue")
        self.textlabel = tk.Label(self, text="Administration page", font=("arial", 30, 'bold'), bg='blue')
        self.textlabel.place(x=400, y=10)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=750)
        window.grid_columnconfigure(0, minsize=1365)

        self.frames = {}
        for F in ( ThirdPage,FouthPage,AdminPage, SecondPage, ThirdPage, FirstPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame( ThirdPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()

app.mainloop()
