from gettext import find
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from turtle import shape
from typing import Any
from PIL import Image, ImageTk
import gridfs
import subprocess
import numpy as image_np
import numpy as np
import json
import requests
import base64
from sqlalchemy import create_engine
import cv2
import PySimpleGUI as sg
import os
import sys
from keras.models import load_model
import tensorflow
import pymongo
from pymongo import MongoClient
from importlib.machinery import SourceFileLoader
import pandas as pd
from itertools import combinations
import time
from trackPerson import EuclideanDistTracker
from non_max_suppression import non_max_suppression_fast
import mss as miss
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime


facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

appsIcon = (Image.open("assets/icons/pps.png"))
# path = sys.path.append('C:\Users\Client\OneDrive\Documents\Python projects\CountMe - main\home.py')

cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")

# try:
#     cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
#     cluster.server_info()
# except pymongo.errors.ServerSelectionTimeoutError as err:
#     print(err)

tracker = EuclideanDistTracker()
wht = 1000
confThreshold = 0.3
nmsThreshold = 0.3

# db = cluster["camera"]
# dbb = db["images"]

db = cluster["Reports"]
collection_name = db["Violators"]

fs = gridfs.GridFS(db)
file = "C:/Users/Client/OneDrive/Documents/Python projects/New folder/Capture/1.jpeg"

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

cap = cv2.VideoCapture(0)
output_layers = net.getUnconnectedOutLayersNames()
print(output_layers)


# post = {"_id": 0, "name": "Violators", "score": 1}
# collection_name.insert_one(post)
                
# class Cv:

