from tkinter import *
from socket import timeout
import tkinter as tk
import time
import subprocess
import sys
from trackPerson import EuclideanDistTracker
import warnings
warnings.filterwarnings('ignore')
import tkinter as tk, tkinter.font
import PIL.Image
from pymongo import MongoClient
from sqlalchemy import create_engine
import numpy as np
import datetime as dt
from turtle import bgcolor, color
from io import StringIO
import pandas
import matplotlib.pyplot as plt
import gridfs
from tkinter.font import Font
from tkinter import PhotoImage, Tk
from turtle import bgpic
import pymongo
from pymongo import MongoClient
import os
import cv2
from itertools import combinations
from datetime import datetime
from PIL import ImageTk, Image


date = dt.datetime.now()

cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
# engine = create_engine("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Users"]
collection_name = db["Username"]
collection_pass = db["Password"]
dbb = cluster["Reports"]
collection_name1 = dbb["Violators"]

tracker = EuclideanDistTracker()
wht = 1000
confThreshold = 0.3
nmsThreshold = 0.3

db = cluster["camera"]
dbb = db["images"]

fs = gridfs.GridFS(db)
file = "C:/Users/Client/OneDrive/Documents/Python projects/New folder/Capture/"

classesFile = 'coco.names'
className = []
with open(classesFile, 'rt') as f:
    className = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')  
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)    
classes = []
with open('coco.names','r') as f:
    classes =f.read().splitlines()
print(classes)
cap = cv2.VideoCapture('sample footage/CULTURAL COC.mp4')
output_layers = net.getUnconnectedOutLayersNames()
print(output_layers)

# fs = gridfs.GridFS(db)
# gridfs.GridFS.find_one
# file = fs.get({'filename': "file"})
# fs.get(file).read()

def delete2():
      screen3.destroy()

def delete3():
      screen4.destroy()

def delete4():
      screen5.destroy()


# def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

def nextpage():
    window.withdraw()
    screen3.destroy()
    file = tk.Toplevel()
    file.geometry("800x604")
    file.config(bg="#071D20")
    Dashboard(file)
    file.mainloop()
    
    # nextpage(['python', 'home.py']) 

# def campage():
#     dzuh = Toplevel(file)
#     dzuh.destroy()
#     import Camera

def login_sucess():
    global screen3
    screen3 = Toplevel(window)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Sucess").pack()
    Button(screen3, text = "OK", command=nextpage).pack()
    
def password_not_recognised():
      global screen4
      screen4 = Toplevel(window)
      screen4.title("Success")
      screen4.geometry("150x100")
      Label(screen4, text = "Password Error").pack()
      Button(screen4, text = "OK", command=delete3).pack()

def user_not_found():
      global screen5
      screen5 = Toplevel(window)
      screen5.title("Success")
      screen5.geometry("150x100")
      Label(screen5, text = "User Not Found").pack()
      Button(screen5, text = "OK", command =delete4).pack()      

def login_verify():
            username1 = username_verify.get()
            password1 = password_verify.get()
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            forname = {"username": username1}
            forpass = {"password": password1}
            result1 = collection_name.find_one(forname)
            result2 = collection_pass.find_one(forpass)

            if result1:

              if result2:
                True
                login_sucess()
                
              else:
                password_not_recognised()

            else:
                user_not_found()
                    
def register_user():

  # for x in results:
  #   print(results["name"])
    username_info = username_entry1.get()
    password_info = password_entry1.get()

    forname = {"username": username_info}
    forpass = {"password": password_info}
    collection_name.insert_one(forname)
    collection_pass.insert_one(forpass)
    # collection.insert_one({"username":forname, "password":forpass})
    # file=open(username_info+".txt", "w")
    # file.write(username_info+"\n")
    # file.write(password_info)
    # file.close()

    username_verify.delete(0, END)
    password_verify.delete(0, END)

