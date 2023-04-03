# Importación de librerías

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Lectura de datos
DATA_URL = ('Employees.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


st.title("Análisis de empleados")
st.write("La siguiente aplicación genera un análisis exploratiorio de los datos de empleados")
seccion_1 = st.expander("Datos considerados en el análisis", True)
seccion_1.header("Datos considerados en el análisis")
seccion_1.write("Los datos mostrados en este apartado son lo que son utilizados para el resto del análisis. \n\
         Por defecto son los primeros 500 registros, pero puede introducir más si usted lo desea, la base de datos origina incluye 7,000 registros")

nrows = seccion_1.number_input('¿Cuántos registros de empleados desea considerar (máximo 7000 registros)?: ', step=1, min_value=500, max_value=7000)
employees = load_data(nrows=nrows)


sidebar = st.sidebar
sidebar.subheader('René Jair Garza Rojas | Aplicación web de ciencia de datos')
sidebar.title('Opciones del análisis')
sidebar.write('El resultado de las selecciones y filtros se verán reflejados en el apartado que indiqué el subheader')
sidebar.subheader('Datos considerados en el análisis')
dataframe_vis = sidebar.checkbox('¿Desea visualizar el dataframe?', help="Si esta casilla está marcada podrá visualizar el dataframe en el apartado de 'Datos considerados en el análisis'")
sidebar.subheader('Filtros')

if (dataframe_vis):
    seccion_1.dataframe(employees)
    seccion_1.write(f'El dataframe cargado tiene {int(employees.shape[0])} filas')
    seccion_1.write(f'El dataframe cargado tiene {employees.shape[1]} columnas')

seccion_2 = st.expander("Buscadores de información", False)
seccion_2.header("Buscadores de información")
seccion_2.write("Este apartado es un buscador de información, la información que usted busque podrá se utilizará como filtro sobre el dataframe original y se mostrará el resultado")
seccion_2.subheader("Buscador por ID de empleado")
seccion_2.write("Se buscarán todos los ID de empleado que contengan lo escrito")
id = seccion_2.text_input('Introduzca el ID que desea buscar: ').upper()

if (id):
    datos = employees[employees['employee_id'].str.upper().str.contains(id)]
    seccion_2.dataframe(datos)
    seccion_2.write(f"Total de ID's de empleados coincidentes: {len(datos)} ")

seccion_2.subheader("Buscador por ciudad de origen")
seccion_2.write("Se buscarán todos los registros por ciudad de origen")
ciudad_origen = seccion_2.text_input('Introduzca la ciudad de origen: ').upper()

if (ciudad_origen):
    datos = employees[employees['hometown'].str.upper().str.contains(ciudad_origen)]
    seccion_2.dataframe(datos)
    seccion_2.write(f"Total de registros coincidentes con la ciudad de origen: {len(datos)} ")

seccion_2.subheader("Buscador por unidad")
seccion_2.write("Se buscarán todos los registros por unidad de trabajo")
seleccion_unidad = seccion_2.radio("Seleccione una unidad", employees["unit"].unique())

if (seleccion_unidad):
    datos = employees[employees['unit']==seleccion_unidad]
    seccion_2.dataframe(datos)
    seccion_2.write(f"Total de registros coincidentes con la unidad: {len(datos)} ")

filtro_nivel_educativo = sidebar.expander('Filtro por nivel educativo', False)
nivel_educativo = filtro_nivel_educativo.selectbox('Seleccione el nivel educativo que desea filtrar:', employees['education_level'].unique(),
                                    help="Este filtro se aplicará al dataframe mostrado en el expander llamado 'Filtro de empleados por nivel educativo'")

seccion_3 = st.expander("Filtro de empleados por nivel educativo", False)
seccion_3.header("Filtro de empleados por nivel educativo")
seccion_3.write("Este apartado muestra el resultado de filtrar por nivel educativo (Sidebar > Apartado: Filtros > Expander Nivel educativo) el dataframe cargado al inicio (obtenido de la sección 'Datos considerados en el análisis' que incluye unicamente una muestra de los empleados)")
if (nivel_educativo):
    datos = employees[employees['education_level']==nivel_educativo]
    seccion_3.write(f"El nivel educativo seleccionado es: {nivel_educativo}")
    seccion_3.dataframe(datos)
    seccion_3.write(f"El total de empleados con el nivel educativo {nivel_educativo} es de {len(datos)} ")

filtro_ciudad = sidebar.expander('Filtro por ciudad', False)
ciudad = filtro_ciudad.selectbox('Seleccione la ciudad que desea filtrar:', employees['hometown'].unique(),
                                    help="Este filtro se aplicará al dataframe mostrado en el expander llamado 'Filtro de empleados por ciudad'")

seccion_4 = st.expander("Filtro de empleados por ciudad", False)
seccion_4.header("Filtro de empleados por ciudad")
seccion_4.write("Este apartado muestra el resultado de filtrar por ciudad (Sidebar > Apartado: Filtros > Ciudad) el dataframe cargado al inicio (obtenido de la sección 'Datos considerados en el análisis' que incluye unicamente una muestra de los empleados)")
if (ciudad):
    datos = employees[employees['hometown']==ciudad]
    seccion_4.write(f"La ciudad seleccionada es: {ciudad}")
    seccion_4.dataframe(datos)
    seccion_4.write(f"El total de empleados de {ciudad} es de {len(datos)} ")

filtro_unidad = sidebar.expander('Filtro por unidad', False)
unidad = filtro_unidad.selectbox('Seleccione la unidad que desea filtrar:', employees['unit'].unique(),
                                    help="Este filtro se aplicará al dataframe mostrado en el expander llamado 'Filtro de empleados por unidad'")

seccion_5 = st.expander("Filtro de empleados por unidad", False)
seccion_5.header("Filtro de empleados por unidad")
seccion_5.write("Este apartado muestra el resultado de filtrar por unidad (Sidebar > Apartado: Filtros > Unidad) el dataframe cargado al inicio (obtenido de la sección 'Datos considerados en el análisis' que incluye unicamente una muestra de los empleados)")
if (unidad):
    datos = employees[employees['unit']==unidad]
    seccion_5.write(f"La unidad seleccionada es: {unidad}")
    seccion_5.dataframe(datos)
    seccion_5.write(f"El total de empleados de {unidad} es de {len(datos)} ")

seccion_6 = st.expander("Histograma de empleados agrupados por edad", False)
seccion_6.header("Histograma de empleados agrupados por edad, tomando como referencia la el dataframe obtenido en la sección 'Datos considerados en el análisis'")
seccion_6.write("Este apartado muestra un histograma de los empleados agrupados por edad, tomando como referencia el dataframe obtenido en la sección 'Datos considerados en el análisis' que incluye solo una muestra de los datos")
cantidad_bins = seccion_6.slider(
    "Selecciona la cantidad de bins",
    min_value=5,
    max_value=20
)
fig1, ax1 = plt.subplots()
ax1.hist(employees['age'], bins=cantidad_bins, color='green')
ax1.set_ylabel("Frecuencia")
ax1.set_xlabel("Edad")
ax1.set_title('Histograma empleados por grupo de edad')
seccion_6.pyplot(fig1)

seccion_7 = st.expander("Empleados por unidad", False)
seccion_7.header("Gráfico de barras para unidad")
seccion_7.write("Este apartado muestra un un gráfico de barras que indica el número de empleados por unidad, tomando como referencia el dataframe obtenido en la sección 'Datos considerados en el análisis' que incluye solo una muestra de los datos")

fig2, ax2 = plt.subplots()
ax2 = sns.barplot(x = employees.value_counts('unit').index ,y = employees.value_counts('unit'))
ax2.set_ylabel("Frecuencia")
ax2.set_xlabel("Unidad")
ax2.set_title('Empleados por unidad')
ax2.tick_params(labelrotation=90)
seccion_7.pyplot(fig2)

seccion_7 = st.expander("Análisis de la tasa de deserción por ciudad", False)
seccion_7.header("Tasa de deserción por ciudad")
seccion_7.write("En este apartado se muestra una gráfica con la tasa de deserción media por ciudad, tomando como referencia el dataframe obtenido en la sección 'Datos considerados en el análisis' que incluye solo una muestra de los datos")

fig3, ax3 = plt.subplots()
datos = employees.groupby('hometown').mean()['attrition_rate']
ax3 = sns.lineplot(x = datos.index ,y = datos)
ax3.set_xlabel("Ciudad")
ax3.set_ylabel("Tasa de deserción promedio")
ax3.set_title('Tasa de deserción promedio por planta')
ax3.tick_params(labelrotation=45)
seccion_7.pyplot(fig3)
seccion_7.write(f"La ciudad con mayor tasa de deserción es: {datos.index[datos==datos.max()][0]}")

seccion_8 = st.expander("Análisis de la tasa de deserción vs edad", False)
seccion_8.header("Tasa de deserción vs edad")
seccion_8.write("En este apartado se muestra una gráfica con la tasa de deserción vs edad, tomando como referencia el dataframe obtenido en la sección 'Datos considerados en el análisis' que incluye solo una muestra de los datos")

fig4, ax4 = plt.subplots()
ax4 = sns.scatterplot(x = employees['age'] ,y = employees['attrition_rate'], color='gray')
ax4.set_xlabel("Edad")
ax4.set_ylabel("Tasa de deserción")
ax4.set_title('Tasa de deserción vs edad')
seccion_8.pyplot(fig4)
seccion_8.write(f"No se aprecia una correlación entre la edad y la tasa de deserción")

seccion_9 = st.expander("Análisis de relación entre tiempo de servicio y tasa de deserción", False)
seccion_9.header("Tasa de deserción vs tiempo de servicio")
seccion_9.write("En este apartado se muestra una gráfica con la tasa de deserción vs el tiempo de servicio, tomando como referencia el dataframe obtenido en la sección 'Datos considerados en el análisis' que incluye solo una muestra de los datos")

fig5, ax5 = plt.subplots()
ax5 = sns.scatterplot(x = employees['time_of_service'] ,y = employees['attrition_rate'], color='green')
ax5.set_xlabel("Tiempo de servicio")
ax5.set_ylabel("Tasa de deserción")
ax5.set_title('Tasa de deserción vs tiempo de servicio')
seccion_9.pyplot(fig5)
seccion_9.write(f"No parece existir una correlación entre el tiempo de servicio y la tasa de deserción, revisemos la correlación que existe entre las variables")

upp_mat = np.triu(employees.dropna().corr())
fig6, ax6 = plt.subplots()
ax6 = sns.heatmap(data=employees.dropna().corr(), cmap="crest", linewidths=0.5, mask=upp_mat)
ax6.set_title('Matríz de correlación')
seccion_9.pyplot(fig6)
seccion_9.write(f"Se puede observar que no existe una correlación entre el tiempo de servicio y la tasa de deserción")