from tkinter import *
from  tkinter import  ttk
#defining register function
def register():
    #getting form data
    name1=name.get()
    passwrd=password.get()
    cpasswrd=confirmPassword.get()
    gen1=gender.get()

    #applying empty validation
    if name1=='' or passwrd==''or cpasswrd=='' or gen1=='':
        message.set("fill the empty field!!!")
    else:
        #opening of file to store data
        fileptr = open("StuReg.txt", "a")#here a means append
        if gen1==1:
         fileptr.write("\n"+name1+"  "+passwrd+"  "+cpasswrd)
        else:
         fileptr.write("\n" + name1 + "  " + passwrd + "  " + cpasswrd )


#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global  message;
    global name
    global password
    global confirmPassword
    global gender

    name = StringVar()
    password = StringVar()
    confirmPassword=StringVar()
    gender=IntVar()


    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #name Label
    Label(reg_screen, text="Name * ").place(x=20,y=40)
    #name textbox
    Entry(reg_screen, textvariable=name).place(x=90,y=42)
    #contact Label
    Label(reg_screen, text="Contact * ").place(x=20,y=80)
    #contact textbox
    Entry(reg_screen, textvariable=password).place(x=90, y=82)

    # email Label
    Label(reg_screen, text="Confirm Password * ").place(x=20, y=120)
    # email textbox
    Entry(reg_screen, textvariable=confirmPassword).place(x=90, y=122)


    Button(reg_screen, text="Register", width=10, height=1, bg="orange",command=register).place(x=105,y=300)
    reg_screen.mainloop()
#calling function Registrationform
Registrationform()