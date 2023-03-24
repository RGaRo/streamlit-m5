import streamlit as st
import pandas as pd

titanic = pd.read_csv("titanic.csv")
optionals = st.expander("Optional Configurations", True)
fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(titanic["Fare"].min()),
    max_value=float(titanic["Fare"].max())
)

st.dataframe(titanic[titanic["Fare"]>=fare_select])
st.write("The number of passengers with this fare or more are", titanic[titanic["Fare"]>=fare_select].shape[0] )