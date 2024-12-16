from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="Train Data Set", 
                          font=("times new roman", 35, "bold"), 
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-12 151252.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root, image=self.photoimg_top, bg="white")
        f_lbl_top.place(x=0, y=55, width=1530, height=280)

        # Button (Adjusted to avoid overlap)
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", 
                      font=("times new roman", 30, "bold"), 
                      bg="blue", fg="black")
        b1_1.place(x=0, y=340, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-12 151900.png")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom, bg="white")
        f_lbl_bottom.place(x=0, y=400, width=1530, height=300)

    def train_classifier(self):
        data_dir = r"D:\My Projects\automatic attendance project\Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for images in path:
            img = Image.open(images).convert('L')  # For grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(images)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)  # Small delay

        ids = np.array(ids)

        # Train the classifier and save the model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training DataSets Completed !!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
