import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")

optionals = st.expander('Optional Configurations', True)
selected_fare = optionals.slider(
    "Select the Fare",
    min_value=float(titanic["Fare"].min()),
    max_value=float(titanic["Fare"].max())
)
selected_sex = optionals.radio("Select sex", titanic["Sex"].unique())
selected_class = optionals.radio("Select class", np.sort(titanic["Pclass"].unique()))

titanic_subset = titanic.loc[(titanic['Sex']==selected_sex) & 
                             (titanic['Pclass']==selected_class) & 
                             (titanic['Fare']>=selected_fare),:]

st.dataframe(titanic_subset)

fig, ax = plt.subplots()
ax.hist(titanic_subset['Fare'])
st.header('Histograma del Titanic')
st.pyplot(fig)
st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_subset['Pclass']
x_pos = titanic_subset['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Pclass')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuánto pagaron las clases del titanic')

st.header("Gráfico de barras del titánic")
st.pyplot(fig2)
st.markdown("___")

fig3, ax3 = plt.subplots()

ax3.scatter(titanic_subset['Age'], titanic_subset['Fare'])

ax3.set_xlabel("Edad")

ax3.set_ylabel("Tarifa")

st.header("Grafica de Dispersión del Titanic")

st.pyplot(fig3)

