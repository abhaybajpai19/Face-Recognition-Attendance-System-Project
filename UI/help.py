from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser  


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="Help Desk", 
                          font=("times new roman", 35, "bold"), 
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"D:\My Projects\automatic attendance project\images\vecteezy_call-center-vector-icon_27910121-1.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root, image=self.photoimg_top, bg="white")
        f_lbl_top.place(x=0, y=55, width=1530, height=720)

        # Contact Label
        contact_message = Label(f_lbl_top, text="For any queries or questions, contact me at:", 
                                font=("times new roman", 20, "bold"), fg="white", bg="black")
        contact_message.place(x=480, y=230)

        # Clickable Email
        email_label = Label(f_lbl_top, text="babhay128@gmail.com", 
                            font=("times new roman", 20, "bold"), fg="blue", bg="black", cursor="hand2")
        email_label.place(x=580, y=270)
        email_label.bind("<Button-1>", lambda e: webbrowser.open("mailto:babhay128@gmail.com"))


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
