from yolo import model_yolo
from attendance import create_table,adding_date,present,show_table, return_columns
import os
import pandas as pd
import sqlite3
from datetime import date

# The streamlit portion
import cv2
import streamlit as st

st.title("Webcam Live Feed")
submit = st.button("Capture")
run = True
#check = st.button('take attendance')
path = "./"
dir_list = os.listdir(path)
exists = "attendance.db" in dir_list

con = sqlite3.connect("attendance.db")

if not exists:
    create_table()
if str(date.today()).replace("-","") not in return_columns():
    adding_date()



FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Cannot open camera")


while run:
    ret, frame = camera.read()
    if not ret:
        st.write("Not enough frames")
        continue
    if submit:
        run = False
    model_yolo(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

camera.release()
cv2.destroyAllWindows()






df = pd.read_sql_query("SELECT * FROM attendance", con)
st.dataframe(df)

#present()
#show_table()



#model_yolo()
