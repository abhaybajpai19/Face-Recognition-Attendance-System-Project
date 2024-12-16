from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from login import FaceRecognitionSystem  # Corrected the import statement
from register import Register
from datetime import datetime

def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"D:\My Projects\automatic attendance project\images\bg_img.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=530, y=170, width=340, height=420)

        # Adding an image inside the frame
        img1 = Image.open(r"D:\My Projects\automatic attendance project\images\images (2).jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(frame, image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=120, y=5, width=100, height=100)

        # "Student Portal" label
        get_str = Label(frame, text="Student Portal", font=("times new roman", 20, "bold"), bg="white")
        get_str.place(x=80, y=90)

        # "UserName or Email" Label and Entry
        username_label = Label(frame, text="UserName or Email", font=("times new roman", 15, "bold"), bg="white")
        username_label.place(x=100, y=130)

        self.txtuser = Entry(frame, font=("times new roman", 15), bg="#f0f0f0", relief=GROOVE, borderwidth=2)
        self.txtuser.place(x=40, y=160, width=260, height=35)

        # "Password" Label and Entry
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=100, y=205)

        self.txtpass = Entry(frame, font=("times new roman", 15), bg="#f0f0f0", relief=GROOVE, borderwidth=2, show='*')
        self.txtpass.place(x=40, y=230, width=260, height=35)

        # Icon for Username
        img2 = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-24 225044.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(frame, image=self.photoimage2, bg="white", borderwidth=0)
        lblimg2.place(x=75, y=130, width=25, height=25)

        # Icon for Password
        img3 = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-24 225815.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(frame, image=self.photoimage3, bg="white", borderwidth=0)
        lblimg3.place(x=75, y=205, width=25, height=25)

        # Login Button
        loginbtn = Button(
            frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
            fg="white", bg="black", activeforeground="white", activebackground="black",
            cursor="hand2", command=self.login
        )
        loginbtn.place(x=110, y=280, width=120, height=40)

        # Register Button
        registerbtn = Button(
            frame, text="New User Register", font=("times new roman", 15, "bold"), borderwidth=0,
            fg="black", bg="white", activeforeground="white", activebackground="white",
            cursor="hand2", command=self.register_window
        )
        registerbtn.place(x=15, y=350, width=160)

        # Forget Password Button
        passwordbtn = Button(
            frame, text="Forget Password?", font=("times new roman", 15, "bold"), borderwidth=0,
            fg="black", bg="white", activeforeground="white", activebackground="white",
            cursor="hand2", command=self.forget_password_window
        )
        passwordbtn.place(x=10, y=390, width=160)

        # Current time label
        self.time_label = Label(frame, text="", font=("times new roman", 10), bg="white")
        self.time_label.place(x=10, y=5)
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)  # Update every second

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif self.txtuser.get() == "Abhay19" and self.txtpass.get() == "Abhay123":
            messagebox.showinfo("Success", "Welcome to Rama University")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email= %s AND password = %s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Access Only Admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = FaceRecognitionSystem(self.new_window)  # Corrected class name
            conn.commit()
            conn.close()

    def reset_password(self):
        if self.security_question_combo.get() == "Select":
            messagebox.showerror("Error", "Select a security question", parent=self.root2)
        elif self.security_answer_entry.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.new_pass.get() == "":
            messagebox.showerror("Error", "Please enter a new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email = %s AND security_question = %s AND security_answer = %s"
            value = (self.txtuser.get(), self.security_question_combo.get(), self.security_answer_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = "UPDATE register SET password = %s WHERE email = %s"
                value = (self.new_pass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Updated", "Your password has been updated. Please log in with the new password.", parent=self.root2)
                self.root2.destroy()

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email = %s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter a valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                # Security Question
                Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), 
                      bg="white").place(x=50, y=80)
                self.security_question_combo = ttk.Combobox(self.root2, font=("times new roman", 12), state="readonly")
                self.security_question_combo['values'] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
                self.security_question_combo.place(x=50, y=120, width=250)
                self.security_question_combo.current(0)

                # Security Answer Entry
                Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=160)
                self.security_answer_entry = Entry(self.root2, font=("times new roman", 15), bg="lightyellow")
                self.security_answer_entry.place(x=50, y=200, width=250)

                # New Password Entry
                Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
                self.new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightyellow")
                self.new_pass.place(x=50, y=280, width=250)

                # Reset Password Button
                reset_btn = Button(self.root2, text="Reset Password", command=self.reset_password, 
                                   font=("times new roman", 15), bg="black", fg="white")
                reset_btn.place(x=90, y=340, width=160)

if __name__ == "__main__":
    main()
