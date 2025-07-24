import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Linear Regression with Streamlit")

data = pd.read_csv("data.csv")

st.write(data)

x = data[['Hours_Studied']]
y = data['Marks_Scored']

model = LinearRegression()
model.fit(x, y)

hours = st.number_input("Enter Hours Studied:", 1.0, 10.0, step=0.5)
prediction = model.predict([[hours]])
st.write("Predicted Marks:", prediction[0])