class LoginFile:

    def __init__(self, window):
        self.window = window
        self.window_width = 1166
        self.window_height = 718
        window.geometry(f'{self.window_width}x{self.window_height}+{100}+{30}')
        # self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        
        global username_entry1
        global password_entry1
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()

        #==========Background Image===========
        self.bg = Image.open('assets/bg/loginbg.png')
        photo = ImageTk.PhotoImage(self.bg)
        self.bgpan = Label(self.window, image=photo)
        self.bgpan.image = photo
        self.bgpan.pack(fill='both', expand='yes')

        self.loginbg = Image.open('assets/bg/login_bg.png')
        photo = ImageTk.PhotoImage(self.loginbg)
        self.loginframe = Label(self.window, image=photo, bg='#FFFFFF', width=950, height=600, borderwidth=0)
        self.loginframe.image = photo
        self.loginframe.place(x=200, y=70)

        # self.txt = 'WELCOME'
        # self.heading =  Label(self.loginframe, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#FFFFFF', fg='black')
        # self.heading.place(x=80, y=30, width=300, height=30)

        # self.CC = Image.open('assets/bg/COUNTME.png')
        # photo = ImageTk.PhotoImage(self.CC) 
        # self.CC_label = Label(self.loginframe, image=photo, bg='white')
        # self.CC_label.image = photo
        # self.CC_label.place(x=80, y=180)

        self.Logo = Image.open('assets/icons/CC.png')
        photo = ImageTk.PhotoImage(self.Logo)
        self.Logo_label = Label(self.loginframe, image=photo, bg='white')
        self.Logo_label.image = photo
        self.Logo_label.place(x=515, y=50)

        self.signin_label = Label(self.loginframe, text="Sign In", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        self.signin_label.place(x=688, y=190)


        #=============USERNAME==================
        username_icon = Image.open('assets/icons/user.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label= Label(self.loginframe, image=photo, bg='white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=287)

        username_entry = Label(self.loginframe, text="Username", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        username_entry.place(x=550, y=240)
        username_entry1 = Entry(self.loginframe,  textvariable=username_verify,highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'))
        username_entry1.place(x=595, y=285, width=220)
        username_line = Canvas(self.loginframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
        username_line.place(x=580, y=309)

        #================PASSWORD===============================
        password_icon = Image.open('assets/icons/key.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label= Label(self.loginframe, image=photo, bg='white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=387)

        password_entry = Label(self.loginframe, text="Password", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        password_entry.place(x=550, y=340)
        password_entry1 = Entry(self.loginframe, textvariable=password_verify, highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'), show='*')
        password_entry1.place(x=595, y=385, width=320)
        self.password_line = Canvas(self.loginframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
        self.password_line.place(x=580, y=409)

        #=====================LOGIN BUTTON ===============================
        login_btn = Image.open('assets/placeholder/menu.png')
        photo = ImageTk.PhotoImage(login_btn)
        login_label= Label(self.loginframe, image=photo, bg='white')
        login_label.image = photo
        login_label.place(x=575, y=450)
        entry_button = Button(login_label, text='LOGIN', font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=login_verify)
        entry_button.place(x=40, y=10)

        #======================REGISTER LOINK================
        register = Label(self.loginframe, text="No Account?", bg='white', fg='black', font=('yu gothic ui', 13, 'bold'))
        register.place(x=570, y=533)
        register_btn = Image.open('assets/placeholder/menu1.png')
        photo = ImageTk.PhotoImage(register_btn)
        register_label= Label(self.loginframe, image=photo, bg='white')
        register_label.image = photo
        register_label.place(x=675, y=530)
        register_button = Button(register_label, text='Register', font=('yu gothic ui', 10, 'bold'), width=10, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=regform)
        register_button.place(x=55, y=3)

        #===========================SHOW PASS=====================
        show_btn = Image.open('assets/icons/eye.png')
        photo = ImageTk.PhotoImage(show_btn)
        show_label= Button(self.loginframe, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=self.show)
        show_label.image = photo
        show_label.place(x=855, y=382)

        
    def show(self):
        self.show_btn1 = Image.open('assets/icons/eye.png')
        self.photo = ImageTk.PhotoImage(self.show_btn1)
        self.show_btn1 =  Button(self.loginframe, image=self.photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=self.show2)
        self.show_btn1.place(x=855, y=382)
        password_entry1.config(show='')
    
    def show2(self):
        self.show_btn2 = Image.open('assets/icons/eye2.png')
        self.photo = ImageTk.PhotoImage(self.show_btn2)
        self.show_btn2 =  Button(self.loginframe, image=self.photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=self.show)
        self.show_btn2.place(x=855, y=382)
        password_entry1.config(show='*')




def regform():
    window.geometry('1166x718')
    window.state('zoomed')
    window.resizable(0, 0)

    global username
    global password    
    global username_entry1
    global password_entry1
    global username_verify
    global password_verify
    username_entry1 = StringVar()
    password_entry1 = StringVar()

        #==========Background Image===========
    bg = Image.open('assets/bg/loginbg.png')
    photo = ImageTk.PhotoImage(bg)
    bgpan = Label(window, image=photo)
    bgpan.image = photo
    bgpan.pack(fill='both', expand='yes')

    # regframe = Frame(window, bg='#FFFFFF', width=950, height=600, borderwidth=0)
    # regframe.pack()

    CC = Image.open('assets/bg/login_bg.png')
    photo = ImageTk.PhotoImage(CC) 
    regframe = Label(window, image=photo, bg='#FFFFFF', width=950, height=600, borderwidth=0)
    regframe.image = photo
    regframe.place(x=200, y=70)

    Logo = Image.open('assets/icons/CC.png')
    photo = ImageTk.PhotoImage(Logo)
    Logo_label = Label(regframe, image=photo, bg='white')
    Logo_label.image = photo
    Logo_label.place(x=515, y=50)

    signin_label = Label(regframe, text="Sign Un", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    signin_label.place(x=688, y=190)

    username_icon = Image.open('assets/icons/user.png')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label= Label(regframe, image=photo, bg='white')
    username_icon_label.image = photo
    username_icon_label.place(x=550, y=287)

    username_entry = Label(regframe, text="Username", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    username_entry.place(x=550, y=240)
    username_entry1 = Entry(regframe,  textvariable=username_entry1,highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'))
    username_entry1.place(x=595, y=285, width=220)
    username_line = Canvas(regframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
    username_line.place(x=580, y=309)

    password_icon = Image.open('assets/icons/key.png')
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label= Label(regframe, image=photo, bg='white')
    password_icon_label.image = photo
    password_icon_label.place(x=550, y=387)

    password_entry = Label(regframe, text="Password", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    password_entry.place(x=550, y=340)
    password_entry1 = Entry(regframe, textvariable=password_entry1, highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'), show='*')
    password_entry1.place(x=595, y=385, width=320)
    password_line = Canvas(regframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
    password_line.place(x=580, y=409)

    reg_btn = Image.open('assets/placeholder/menu.png')
    photo = ImageTk.PhotoImage(reg_btn)
    reg_label= Label(regframe, image=photo, bg='white')
    reg_label.image = photo
    reg_label.place(x=575, y=450)
    entry_button = Button(reg_label, text='REGISTER', font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=register_user)
    entry_button.place(x=40, y=10)
    
    #===========================SHOW PASS=====================
    
    def show2():
            show_btn2 = Image.open('assets/icons/eye2.png')
            photo = ImageTk.PhotoImage(show_btn2)
            show_btn2 =  Button(regframe, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show)
            show_btn2.place(x=855, y=382)
            password_entry1.config(show='*') 
    def show():
            show_btn1 = Image.open('assets/icons/eye.png')
            photo = ImageTk.PhotoImage(show_btn1)
            show_btn1 =  Button(regframe, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show2)
            show_btn1.place(x=855, y=382)
            password_entry1.config(show='')
            
    show_btn = Image.open('assets/icons/eye2.png')
    photo = ImageTk.PhotoImage(show_btn)
    show_label= Button(regframe, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show)
    show_label.image = photo
    show_label.place(x=855, y=382)        

def page():
    global window
    global file
    window = tk.Tk()
    window.geometry("800x604")
    window.config(bg="#071D20")
    LoginFile(window)
    window.mainloop()



class Dashboard:
    def __init__(self, file):
        
        self.file = file
        
        self.file_width = 1040
        self.file_height = 640
        self.file.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
        self.file.config(background="#B0AEAE")
        self.file.resizable(0,0)

        self.icon = PhotoImage(file='assets/icons/CC2.png')
        self.file.iconphoto(True, self.icon)

        #===========HEADER==========
        self.header = Frame(self.file, bg='#015C5A')
        self.header.place(x=277, y=0, width=1070, height=60)
        self.intro = Label(self.header,
            text=f'TODAY is {date:%A, %B %d, %Y}', bg="#015C5A", font=("", 14, "bold"), fg='white')
        self.intro.place(x=50, y=10)

        #==========LOGOUT BUTTON ====================
        self.logout_text = Button(self.file, text='Logout', bg='#FFFFFF', font=("", 13, "bold"), fg='black', cursor='hand2', activebackground='#015C5A')
        self.logout_text.place(x=950, y=15)

        #=========NAVBAR===============
        self.sidebar = Frame(self.file, bg="#FFFFFF")
        self.sidebar.place(x=0, y=0, width=275, height=750)

        #=======NAVBAR LOGO===========
        self.logo = Image.open('assets/icons/TEXT.png')
        self.photo = ImageTk.PhotoImage(self.logo)
        self.logo = Label(self.sidebar, image=self.photo, bg="#FFFFFF")
        self.logo.image = self.photo
        self.logo.place(x=10, y=50)

        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        #=========CONTENTS =============
        self.heading = Label(self.file, text='Dashboard', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        self.heading.place(x=325, y=70)

        self.logo_dash = Image.open('assets/icons/pps.png')
        self.photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=self.photo, bg="#FFFFFF")
        self.logo_dash.image = self.photo
        self.logo_dash.place(x=35, y=255)

        self.dash_text = Label(self.sidebar, text='Dashboard', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/camera.png')
        self.photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=self.photo, bg="#FFFFFF")
        self.logo_cam.image = self.photo
        self.logo_cam.place(x=35, y=310)

        self.cam_text = Button(self.sidebar, text='Camera', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.cam_text.place(x=75, y=315)

        self.logo_notif = Image.open('assets/icons/ss.png')
        self.photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=self.photo, bg="#FFFFFF")
        self.logo_notif.image = self.photo
        self.logo_notif.place(x=35, y=365)

        self.notif_text = Button(self.sidebar, text='Notification', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.notif_text.place(x=75, y=368)

        self.logo_data = Image.open('assets/icons/dd.png')
        self.photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=self.photo, bg="#FFFFFF")
        self.logo_data.image = self.photo
        self.logo_data.place(x=35, y=415)

        self.data_text = Button(self.sidebar, text='Database', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.data_text.place(x=75, y=418)



        #========FOR TABLES==============
        self.bodyframe1 = Frame(self.file, bg="#FFFFFF")
        self.bodyframe1.place(x=328, y=110, width=1040, height=290)
        # photo = ImageTk.PhotoImage(file)
        # self.imageframe = Frame(self.bodyframe1, image=photo)

        
        # df = pandas.read_sql("SELECT borough, cuisine FROM restaurants WHERE Name = 'Morris Park Bake Shop'", engine)
        
        # df.plot(kind="bar", x="borough", y="cuisine")
        # plt.show()

        #=========REPORTS================
        self.bodyframe2 = Frame(self.file, bg="#FFFFFF")
        self.bodyframe2.place(x=380, y=435, width=269, height=180)

        self.bodyframe3 = Frame(self.file, bg="#FFFFFF")
        self.bodyframe3.place(x=708, y=435, width=269, height=180)

if __name__ == '__main__':
    page()
