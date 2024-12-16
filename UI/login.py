from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#d0e7f9")

        # First Image
        img = Image.open(r"D:\My Projects\automatic attendance project\images\Rama University1680090661_upload_logo.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg, bg="#d0e7f9")
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"D:\My Projects\automatic attendance project\images\automaticattendancelogo.jpg.jpg")
        img1 = img1.resize((400, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl2 = Label(self.root, image=self.photoimg1, text="Abhay Bajpai", compound="bottom", font=("Arial", 12), bg="#d0e7f9", fg="black")
        f_lbl2.place(x=500, y=0, width=400, height=120)

        # Third Image
        img2 = Image.open(r"D:\My Projects\automatic attendance project\images\images (1).jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl3 = Label(self.root, image=self.photoimg2, bg="#d0e7f9")
        f_lbl3.place(x=900, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(r"D:\My Projects\automatic attendance project\images\bg_img.jpg")
        img3 = img3.resize((1550, 670), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3, bg="#d0e7f9")
        bg_img.place(x=0, y=130, width=1550, height=670)

        title_lbl = Label(bg_img, text="Face Recognition System Software By Abhay Bajpai", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Button size
        button_size = 180

        # Student Button
        img4 = Image.open(r"D:\My Projects\automatic attendance project\images\button.png")
        img4 = img4.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, command=self.students_details, cursor="hand2")
        b1.place(x=200, y=70, width=button_size, height=button_size)
        b1_1 = Button(bg_img, text="Students Details", command=self.students_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=200, y=250, width=button_size, height=40)

        # Detect Face Button
        img5 = Image.open(r"D:\My Projects\automatic attendance project\images\face_detector.png")
        img5 = img5.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, command=self.face_data, cursor="hand2")
        b2.place(x=500, y=70, width=button_size, height=button_size)
        b2_1 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b2_1.place(x=500, y=250, width=button_size, height=40)

        # Attendance Button
        img6 = Image.open(r"D:\My Projects\automatic attendance project\images\attendance.png")
        img6 = img6.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, command=self.attendance_data, cursor="hand2")
        b3.place(x=800, y=70, width=button_size, height=button_size)
        b3_1 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b3_1.place(x=800, y=250, width=button_size, height=40)

        # Help Button
        img7 = Image.open(r"D:\My Projects\automatic attendance project\images\help.png")
        img7 = img7.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b4.place(x=1100, y=70, width=button_size, height=button_size)
        b4_1 = Button(bg_img, text="Help?", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b4_1.place(x=1100, y=250, width=button_size, height=40)

        # Train Button
        img8 = Image.open(r"D:\My Projects\automatic attendance project\images\traindata.png")
        img8 = img8.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, command=self.train_data, cursor="hand2")
        b5.place(x=200, y=320, width=button_size, height=button_size)
        b5_1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b5_1.place(x=200, y=500, width=button_size, height=40)

        # Photos Button
        img9 = Image.open(r"D:\My Projects\automatic attendance project\images\photos.png")
        img9 = img9.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
        b6.place(x=500, y=320, width=button_size, height=button_size)
        b6_1 = Button(bg_img, text="Photos", command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b6_1.place(x=500, y=500, width=button_size, height=40)

        # Developer Button
        img10 = Image.open(r"D:\My Projects\automatic attendance project\images\devloper.png")
        img10 = img10.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b7.place(x=800, y=320, width=button_size, height=button_size)
        b7_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b7_1.place(x=800, y=500, width=button_size, height=40)

        # Exit Button
        img11 = Image.open(r"D:\My Projects\automatic attendance project\images\exit.png")
        img11 = img11.resize((button_size, button_size), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b8.place(x=1100, y=320, width=button_size, height=button_size)
        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b8_1.place(x=1100, y=500, width=button_size, height=40)

    # Functions for each button action
    def open_img(self):
        os.startfile(r"D:\My Projects\automatic attendance project\Data")  

    def iExit(self):
        self.iExit = mb.askyesno("Exit", "Are you sure you want to exit?")
        if self.iExit:
            self.root.destroy()

    def students_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
