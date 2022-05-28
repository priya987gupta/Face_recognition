from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2


 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
       #######variables 
        #self.var_s
        self.var_dep = StringVar ( )
        self.var_course = StringVar ( )
        self.var_year = StringVar ( )
        self.var_semester = StringVar ( )
        self.va_std_id = StringVar ( )
        self.var_std_name = StringVar ( )
        self.var_div = StringVar ( )
        self.var_roll = StringVar ( )
        self.var_gender = StringVar ( )
        


#E:\projectms\ImagesAttendance\Bill Gates.jpg
        img=Image.open(r"C:\Users\DELL\Desktop\money\myimages\manage.png")
        img=img.resize((600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        

        img1=Image.open(r"C:\Users\DELL\Desktop\money\myimages\manage.png")
        img1=img1.resize((300,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        img2=Image.open(r"C:\Users\DELL\Desktop\money\myimages\manage.png")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)   
        
        img3=Image.open(r"C:\Users\DELL\Desktop\money\myimages\bg3.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="pink",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1480,height=480)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("lato",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=460)
        
        
         
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="COURSE INFORMATION",font=("lato",12,"bold"))
        current_course_frame.place(x=5,y=1,width=650,height=140)
        
        
        dep_label=Label(current_course_frame,text="Department",font=("lato",12,"bold"),bg="white")
        
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("lato",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer Science", "Information Technology","Electronics", "Electrical","Mechanical","Civil","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  
        
        #course
        course_label=Label(current_course_frame,text="Course",font=("lato",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("lato",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","B.Tech","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label=Label(current_course_frame,text="Year",font=("lato",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("lato",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         #semester
        semester_label=Label(current_course_frame,text="Semester",font=("lato",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("lato",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester1","Semester2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student course
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("lato",12,"bold"))
        class_student_frame.place(x=5,y=150,width=650,height=250)
        
        studentID_label=Label(class_student_frame,text="StudentID: ",font=("lato",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id, width=20,font=("lato",13,"bold") )
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #student name
        studentName_label=Label(class_student_frame,text="Student Name: ",font=("lato",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20,font=("lato",13,"bold") )
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
       
         #class div
        class_div_label=Label(class_student_frame,text="Class Div: ",font=("lato",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)
        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div, width=20,font=("lato",13,"bold") )
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("lato",13,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         #roll no
        RollNo_label=Label(class_student_frame,text="Roll No: ",font=("lato",13,"bold"),bg="white")
        RollNo_label.grid(row=1,column=2,padx=10,sticky=W)
        RollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20,font=("lato",13,"bold") )
        RollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #gender
        gender_label=Label(class_student_frame,text="Gender: ",font=("lato",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)
       # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20,font=("lato",13,"bold") )
       # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
       
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("lato",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=3,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=3,column=1)
        
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=140,width=640,height=80)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        update_btn.grid(row=0,column=1)
        
        
        
        take_photo=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("lato",13,"bold"),bg="pink",fg="white")
        take_photo.grid(row=1,column=0)
        
       # update_photo=Button(btn_frame,text="Update Photo Sample",width=15,font=("lato",13,"bold"),bg="pink",fg="white")
      #  update_photo.grid(row=1,column=1)
        
        
        
        
        
        
        
                  
                  
            
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("lato",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=580)
        
        #search
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("lato",12,"bold"))
        Search_frame.place(x=5,y=0,width=650,height=60)
        
        Search_label=Label(Search_frame,text="Search By:  ",font=("lato",13,"bold"),bg="pink",fg="purple")
        Search_label.grid(row=2,column=0,padx=10,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("lato",13,"bold"),state="readonly",width=20)
        Search_combo["values"]=("Select","Roll_No","Student Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame, width=12,font=("lato",13,"bold") )
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=8,font=("lato",13,"bold"),bg="pink",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)
        
        showALL_btn=Button(Search_frame,text="Show All",width=8,font=("lato",13,"bold"),bg="pink",fg="white")
        showALL_btn.grid(row=0,column=4,padx=4)
        
       # table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=70,width=650,height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","studentname","id","div","roll","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="student_id")
        self.student_table.heading("studentname",text="Name")
        
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Rollno")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="photo_id")
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("studentname",width=100)
        
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=100)
        
        
       
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        #####function declaration##
    def add_data ( self ) :
        if self.var_dep.get ( ) == " Select Department " or self.var_std_name.get ( ) == " " or self.va_std_id.get()==" ":
           messagebox.showerror ( " Error " , " All Fields are required ",parent=self.root )
        else : 
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gupta@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_dep.get(),
                                                                                         self.var_course.get(),
                                                                                         self.var_year.get(),
                                                                                         self.var_semester.get(),
                                                                                         self.va_std_id.get(),
                                                                                         
                                                                                         self.var_std_name.get(),
                                                                                         self.var_div.get(),
                                                                                         self.var_roll.get(),
                                                                                         self.var_gender.get(),
                                                                                         self.var_radio1.get()
                                                                                         
                                                                                         
                                                                                   
                                                                                       )) 
               
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
               
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                
                
                #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Gupta@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
            
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        # get cursor
        
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_radio1.set(data[9])
        
         #upadate function
         
         
    def update_data(self):
        if self.var_dep.get ( ) == " Select Department " or self.var_std_name.get ( ) == " " or self.va_std_id.get()==" ":
            messagebox.showerror ( " Error " , " All Fields are required ",parent=self.root )
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do u want to update student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Gupta@123",database="face_recognizer") 
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Rollno=%s,Gender=%s,photo_id=%s where student_id=%s",(

                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                    #self.va_std_id.get(),
                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                    self.var_div.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_radio1.get(), 
                                                                                                                                                    self.va_std_id.get()                               
                                                                                                                             ))
                else:
                    if  not Upadate:
                        return
                messagebox.showinfo("Success","Students details successfully updated",parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)     
    
                #dataset 
                
    def generate_dataset(self):
        if self.var_dep.get ( ) == " Select Department " or self.var_std_name.get ( ) == " " or self.va_std_id.get()==" ":
            messagebox.showerror ( " Error " , " All Fields are required ",parent=self.root )
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Gupta@123",database="face_recognizer") 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Name=%s,Division=%s,Rollno=%s,Gender=%s,photo_id=%s where student_id=%s",(

                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_semester.get(),
                                                                                                                                            
                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                    self.var_div.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_radio1.get(), 
                                                                                                                                                    self.va_std_id.get()==id+1                               
                                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
              
                
                
                
                 ####load predefined data from open cv####
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0) 
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)   
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                
                messagebox.showinfo("Result","Generatying dataset completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)     

            
             
        
        
                    
                
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()