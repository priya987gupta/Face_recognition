from pydoc import Helper
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
from attendance import Attendence
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        img=Image.open(r"C:\Users\DELL\Desktop\money\myimages\girl.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        img1=Image.open(r"C:\Users\DELL\Desktop\money\myimages\girl.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=570,height=130)
        
        
        img2=Image.open(r"C:\Users\DELL\Desktop\money\myimages\girl.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=570,height=130)
        
        img3=Image.open(r"C:\Users\DELL\Desktop\money\myimages\blue.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="pink",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        img4=Image.open(r"C:\Users\DELL\Desktop\money\myimages\student_details.png")
        img4=img4.resize((220,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
    
    
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.Student_details)
        b1.place(x=100,y=100,width=220,height=180)
        
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.Student_details,font=("times new roman",15,"bold"),bg="pink",fg="white")
        b1_1.place(x=100,y=260,width=220,height=30)
        
        #detect face
        
        img5=Image.open(r"C:\Users\DELL\Desktop\money\myimages\face_detector.webp")
        img5=img5.resize((220,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=220,height=180)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="pink",fg="white")
        b1_1.place(x=400,y=260,width=220,height=30)
        
        #attendence
        img6=Image.open(r"C:\Users\DELL\Desktop\money\myimages\attendance.png")
        img6=img6.resize((220,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b1.place(x=700,y=100,width=220,height=180)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence,font=("times new roman",15,"bold"),bg="pink",fg="white")
        b1_1.place(x=700,y=260,width=220,height=30)
        
        #help desk
        img7=Image.open(r"C:\Users\DELL\Desktop\money\myimages\help_desk.png")
        img7=img7.resize((220,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk)
        b1.place(x=1000,y=100,width=220,height=180)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="pink",fg="white")
        b1_1.place(x=1000,y=260,width=220,height=30)
        
        #train model
        img8=Image.open(r"C:\Users\DELL\Desktop\money\myimages\train_data.webp")
        img8=img8.resize((220,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=320,width=220,height=180)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="pink",fg="white")
        b1_1.place(x=100,y=480,width=220,height=30)
        


    def open_img(self):
        os.startfile("data")    
        #function button
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)    
        
    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)    
      
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Helper(self.new_window)        
        
        
        

        
        
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()