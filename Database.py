from tkinter import *
from socket import timeout
import tkinter as tk
from tkinter import messagebox
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

class Database:
    def __init__(self, records):

        self.records = records
        self.file_width = 1040
        self.file_height = 640
        records.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
        self.records.config(background="#B0AEAE")
        self.records.resizable(0,0)

        self.icon = PhotoImage(file='assets/icons/CC2.png')
        self.records.iconphoto(True, self.icon)

        

        #===========HEADER==========
        self.header = Frame(self.records, bg='#015C5A')
        self.header.place(x=277, y=0, width=1070, height=60)
        self.intro = Label(self.header,
            text=f'TODAY is {date:%A, %B %d, %Y}', bg="#015C5A", font=("", 14, "bold"), fg='white')
        self.intro.place(x=50, y=10)

        #==========LOGOUT BUTTON ====================
        self.logout_text = Button(self.records, text='Logout', bg='#FFFFFF', font=("", 13, "bold"), fg='black', cursor='hand2', activebackground='#015C5A')
        self.logout_text.place(x=950, y=15)

        #=========NAVBAR===============
        self.sidebar = Frame(self.records, bg="#FFFFFF")
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
        self.heading = Label(self.records, text='Dashboard', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
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
        self.bodyframe1 = Frame(self.records, bg="#FFFFFF")
        
        self.bodyframe1.place(x=328, y=110, width=1040, height=590)

        serts = StringVar()

        def sertz():
            
            datee = self.search.get()
            forname = {"Date": datee}
            collection_name.find_one(forname)
            fornana = collection_name.find({'Persons'})
            fornana
            
            for doc in fornana:
                tablelabel = Label(self.bodyframe1, text=doc, width=30, height=1, bg="#FFFFFF", anchor='center')
                tablelabel.config(font=("Courier", 10))
                tablelabel.grid(column=3, row=3)

            print(fornana)

        self.search = Entry(self.bodyframe1, textvariable = serts, bg="#FFFFFF")
        self.search.grid(column=3, row=1)
        self.sertsbtn = Button(self.bodyframe1, text = "Search", width = 10, height = 1, command = sertz).grid(column=3, row=2)

        
        self.table1 = Label(self.bodyframe1, text="Person counts", width=30, height=1, bg="#FFFFFF", anchor='center')
        self.table1.grid(column=3,  row=4)

        # self.table2 = Label(self.bodyframe1, text="Person counts", width=30, height=1, bg="#FFFFFF", anchor='center')
        # self.table2.grid(column=4, row=5)

        cid = tk.StringVar()
        persid = tk.Entry(self.bodyframe1, textvariable=cid)
        persid.grid(column=3, row=5)
        persid.configure(state=tk.DISABLED)


def win():
    global records
    records = Tk()
    records.geometry("800x604")
    records.config(bg="#071D20")
    Database(records)    
    records.mainloop()

if __name__ == '__main__':
    win()
