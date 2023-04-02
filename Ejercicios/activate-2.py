import streamlit as st
import pandas as pd

walmart = pd.read_csv('walmart.csv')
st.title("Análisis de Walmart")
st.header("Este pryecto invluye una breve revisión de las ventas de Walmart por país")
st.write("""
Este es un ejercicio hecho para visualizar el comportamiento de ventas por país
""")
selected_shipmode = st.radio("Selected Ship Mode", walmart['Ship Mode'].unique())
st.write("Selected Ship Mode", selected_shipmode)

selected_category = st.selectbox("Selected Category", walmart['Category'].unique())
st.write("Selected Category", selected_category)

discount = st.slider(
    "Select the discount",
    min_value=float(walmart["Discount"].min()),
    max_value=float(walmart["Discount"].max())
)

st.dataframe(walmart.loc[(walmart["Category"]==selected_category) & 
                         (walmart["Ship Mode"]==selected_shipmode) & 
                         (walmart['Discount']>=discount) ,:])