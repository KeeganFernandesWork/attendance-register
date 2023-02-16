from yolo import model_yolo
from attendance import create_table,adding_date,present,show_table, return_columns
import os
import pandas as pd
import sqlite3
from datetime import date

# The streamlit portion
import cv2
import streamlit as st

st.title("Attendance App")
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


st.image("hello.jpg")
image = cv2.imread("hello.jpg")
names = []
if submit:
    a = model_yolo(image)
    for i in a:
        names.append(i[0])
    present(names)
    st.image("./runs/detect/predict/image0.jpg")
st.write(names)
    




df = pd.read_sql_query("SELECT * FROM attendance", con)
st.dataframe(df)

present()
#show_table()



#model_yolo()
