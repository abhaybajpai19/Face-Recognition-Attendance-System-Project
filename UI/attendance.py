from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog, messagebox

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")
        
        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First Image
        img = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-31 161352.png")
        img = img.resize((500, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg1, bg="white")
        f_lbl1.place(x=20, y=20, width=500, height=200)

        # Second Image
        img1 = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-31 161822.png")
        img1 = img1.resize((500, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg2, bg="white")
        f_lbl2.place(x=540, y=20, width=500, height=200)

        # Third Image (Logo)
        img2 = Image.open(r"D:\My Projects\automatic attendance project\images\images (2).jpg")
        img2 = img2.resize((300, 150), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg3, bg="white")
        f_lbl3.place(x=1060, y=35, width=300, height=150)

        # Background Image
        img3 = Image.open(r"D:\My Projects\automatic attendance project\images\bg_img.jpg")
        img3 = img3.resize((1550, 700), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=200, width=1550, height=700)

        # Title Label
        title_lbl = Label(bg_img, text="Attendance Management System", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=2, y=50, width=1500, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=660, height=580)

        img_left = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-05 210430.png")
        img_left = img_left.resize((650, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(left_frame, image=self.photoimg_left, bg="white")
        f_lbl_left.place(x=5, y=0, width=650, height=100)

        # Frame inside the left frame
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=105, width=650, height=370)

        # Labels and Entry fields side by side

        # Row 1: Attendance ID and Roll No
        attendanceid_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceid_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        rollno_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        rollno_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        rollno_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Row 2: Name and Department
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        department_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Row 3: Time and Date
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Row 4: Attendance Status
        attendance_label = Label(left_inside_frame, text="Attendance:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        attendance_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=18, textvariable=self.var_atten_attendance)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)  # Set default value
        attendance_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Button frame inside the left inside frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=250, width=640, height=50)

        # Buttons
        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 12, "bold"), bg="#5cb85c", fg="white")
        save_btn.grid(row=0, column=0, padx=10, pady=5)

        update_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15, font=("times new roman", 12, "bold"), bg="#0275d8", fg="white")
        update_btn.grid(row=0, column=1, padx=10, pady=5)

        delete_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 12, "bold"), bg="#d9534f", fg="white")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)

        reset_btn = Button(btn_frame, text="Reset", width=15, font=("times new roman", 12, "bold"), bg="#5bc0de", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=5)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Records", font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=780, height=580)

        # Table frame
        tabel_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        tabel_frame.place(x=0, y=40, width=775, height=500)

        # Scroll Bars
        scroll_x = ttk.Scrollbar(tabel_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        
        self.attendance_table = ttk.Treeview(tabel_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), 
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure the table
        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance")

        # Set the width of the columns
        self.attendance_table.column("id", width=100)
        self.attendance_table.column("roll", width=100)
        self.attendance_table.column("name", width=150)
        self.attendance_table.column("department", width=150)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("attendance", width=100)

        self.attendance_table["show"] = "headings"  
        self.attendance_table.pack(fill=BOTH, expand=1)  
        
        # Configure the scrollbars to work with the treeview
        self.attendance_table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.configure(command=self.attendance_table.xview)
        scroll_y.configure(command=self.attendance_table.yview)

        # Bind the double-click event to the Treeview
        self.attendance_table.bind("<ButtonRelease-1>", self.get_cursor)

    def importCsv(self):
        global mydata
        mydata.clear()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        if file_path:
            with open(file_path, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    mydata.append(row)
            self.update_table()

    def exportCsv(self):
        if not mydata:
            messagebox.showerror("No data", "No data to export.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
        if file_path:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(mydata)
            messagebox.showinfo("Success", "Data exported successfully.")

    def update_table(self):
        self.attendance_table.delete(*self.attendance_table.get_children())  
        for row in mydata:
            self.attendance_table.insert("", END, values=row)

    def get_cursor(self, event):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        row = content["values"]

        # Set the values to the entry fields
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
