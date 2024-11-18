import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Streamlit demo")

## Display a simple text
st.write("This is a simple text")

df = pd.DataFrame({'1' : [1 , 2 , 3] , '2' : [10 , 20  ,30]})

st.write("The dataframe")
st.write(df)

chart_data = pd.DataFrame(np.random.randn(20 , 3) , columns = ['a' , 'b' , 'c'])
st.line_chart(chart_data)
