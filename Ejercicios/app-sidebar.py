import streamlit as st
st.title('Mi aplicación con Sidebar')
sidebar = st.sidebar
sidebar.title('Esta es la barra lateral')
sidebar.write('Aquí van los elementos de entrada')

st.header('Información sobre el conjunto de datos')
st.header('Descripción de los datos')

st.write("""
Este es un simple ejemplo de una app para predecir
¡Esta app predice mis datos!
""")