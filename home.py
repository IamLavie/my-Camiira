from tkinter import *
from socket import timeout
import tkinter as tk
import time
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
db = cluster["Reports"]
collection_name = db["Violators"]
collection = db["Users"]

db = cluster["camera"]
dbb = db["images"]

db = cluster["Reports"]
collection_name = db["Violators"]
# def Camera():
#        .file.destroy()
#         import Camera


class Dashboard:
    def __init__(self, file):

        self.file = file
        self.file_width = 1040
        self.file_height = 640
        self.file.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
        self.file.config(background="#B0AEAE")
        self.file.resizable(0,0)

        # self.icon = PhotoImage(file='assets/icons/CC2.png')
        # self.file.iconphoto(True, self.icon)

        

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
        photo = ImageTk.PhotoImage(self.logo)
        self.logo = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo.image = photo
        self.logo.place(x=10, y=50)

        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        #=========CONTENTS =============
        self.heading = Label(self.file, text='Dashboard', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        self.heading.place(x=325, y=70)

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo_dash.image = photo
        self.logo_dash.place(x=35, y=255)

        self.dash_text = Label(self.sidebar, text='Dashboard', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo_cam.image = photo
        self.logo_cam.place(x=35, y=310)

        self.cam_text = Button(self.sidebar, text='Camera', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.cam_text.place(x=75, y=315)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo_notif.image = photo
        self.logo_notif.place(x=35, y=365)

        self.notif_text = Button(self.sidebar, text='Notification', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        self.notif_text.place(x=75, y=368)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo_data.image = photo
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


def win():
    global file
    file = Tk()
    file.geometry("800x604")
    file.config(bg="#071D20")
    Dashboard(file)    
    file.mainloop()

if __name__ == '__main__':
    win()
