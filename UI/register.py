from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # Store registered user data
        self.registered_users = {}

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"D:\My Projects\automatic attendance project\images\bg_img.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        self.bg1 = Image.open(r"D:\My Projects\automatic attendance project\UI\Login_Form\Images\Screenshot 2024-10-28 220328.png")
        self.bg1 = self.bg1.resize((470, 550), Image.LANCZOS)
        self.photo_bg1 = ImageTk.PhotoImage(self.bg1)

        left_label = Label(self.root, image=self.photo_bg1)
        left_label.place(x=50, y=100, width=470, height=550)

        # Frame
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=520, y=100, width=800, height=550)

        # Title Label
        register_lbl = Label(self.frame, text="Register Here:", font=("times new roman", 20, "bold"), 
                             fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # Registration Form Fields
        self.create_registration_form()

    def create_registration_form(self):
        # First Name
        Label(self.frame, text="First Name", font=("times new roman", 15, "bold"), 
              bg="white").place(x=50, y=100)
        self.first_name_entry = ttk.Entry(self.frame, font=("times new roman", 15))
        self.first_name_entry.place(x=50, y=130, width=250)

        # Last Name
        Label(self.frame, text="Last Name", font=("times new roman", 15, "bold"), 
              bg="white").place(x=370, y=100)
        self.last_name_entry = ttk.Entry(self.frame, font=("times new roman", 15))
        self.last_name_entry.place(x=370, y=130, width=250)

        # Contact Number
        Label(self.frame, text="Contact No:", font=("times new roman", 15, "bold"), 
              bg="white").place(x=50, y=170)
        self.contact_entry = ttk.Entry(self.frame, font=("times new roman", 15))
        self.contact_entry.place(x=50, y=200, width=250)

        # Email
        Label(self.frame, text="Email:", font=("times new roman", 15, "bold"), 
              bg="white").place(x=370, y=170)
        self.email_entry = ttk.Entry(self.frame, font=("times new roman", 15))
        self.email_entry.place(x=370, y=200, width=250)

        # Security Question
        Label(self.frame, text="Select Security Question", font=("times new roman", 15, "bold"), 
              bg="white").place(x=50, y=240)
        self.security_question_combo = ttk.Combobox(self.frame, font=("times new roman", 15), 
                                                    state="readonly")
        self.security_question_combo["values"] = (
            "Select", "Your Birth Place", "Your Pet Name", "Your School Name"
        )
        self.security_question_combo.place(x=50, y=270, width=250)
        self.security_question_combo.current(0)

        # Security Answer
        Label(self.frame, text="Security Answer", font=("times new roman", 15, "bold"), 
              bg="white").place(x=370, y=240)
        self.security_answer_entry = ttk.Entry(self.frame, font=("times new roman", 15))
        self.security_answer_entry.place(x=370, y=270, width=250)

        # Password
        Label(self.frame, text="Password", font=("times new roman", 15, "bold"), 
              bg="white").place(x=50, y=310)
        self.password_entry = ttk.Entry(self.frame, font=("times new roman", 15), show='*')
        self.password_entry.place(x=50, y=340, width=250)

        # Confirm Password
        Label(self.frame, text="Confirm Password", font=("times new roman", 15, "bold"), 
              bg="white").place(x=370, y=310)
        self.confirm_password_entry = ttk.Entry(self.frame, font=("times new roman", 15), show='*')
        self.confirm_password_entry.place(x=370, y=340, width=250)

        # Terms and Conditions Checkbutton
        self.agree_var = IntVar()
        Checkbutton(self.frame, text="I Agree to the Terms and Conditions", variable=self.agree_var,
                    font=("times new roman", 12), onvalue=1, offvalue=0, bg="white").place(x=50, y=380)

        # Register Button
        Button(self.frame, text="Register", font=("times new roman", 15, "bold"), 
               bg="green", fg="white", command=self.register).place(x=50, y=430, width=200, height=40)

        # Login Button
        Button(self.frame, text="Login", font=("times new roman", 15, "bold"), 
               bg="blue", fg="white", command=self.login_screen).place(x=300, y=430, width=200, height=40)

    def register(self):
        if (self.first_name_entry.get() == "" or self.last_name_entry.get() == "" or
                self.contact_entry.get() == "" or self.email_entry.get() == "" or
                self.security_question_combo.get() == "Select" or
                self.security_answer_entry.get() == "" or self.password_entry.get() == "" or
                self.confirm_password_entry.get() == ""):
            messagebox.showerror("Error", "All fields are required!")
        elif self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Passwords do not match!")
        elif self.agree_var.get() == 0:
            messagebox.showerror("Error", "You must agree to the Terms and Conditions!")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO register (first_name, last_name, contact_no, email, security_question, "
                    "security_answer, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.first_name_entry.get(),
                        self.last_name_entry.get(),
                        self.contact_entry.get(),
                        self.email_entry.get(),
                        self.security_question_combo.get(),
                        self.security_answer_entry.get(),
                        self.password_entry.get(),
                    )
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful!")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")

    def login_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
