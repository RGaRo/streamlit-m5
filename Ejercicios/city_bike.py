import streamlit as st
import pandas as pd
import numpy as np

st.title("San Francisco Map")
st.header("Using Streamlit and Mapbox")


map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50] + [37.76,-122.4],
    columns=['lat','lon']
)

st.map('citibike-tripdata.csv')