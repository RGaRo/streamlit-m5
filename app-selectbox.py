import streamlit as st
import pandas as pd

titanic = pd.read_csv("titanic.csv")
selected_sex = st.selectbox("Select sex", titanic["Sex"].unique())
st.write('Selected Sex:', selected_sex)
st.dataframe(titanic[titanic["Sex"]==selected_sex])