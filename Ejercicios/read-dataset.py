import streamlit as st
import pandas as pd

names_data = pd.read_csv('/workspaces/streamlit-m5/dataset.csv')
st.title('Dataframe en Streamlite')
st.dataframe(names_data)