import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Welcome: {name}")

age = st.slider("Select your age" , 0 , 100 )

st.write(f"Your age is {age} ")

options = ["Python" , "C++" , "Java"]
choice = st.selectbox("Choose you programming language:" , options)
st.write(f"You have selected: {choice}")

df = pd.DataFrame({'1' : [1 , 2 , 3] , '2' : [10 , 20  ,30]})
st.write(df)

upload_file = st.file_uploader("Choose a csv file" , type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)