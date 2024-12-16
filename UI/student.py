from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        # Declaring StringVar() variables for all fields
        self.var_dep = StringVar()      # Department
        self.var_course = StringVar()   # Course
        self.var_sem = StringVar()      # Semester
        self.var_id = StringVar()       # ID
        self.var_name = StringVar()     # Name
        self.var_div = StringVar()      # Division
        self.var_roll_no = StringVar()  # Roll No
        self.var_gender = StringVar()   # Gender
        self.var_dob = StringVar()      # Date of Birth
        self.var_email = StringVar()    # Email
        self.var_phone = StringVar()    # Phone
        self.var_address = StringVar()  # Address
        self.var_teacher = StringVar()  # Teacher
        self.var_photo = StringVar()    # Photo
        self.var_year = StringVar()
        # First Image
        img = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-05 122347.png")
        img = img.resize((500, 100), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg, bg="white")
        f_lbl1.place(x=0, y=0, width=500, height=100)

        # Second Image
        img1 = Image.open(r"D:\My Projects\automatic attendance project\images\images (2).jpg")
        img1 = img1.resize((400, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg1, text="Abhay Bajpai", compound="bottom", font=("Arial", 12), bg="white", fg="black")
        f_lbl2.place(x=500, y=0, width=400, height=100)

        # Third Image
        img2 = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-05 123443.png")
        img2 = img2.resize((500, 100), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg2, bg="white")
        f_lbl3.place(x=900, y=0, width=475, height=100)

        # Background Image
        img3 = Image.open(r"D:\My Projects\automatic attendance project\images\bg_img.jpg")
        img3 = img3.resize((1550, 700), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1550, height=700)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=2, y=50, width=1500, height=600) 

        # Left side label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=580)  

        # Left frame image
        img_left = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-05 210430.png")
        img_left = img_left.resize((650, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(left_frame, image=self.photoimg_left, bg="white")
        f_lbl_left.place(x=5, y=0, width=650, height=100)

        # Current Course Frame
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Course Info", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=90, width=650, height=98)

        # Department Label and Combobox
        deep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        deep_label.grid(row=0, column=0, padx=10, pady=5)

        deep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="readonly")
        deep_combo['values'] = ("Select Department", "CSE", "IT", "ECE", "Mechanical")
        deep_combo.current(0)
        deep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Course Label and Combobox
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=1, column=0, padx=10, pady=5)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo['values'] = ("Select Course", "B.Tech", "M.Tech", "Diploma")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=5)

        # Year Label and Combobox
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=0, column=2, padx=10, pady=5)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo['values'] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=5)

        # Semester Label and Combobox
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo['values'] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=5)

        # Class Students Info Frame
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Students Info", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=200, width=720, height=300)

        # Student ID
        studentid_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_id, width=20, font=("times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentname_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_name,width=20, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div ,font=("times new roman", 12, "bold"), width=17, state="readonly")
        div_combo['values'] = ("Select","1","2","3")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=5)

        # Roll Number
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no,width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"), width=17, state="readonly")
        gender_combo['values'] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob,width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address,width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        # Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        # Adding Radio Buttons at the bottom
        # Radio Button for Photo Sample
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take a Photo sample", value="Yes")
        radio_btn1.grid(row=6, column=0)
       
        radio_btn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No Photo sample", value="No")
        radio_btn2.grid(row=6, column=1)
        #button frames
        btn_frame= Frame(class_student_frame , bd=2 , relief=RIDGE , bg= "white")
        btn_frame.place (x =0 ,y= 200, width=715 , height=70)

        save_btn = Button(btn_frame, text= "Save",command=self.add_data, width = 17, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        save_btn.grid(row= 0 , column=0)

        update_btn = Button(btn_frame, text= "Update",command=self.update_data, width = 17, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        update_btn.grid(row= 0 , column=1)

        delete_btn = Button(btn_frame, text= "Delete",command=self.delete_data, width = 17, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        delete_btn.grid(row= 0 , column=2)

        reset_btn = Button(btn_frame, text= "Reset", command=self.reseta_data,width = 17, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        reset_btn.grid(row= 0 , column=3)
        
        btn_frame1= Frame(class_student_frame , bd=2 , relief=RIDGE , bg= "white")
        btn_frame1.place (x =0 ,y= 235, width=715 , height=70)

        take_photo_frame = Button(btn_frame1 ,text= "Take Photo Sample",command=self.genrate_dataset, width = 35, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        take_photo_frame.grid(row= 0, column=0)

        update_photo_frame = Button(btn_frame1 ,text= "Update Photo Sample", width = 35, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        update_photo_frame.grid(row= 0, column=1)
        # Right side label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Other Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=660, height=460)  
        # Right frame image
        img_right = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-06 153148.png")
        img_right = img_right.resize((650, 100), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_left = Label(right_frame, image=self.photoimg_right, bg="white")
        f_lbl_left.place(x=5, y=0, width=650, height=100)
        #searching System
        # Searching Info Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=650, height=70)
        # Inner Frame with 'Search By' label
        search_by_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_by_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        #comboBox
        search_combo = ttk.Combobox(search_frame,font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo['values'] = ("Select", "Roll No:", "Phone No:")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5)
        #entry fieal
        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        #searchBox button
        search_btn = Button(search_frame, text= "Search", width = 10, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        search_btn.grid(row= 0 , column=3, padx=4)
        showall_btn = Button(search_frame, text= "Show All", width = 10, font=("times new roman", 12, "bold"), bg= "white" , fg= "black")
        showall_btn.grid(row= 0 , column=4, padx=4)
        #tabel frame
        tabel_frame =Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        tabel_frame.place(x=5, y=180, width=650, height=250)
        # Scroll bars
        Scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        # Set up Treeview columns
        self.student_tabel = ttk.Treeview(tabel_frame, 
                                        columns=("Dep", "course", "year", "semester", "student_id", "name", "Division", "RollNo", "Gender", "Dob", "Email",  "Phone","Address" ,"Teacher", "PhotoSample"), 
                                        xscrollcommand=Scroll_x.set, 
                                        yscrollcommand=Scroll_y.set)
        # Configure Treeview to show only headings
        self.student_tabel.config(show="headings")
        # Scrollbars configuration
        Scroll_x.config(command=self.student_tabel.xview)
        Scroll_y.config(command=self.student_tabel.yview)
        # Pack Scrollbars
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        # Set the headings for each column
        self.student_tabel.heading("Dep", text="Department")
        self.student_tabel.heading("course", text="Course")
        self.student_tabel.heading("year", text="Year")
        self.student_tabel.heading("semester", text="Semester")
        self.student_tabel.heading("student_id", text="Student ID")
        self.student_tabel.heading("name", text="Name")
        self.student_tabel.heading("Division", text="Division")
        self.student_tabel.heading("RollNo", text="Roll No")
        self.student_tabel.heading("Gender", text="Gender")
        self.student_tabel.heading("Dob", text="Date of Birth")
        self.student_tabel.heading("Email", text="Email")

        self.student_tabel.heading("Phone", text="Phone Number")
        self.student_tabel.heading("Address", text="Address")
        self.student_tabel.heading("Teacher", text="Teacher Name")
        self.student_tabel.heading("PhotoSample", text="Photo")

        self.student_tabel["show"]="headings"
        # Add columns to Treeview with width adjustment
        self.student_tabel.column("Dep", width=100)
        self.student_tabel.column("course", width=100)
        self.student_tabel.column("year", width=100)
        self.student_tabel.column("semester", width=100)
        self.student_tabel.column("student_id", width=150)
        self.student_tabel.column("name", width=100)
        self.student_tabel.column("Division", width=100)
        self.student_tabel.column("RollNo", width=100)
        self.student_tabel.column("Gender", width=100)
        self.student_tabel.column("Dob", width=150)
        self.student_tabel.column("Email", width=100)
        self.student_tabel.column("Phone", width=200)
        self.student_tabel.column("Address", width=150)
        self.student_tabel.column("Teacher", width=100)
        self.student_tabel.column("PhotoSample", width=100)
        # Pack the Treeview into the frame
        self.student_tabel.pack(fill=BOTH, expand=1)
        self.student_tabel.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        # Link Scrollbars to Treeview
        self.student_tabel.configure(yscrollcommand=Scroll_y.set, xscrollcommand=Scroll_x.set)
        Scroll_x.configure(command=self.student_tabel.xview)
        Scroll_y.configure(command=self.student_tabel.yview)
# function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Gave me some values", "All Fields are required" , parent = self.root)
        else:
            try:
                conn =mysql.connector.connect(host= "localHost" , username="root", password="Heartbeats7586@", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)", (

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll_no.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added Successfully", parent= self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
    # #data fetch
    def fetch_data(self): 

        conn = mysql.connector.connect(host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())  
            for i in data:
                self.student_tabel.insert("", END, values=i)  
            conn.commit()
        conn.close()

    def get_cursor(self, event= ""):
        cursor_focus = self.student_tabel.focus()
        content = self.student_tabel.item(cursor_focus)
        data = content["values"]   
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Gave me some values", "All Fields are required" , parent = self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do You want to update this details" , parent= self.root)
                if Update >0:
                    conn =mysql.connector.connect(host= "localHost" , username="root", password="Heartbeats7586@", database="face_recognizer")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update student Set Dep =%s , course =%s , year=%s , Semester =%s, name =%s , Division =%s , RollNo =%s , Gender=%s , Dob =%s , Email =%s , Phone =%s , Address =%s , Teacher=%s , PhotoSample =%s where  student_id = %s", 
                                                                                                                             (




                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll_no.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get() 
                                                                                         ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success", "Details Successfully Updated. ,Thank You!", parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f" Due To{str(es)}", parent=self.root)                
   #delete function
    def delete_data(self):
        if self.var_id.get() == "":  
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do You want to delete the Info", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",  
                        username="root",
                        password="Heartbeats7586@",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id = %s"
                    val = (self.var_id.get(),)  
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted Details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To {str(es)}", parent=self.root)

    #reset function
    def reseta_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll_no.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #Generate data set &  Take Photo Sample
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Gave me some values", "All Fields are required" , parent = self.root)
        else:
            try:
                conn =mysql.connector.connect(host= "localHost" , username="root", password="Heartbeats7586@", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id= 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student Set Dep =%s , course =%s , year=%s , Semester =%s, name =%s , Division =%s , RollNo =%s , Gender=%s , Dob =%s , Email =%s , Phone =%s , Address =%s , Teacher=%s , PhotoSample =%s where  student_id = %s", 
                                                                                                                             (




                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll_no.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_id.get()==id+1
                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reseta_data
                conn.close()
        #load predifned data on face frontal face from open CV
                face_claasifier= cv2.CascadeClassifier("D:/My Projects/automatic attendance project/haarcascade_frontalface_default.xml") 

                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_claasifier.detectMultiScale(gray, 1.3,5) 

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame= cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face=cv2.resize(face_cropped(my_frame), (450, 450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "D:/My Projects/automatic attendance project/Data/" + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path , face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Genrating Data set Completed Successfully. Thank You!")
            except Exception as es:
                messagebox.showerror("Error", f" Due To{str(es)}", parent=self.root)    
    
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

