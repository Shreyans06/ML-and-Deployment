import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data , columns = iris.feature_names)
    df['species'] = iris.target
    return df , iris.target_names

df , target_names = load_data()
model = RandomForestClassifier()
model.fit(df.iloc[:,:-1] , df['species'])

st.sidebar.title("Input Features")
sepal_len = st.sidebar.slider("Sepal length" , float(0) , float(10) , step= 0.5)
sepal_width = st.sidebar.slider("Sepal Width" , float(0), float(10) , step= 0.5)
petal_len = st.sidebar.slider("Petal length" , float(0), float(10), step= 0.5)
petal_width = st.sidebar.slider("Petal Width" , float(0), float(10), step= 0.5)

input_data = [[sepal_len , sepal_width , petal_len , petal_width]]

prediction = model.predict(input_data)

st.write(f"The predicted species is: {target_names[prediction[0]]}")
