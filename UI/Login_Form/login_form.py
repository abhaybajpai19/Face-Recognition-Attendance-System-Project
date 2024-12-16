from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from login import Face_recognition_system 

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

        # "RUM No" Label and Entry
        username_label = Label(frame, text="RUM No:", font=("times new roman", 15, "bold"), bg="white")
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
    cursor="hand2", command=self.rigester_window  # Change this
)
        registerbtn.place(x=15, y=350, width=160)

        # Forget Password Button
        passwordbtn = Button(
            frame, text="Forget Password?", font=("times new roman", 15, "bold"), borderwidth=0,
            fg="black", bg="white", activeforeground="white", activebackground="white",
            cursor="hand2", command=self.register_action
        )
        passwordbtn.place(x=10, y=390, width=160)
    
    def rigester_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif self.txtuser.get() == "Abhay19" and self.txtpass.get() == "Abhay123":
            messagebox.showinfo("Success", "Welcome to Rama University")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email =%s and password = %s" , (
                                                                                        self.var_email.get(),
                                                                                        self.var_pass.get()
                                                                                            ))
            
            row= my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main= messagebox.askyesno("YessNo", "Access Only Admin")
                if open_main >0:
                    self.new_window= Toplevel(self.new_window)
                    self.app= Face_recognition_system(self.new_window)

    def register_action(self):
        self.root.destroy()  # Close login window
        new_window = Toplevel(self.root)  # Create a new window for registration
        Register(new_window)

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

        # Register Button
        register_button = Button(self.frame, text="Register", font=("times new roman", 15, "bold"), 
                                 bg="green", fg="white", command=self.register)
        register_button.place(x=50, y=390, width=150, height=40)

        # Back Button
        back_button = Button(self.frame, text="Back", font=("times new roman", 15, "bold"), 
                             bg="red", fg="white", command=self.go_back)
        back_button.place(x=370, y=390, width=150, height=40)


    def register(self):
        if self.first_name_entry.get() == "" or self.last_name_entry.get() == "" or \
           self.contact_entry.get() == "" or self.email_entry.get() == "" or \
           self.security_question_combo.get() == "Select" or self.security_answer_entry.get() == "" or \
           self.password_entry.get() == "" or self.confirm_password_entry.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
            return

        if self.password_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Database Connection
        try:
            with mysql.connector.connect(
                host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer"
            ) as conn:
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
                messagebox.showinfo("Success", "Registration Successful!")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def go_back(self):
        self.root.destroy()  # Close registration window
        new_window = Toplevel(self.root)  # Create a new window for login
        main()

if __name__ == "__main__":
    main()
