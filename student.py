from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")




        #---------------variables--------------------
        self.var_dep = StringVar()
        self.var_course= StringVar()
        self.var_year = StringVar()
        self.var_semster=StringVar()
        self.var_std_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_std_name=StringVar()


        
        # First image

        img=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)


        #Second image


        img1=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\Faces.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        # Third image

        img2=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)


        # bg image
        img3=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)


        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)



        img_left=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=720,height=155)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



        # Semester

        semester_label=Label(current_course_frame,text="Semister",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semster,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=730,height=300)


        # student_id
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # student_name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)


        # Roll No.
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        # Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)


        # DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # phone_no
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # teacher
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn = Button(btn_frame,text="Save",command=self.adddata,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        reset_btn.grid(row=0,column=3)


        # 2 button frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn = Button(btn_frame1,text="Take Photo sample",command=self.generate_dataset,width=39,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo sample",width=39,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        update_photo_btn.grid(row=0,column=1)







        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)


        img_right=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img_right=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No.","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn = Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        showAll_btn.grid(row=0,column=4,padx=3)

        # table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=685,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")

        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)

        self.student_table.column("year",width=100)
        
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
         




        #----function declaration ---------------------------


    def adddata(self):
        if self.var_dep.get()=="Select Department " or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
                my_cursor=conn.cursor()
               
                
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                (

                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semster.get(),
                                                                                        self.var_std_id.get(),
                                                                                        
                                                                                        self.var_std_name.get() ,
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get(),
                                                                                     
                                                                                        
                                                                                    )
                                                                                   )
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Succes","Student details Added",parent=self.root)
            except Exception as e:
                print(e)
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)




#----------------------------fetch data_------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()
    
        if len(data) != 0:
            print(data)
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




#-----------------------------get cursor-------------------
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content_table= self.student_table.item(cursor_focus)
        data = content_table["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semster.set(data[3]),
        self.var_std_id.set(data[4]),
        
        self.var_std_name.set(data[5]) ,
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
                 


                  #-------------------update function-----------------
    def update_data(self):
        if self.var_dep.get()=="Select Department " or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               Update = messagebox.askyesno("Update","Do you want update the data",parent=self.root)
               print("itcomes here")
               if Update > 0:
                   conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semster=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semster.get(),
                                                                                        self.var_std_name.get() ,
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_std_id.get(),
                                                                                    ))
               else:
                    if not Update:
                        return
               messagebox.showinfo("Succes","Student details update successfully",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
            except  Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

    #------- delete function--------------------------

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to confirm",parent=self.root)

                if delete >0:
                    conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
                    my_cursor=conn.cursor()

                    sql = "delete from student where Student_id = %s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student data deleted",parent=self.root)
                self.reset_data()
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)



    #----------------reset function---------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semster.set("Select Semster")
        
        self.var_std_id.set("")
        self.var_std_name.set("") 
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


   # ------------------------generate dataset or take photo sample-----------------------------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department " or self.var_std_name.get() == "" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semster=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semster.get(),
                                                                                        self.var_std_name.get() ,
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_std_id.get()==id+1,
                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                face_classifer = cv2.CascadeClassifier(r"C:\Users\Noushad\Documents\project\minorprojectvs\haarcascade_frontalface_default.xml")
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret , my_frame = cap.read()
                    gray = cv2.cvtColor(my_frame,cv2.COLOR_BGR2GRAY)
                    faces = face_classifer.detectMultiScale(gray,1.3,5)
                    
                    for (x,y,w,h) in faces:
                        cv2.rectangle(my_frame,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.imshow("img",my_frame)
                    if faces is not None:
                        img_id +=1 
                    
                        for (x,y,w,h) in faces:
                            
                            face_crop = my_frame[y:y+h,x:x+w]
                            cv2.imshow("face croped",face_crop)
                            face = cv2.resize(face_crop,(450,450))
                            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpeg"
                          
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                            cv2.imshow("Cropped face",face)
                            
                    if cv2.waitKey(1) == 13 or int(img_id)==300:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data sets Completed",parent=self.root)
            except  Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)


        
                
            




if __name__ == "__main__":
    root = Tk()
    obj= Student(root)
    root.mainloop()
