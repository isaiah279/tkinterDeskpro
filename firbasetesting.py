'''from tkinter import *
from tkinter import messagebox
import pyrebase
import random

root = Tk()
root.geometry('200x200')
#varriables
username = StringVar()
gender=StringVar()
occupation=StringVar()


Config = {
    "apiKey": "AIzaSyDtzBovcSx0DLmrk6yyTrNhUjlWc-quB2I",
    "authDomain": "teamproject-cbe48.firebaseapp.com",
    "databaseURL": "https://teamproject-cbe48-default-rtdb.firebaseio.com",
    "projectId": "teamproject-cbe48",
    "storageBucket": "teamproject-cbe48.appspot.com",
    "messagingSenderId": "1056073545255",
    "appId": "1:1056073545255:web:b95f0707eb5c4dea384002",
    "measurementId": "G-KPB4YGV4MB"
}

firebase = pyrebase.initialize_app(Config)
db = firebase.database()


def submit():
    UserName = username.get()
    Gender=gender.get()
    Occupation=occupation.get()
    try:
        JSON = {"user":f" {UserName}","Gender":f"{Gender}","Occupation":f"{Occupation}"}

        id = random.randint(0, 1000)
        db.child("USER-ID").child(id).set(JSON)

        messagebox.showinfo("Information Submitted", "success")
    except:
        print("names")



lname = Label(root, text="Name")
lgender = Label(root, text="Gender")
locupation = Label(root, text="Occupation")

lname.grid(row=1,column=1,pady=20, padx=50)
lgender.grid(row=2,column=1,pady=20, padx=30)
locupation.grid(row=3,column=1,pady=20, padx=30)

name_entry = Entry(root, textvariable=username)
gender_entry=Entry(root, textvariable=gender)
occupationr_entry=Entry(root, textvariable=occupation)

name_entry.grid(row=1, column=2)
gender_entry.grid(row=2, column=2)
occupationr_entry.grid(row=3, column=2)

sub_btn = Button(root, text='Submit', command=submit)
sub_btn.grid(row=4, column=2)
root.mainloop()
'''
# File Name -- Map.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude,longitude)
print(getLocation())