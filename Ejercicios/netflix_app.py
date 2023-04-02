import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import codecs

columns_show = ['gross', 'name','director', 'rating']

@st.cache
def load_data(nrows):
    doc = codecs.open('fuentes/movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data[columns_show]

@st.cache
def load_data_byname(name):
    doc = codecs.open('fuentes/movies.csv','rU','latin1')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_byname = data[data['name'].str.upper().str.contains(name)]
    return filtered_data_byname[columns_show]

@st.cache
def load_data_bydirector(director):
    doc = codecs.open('fuentes/movies.csv','rU','latin1')
    data = pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    filtered_data_bydirector = data[ data['director'] == director ]
    return filtered_data_bydirector[columns_show]


df_movies = load_data(500)

# crear title de la app web
st.title("Netflix stats")

sidebar = st.sidebar
sidebar.title("Filtros disponibles")

agree = sidebar.checkbox("Todas las peliculas?")
if agree:
    df_movies = load_data(500)
    
myname = sidebar.text_input("Titulo del filme:")
if (sidebar.button('Buscar Filmes')):
    if (myname):            
        df_movies = load_data_byname(myname.upper())
        count_row = df_movies.shape[0]

# Es un box de selección
selected_dir  = sidebar.selectbox('Seleccionar Director', df_movies['director'].unique())
btnFilterbyDirector = sidebar.button('Buscar director')

if (btnFilterbyDirector):
    df_movies = load_data_bydirector( selected_dir)

st.write(f"Total names : {df_movies.shape[0]}")
st.dataframe(df_movies)