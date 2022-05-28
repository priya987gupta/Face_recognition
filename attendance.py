from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import os 
import csv
from tkinter import filedialog



mydata=[] 
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       
        #=============variables+++++++++++++++++++++
        
        
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        #first image
        img1=Image.open(r"C:\Users\DELL\Desktop\money\myimages\at.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        
        #second image
        
        img2=Image.open(r"C:\Users\DELL\Desktop\money\myimages\at.jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200) 
        
        img3=Image.open(r"C:\Users\DELL\Desktop\money\myimages\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="pink",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1380,height=450)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("lato",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=4,width=727,height=600)
        
        #lable entry
        attendenceID_label=Label(left_inside_frame,text="Attendence ID: ",font=("lato",13,"bold"),bg="white")
        attendenceID_label.grid(row=0,column=0)
        
        
        attendenceID_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_id,font=("lato",13,"bold") )
        attendenceID_entry.grid(row=0,column=1,pady=8)
        
        #name
        rollLabel_label=Label(left_inside_frame,text="Roll No: ",font=("lato",13,"bold"),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=4,pady=8)
        
        
        atten_roll=ttk.Entry(left_inside_frame, width=16,textvariable=self.var_attend_name,font=("lato",13,"bold") )
        atten_roll.grid(row=0,column=3,pady=8)
        
        # date
        nameLabel_label=Label(left_inside_frame,text="Name: ",font=("lato",13,"bold"),bg="white")
        nameLabel_label.grid(row=1,column=0)
        
        
        atten_name=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_date,font=("lato",13,"bold") )
        atten_name.grid(row=1,column=1,pady=8)
        
        #department
        depLabel_label=Label(left_inside_frame,text="Department: ",font=("lato",13,"bold"),bg="white")
        depLabel_label.grid(row=1,column=2)
        
        
        atten_dep=ttk.Entry(left_inside_frame, width=16,textvariable=self.var_attend_dep,font=("lato",13,"bold") )
        atten_dep.grid(row=1,column=3,pady=8)
        
        #time
        timeLabel_label=Label(left_inside_frame,text="Time: ",font=("lato",13,"bold"),bg="white")
        timeLabel_label.grid(row=2,column=0)
        
        
        atten_time=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_time,font=("lato",13,"bold") )
        atten_time.grid(row=2,column=1,pady=8)
        
        #date
        dateLabel_label=Label(left_inside_frame,text="Date: ",font=("lato",13,"bold"),bg="white")
        dateLabel_label.grid(row=2,column=2)
        
        
        atten_date=ttk.Entry(left_inside_frame, width=16,textvariable=self.var_attend_date,font=("lato",13,"bold") )
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendence
        
        attendenceLabel_label=Label(left_inside_frame,text="Attendence Status: ",font=("lato",13,"bold"),bg="white")
        attendenceLabel_label.grid(row=3,column=0)
        
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("lato",13,"bold"),state="readonly",width=20)
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=640,height=80)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCSV,width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        update_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text="Update",width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        update_btn.grid(row=0,column=2)
        
    
        
       
        
        
        
        
        
        
         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence Details",font=("lato",12,"bold"))
        Right_frame.place(x=750,y=10,width=750,height=800)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=727,height=600)
        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        
        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll No")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
        
        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
        
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        
        
    # fetch data
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    ###import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("ALL File",".*")),parent=self.root)
        with open(fln) as myfile:
            
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                
                mydata.append(i)
            
            self.fetchData(mydata)
        
      #####export csv
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data","No Data found to export",parent=self.root) 
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("ALL File",".*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                     exp_write=csv.writer(myfile,delimiter=",")
                     for i in mydata:
                             exp_write.writerow(i)
                     messagebox.showinfo("Data Exported Successfully")       
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

    def get_cursor(self,event=""):
            cursor_row=self.AttendenceReportTable.focus()
            content=self.AttendenceReportTable.item(cursor_row)
            row=content['values']
            self.var_attend_id.set(row[0])
            self.var_attend_roll.set(row[1])
            self.var_attend_name.set(row[2])
            self.var_attend_dep.set(row[3])
            self.var_attend_time.set(row[4])
            self.var_attend_date.set(row[5])
            self.var_attend_attendance.set(row[6])

    #def reset_data(self):  

        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()