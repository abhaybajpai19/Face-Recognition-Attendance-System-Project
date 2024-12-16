from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser  # Importing webbrowser module for clickable link


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="About Developer", 
                          font=("times new roman", 35, "bold"), 
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"D:\My Projects\automatic attendance project\images\rear-view-programmer-working-all-night-long.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root, image=self.photoimg_top, bg="white")
        f_lbl_top.place(x=0, y=55, width=1530, height=720)

        # Frame (moved to the right side)
        main_frame = Frame(f_lbl_top, bd=2, bg="white")
        main_frame.place(x=1030, y=55, width=400, height=600)  # Adjust height for better text visibility

        # Image inside frame (adjusted size and position)
        img_developer = Image.open(r"D:\My Projects\automatic attendance project\images\WhatsApp Image 2024-06-18 at 10.14.59 AM (1).jpeg")
        img_developer = img_developer.resize((200, 200), Image.LANCZOS)  # Smaller size for the image
        self.photoimg_developer = ImageTk.PhotoImage(img_developer)
        f_lbl_developer = Label(main_frame, image=self.photoimg_developer, bg="white")
        f_lbl_developer.place(x=100, y=10, width=200, height=200)  # Adjusted position of the image

        # Developer's Info
        dev_info = (
            "Hello! My name is Abhay Bajpai.\n"
            "I'm a final year CSE student at Rama University Kanpur.\n"
            "This is my final year project: a Face Recognition System \nfor attendance management.\n"
            "Technologies Used: Python, Tkinter, OpenCV, MySQL.\n"
            "Contact: babhay128@gmail.com"
        )
        dev_label = Label(main_frame, text=dev_info, font=("times new roman", 10), bg="white", justify="left", wraplength=380)
        dev_label.place(x=10, y=220) 

        # LinkedIn Profile Link
        link_label = Label(main_frame, text="Connect with me on LinkedIn", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        link_label.place(x=10, y=380)

        # Create clickable link
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/abhay-bajpai-0759a3241/"))
        link_label.cursor = "hand2"  # Change cursor to hand

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