class Camiira:
    def __init__(self, cammish):
        self.cammish = cammish
        self.cammish_width = 1040
        self.cammish_height = 640
        self.cammish.geometry(f'{self.cammish_width}x{self.cammish_height}+{100}+{30}')
        self.cammish.config(background="#B0AEAE")
        self.cammish.resizable(0,0)
        
        icon = PhotoImage(file='assets/icons/CC2.png')
        self.cammish.iconphoto(True, icon)

         #===========HEADER==========
        self.header = Frame(self.cammish, bg='#015C5A')
        self.header.place(x=277, y=0, width=1070, height=60)

        #==========LOGOUT BUTTON ====================
        self.logout_text = Button(self.cammish, text='Logout', bg='#FFFFFF', font=("", 13, "bold"), fg='black', cursor='hand2', activebackground='#015C5A')
        self.logout_text.place(x=950, y=15)

        #=========NAVBAR===============
        self.sidebar = Frame(self.cammish, bg="#FFFFFF")
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
        self.heading = Label(self.cammish, text='Camera', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        self.heading.place(x=325, y=70)

        # def cammo():

        #     v = main()
        #     v.video = webcam.Box(self.cammish, width=450, height=450)
        #     v.video.show_frames()

        # self.cam= Button(self.cammish, command=cammo)
        # self.cam.place(x=708, y=435)  

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#FFFFFF")
        self.logo_dash.image = photo
        self.logo_dash.place(x=35, y=255)

        self.dash_text = Button(self.sidebar, text='Dashboard', 
            bg='#FFFFFF', font=("", 13, "bold"), 
            bd=0, cursor='hand2', activebackground='#FFFFFF',
            )
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
        
        # def cammo():
            
        #     v = findObjects()
        #     v.video = webcam.Box(self.cammish, width=450, height=450)
        #     v.video.show_frames()
        def cvcapture():
    # cap = cv2.VideoCapture(0)

            starting_time = time.time()
            frame_num = 0
            centroid_dict = dict()
            print(centroid_dict)
            while cap.isOpened():
                centroid_dict = dict()
                
                rects = []
                ret, frame = cap.read()
                frame_num +=1
                height, width, channel = frame.shape
                blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)  
                net.setInput(blob)  
                outs = net.forward(output_layers)

                class_ids = []
                confidences = []
                boxes = []
                
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)
                            boxes.append([x,y,w,h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4) 
                frame = frame.copy()
                
                center = list()
                rects = list()
                font = cv2.FONT_HERSHEY_PLAIN
                if len(indexes) > 0:
                    idf = indexes.flatten()
                        
                    for i in idf:
                        (x,y) = (boxes[i][0], boxes[i][1])
                        (w,h) = (boxes[i][2], boxes[i][3])
                        
                        label = str(classes[class_ids[i]])
                        
                        if label == 'person':
                            center.append([int(x+w/2),int(y+h/2)])
                            # (startX,startY, endX,endY) = (x,y,x+w,y+h)
                            rects.append((x,y,w,h))
                            
                            
                                            
                    boundingboxes = np.array(rects)
                    
                    boxes_ids = tracker.update(rects)
                    for box_id in boxes_ids:
                        (x,y,w,h,id)  = box_id
                        Cx = int((x+x+w)/2)
                        Cy = int((y+y+h)/2)
                        centroid_dict[id] = (Cx,Cy,x,y,w,h)
                    red_zone_dict = dict()
                    
                    for (id1, pt1),(id2,pt2) in combinations(centroid_dict.items(),2):
                        dx,dy  = pt1[0]-pt2[0], pt1[1]-pt2[1]
                        center_pair = [(pt1[0],pt1[1]),(pt2[0],pt2[1])]
                    
                        distance = np.sqrt(dx**2 + dy**2)
                    
                        if distance < 30:
                            if id1 not in red_zone_dict:
                                red_zone_dict[id1] = center_pair
                            if id2 not in red_zone_dict:
                                red_zone_dict[id2] = center_pair

                    

                    for id, box in centroid_dict.items():
                        if id in red_zone_dict:
                            # height, width , channel = frame.shape
                            center_pair = red_zone_dict[id]
                            cv2.rectangle(frame, (box[2], box[3]), (box[4]+box[2],box[5]+box[3]), (0, 0, 255), 2)
                            cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2)
                            
                            #crop

                            current_timestamp = datetime.now().strftime("%Y-%m_%d-%I:%M:%S_%p")
                            
                            # print(filename)
                            # count = 0

                            # while True:
                            #         time.sleep(1)
                            #         ret, frame = cap.read(cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2))
                            #         faces = facedetect.detectMultiScale(frame, 1.3, 5)  
                            #         for x,y,w,h in faces:
                            #             filenamechuchu = "violator_" + str(current_timestamp)
                            #             count = count + 1
                            #             name='./images/'+ str(filenamechuchu) + '.jpg'
                            #             print("creating images ...." + name)
                            #             # cv2.imwrite(name, frame[y:y+h,x:x+w])
                            #             # cv2.rectangle(frame,(x,y), (x+w, y+w),(0,0,255), 2)
                            #             cv2.rectangle(frame, (box[2], box[3]), (box[4]+box[2],box[5]+box[3]), (0, 0, 255), 2)

                            #             with open(file, 'rb') as f:
                            #                 contents = f.read()
                                        
                            #             fs.put(contents, filename="file")   
                                        
                            #             if count == 1 :   
                            #                 return
                                    
                            
                        else:
                            cv2.rectangle(frame, (box[2], box[3]), (box[4]+box[2],box[5]+box[3]), (0, 255,0 ), 2)
                        
                        height, width , channel = frame.shape
                        sub_img = frame[0:int(height/10),0:int(width)]
                        
                        black_rect = np.ones(sub_img.shape, dtype=np.uint8)*0
                        
                        res = cv2.addWeighted(sub_img,0.99,black_rect,0.20,0) 
                        FONT = cv2.FONT_HERSHEY_SIMPLEX
                        FONT_SCALE = 0.8
                        FONT_THICKNESS = 2
                        lable_color = (255, 255, 255)
                        lable = "Persons:{}".format(len(center))
                        lable_dimension = cv2.getTextSize(lable,FONT ,FONT_SCALE,FONT_THICKNESS)[0]
                        textX = int((res.shape[1] - lable_dimension[0]) / 2)
                        textY = int((res.shape[0] + lable_dimension[1]) / 2)
                        lable1 = cv2.putText(res, lable, (textX,textY), FONT, FONT_SCALE, lable_color, FONT_THICKNESS)
                        cv2.putText(res, lable, (textX,textY), FONT, FONT_SCALE, lable_color, FONT_THICKNESS)
                        cv2.putText(res, "Violation:{}".format(len(red_zone_dict)), (0,textY+5+2), FONT,0.8, lable_color,2)
                        #cv2.putText(res, "Persons:{}".format(len(center)), (0,textY+5+2), FONT,0.5, lable_color,1)
                        #cv2.putText(res, "Violation:{}".format(len(red_zone_dict)), (0,textX+20+10), FONT,0.5, lable_color,1)


                        frame[0:int(height/10),0:int(width)] = res
                        elapsed_time = time.time() - starting_time
                        fps = frame_num/elapsed_time

                # dateyear = datetime.now().strftime("%A, %B %d, %Y")
                # current_timestamp = datetime.now().strftime("%Y-%m_%d-%I:%M:%S_%p")
                # post = ({"Date": dateyear,"Name": 'People', "Number": lable, "Time": current_timestamp})
                # collection_name.insert_one(post)
                # collection_name.update_one(
                #     {"Date": dateyear},
                #     {"$set": 
                #         {"Number": lable}
                #         }
                #         )        

                        cv2.imshow('CountMe', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()       
        
        v = cvcapture()
        self.cam = Button(self.cammish, text='camera')
        self.cam['command'] = v
        self.cam.place(x=708, y=435) 
            
def win():
    cammish = Tk()
    Camiira(cammish) 
    cammish.mainloop()



if __name__ == '__main__':
    win()
