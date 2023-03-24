import streamlit as st
import pandas as pd
import numpy as np

titanic = pd.read_csv("titanic.csv")
selected_class = st.radio("Select Class", np.sort(titanic["Pclass"].unique()))
st.write("Selected class:", selected_class)

st.dataframe(titanic[titanic["Pclass"]==selected_class])
