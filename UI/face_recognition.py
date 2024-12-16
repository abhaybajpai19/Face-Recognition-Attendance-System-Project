from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", 
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top1 = Image.open(
            r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-14 114233.png"
        ).resize((650, 700), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl_top1 = Label(self.root, image=self.photoimg_top1, bg="white")
        f_lbl_top1.place(x=0, y=55, width=650, height=700)

        img_top2 = Image.open(
            r"D:\My Projects\automatic attendance project\images\Screenshot 2024-10-14 112414.png"
        ).resize((950, 700), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        f_lbl_top2 = Label(self.root, image=self.photoimg_top2, bg="white")
        f_lbl_top2.place(x=500, y=55, width=950, height=700)

        b1_1 = Button(f_lbl_top2, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkgreen", fg="black", 
                      command=self.face_recog)
        b1_1.place(x=400, y=590, width=200, height=40)

    # Attendance
    def mark_attendance(self, i, n, r, c):
        with open("abhay.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if (i not in name_list) and (n not in name_list) and (r not in name_list) and (c not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{c},{dtstring},{d1}, Present")

    # Face recognition function
    def face_recog(self):
        def draw_boundary(img, classifier, scalFactor, miniNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalFactor, miniNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Heartbeats7586@", database="face_recognizer")
                my_cursor = conn.cursor()

                # Fetch all data before proceeding with next query
                my_cursor.execute("SELECT name FROM student WHERE student_id =" + str(id))
                n = my_cursor.fetchone()[0] if my_cursor.fetchone() else "Unknown"

                my_cursor.execute("SELECT RollNo FROM student WHERE student_id =" + str(id))
                r = my_cursor.fetchone()[0] if my_cursor.fetchone() else "Unknown"

                my_cursor.execute("SELECT course FROM student WHERE student_id =" + str(id))
                c = my_cursor.fetchone()[0] if my_cursor.fetchone() else "Unknown"

                my_cursor.execute("SELECT student_id FROM student WHERE student_id =" + str(id))
                i = my_cursor.fetchone()[0] if my_cursor.fetchone() else "Unknown"

                # Close the cursor and connection after fetching all the required data
                my_cursor.close()
                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"RollNo: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Course: {c}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, n, r, c)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Person", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("D:/My Projects/automatic attendance project/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("D:/My Projects/automatic attendance project/classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            if cv2.waitKey(1) == 13: 
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
    