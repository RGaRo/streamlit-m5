import streamlit as st
import pandas as pd

walmart = pd.read_csv('walmart.csv')
st.title("Análisis de Walmart")
st.header("Este pryecto invluye una breve revisión de las ventas de Walmart por país")
st.write("""
Este es un ejercicio hecho para visualizar el comportamiento de ventas por país
""")
sidebar = st.sidebar
sidebar.header('Este sidebar es para presentar los países y estados')

selected_state = sidebar.selectbox("Select State", walmart['State'].unique())
sidebar.write('Selected State:', selected_state)

check = sidebar.checkbox("Click here to share")
if (check):
    sidebar.write("Thanks for share")


st.dataframe(walmart.loc[(walmart['State']==selected_state),:])