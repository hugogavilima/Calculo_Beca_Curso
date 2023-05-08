import streamlit as st
import pandas as pd
from funciones import*

st.set_page_config(layout="wide", page_title="Cálculo Porcentaje de Beca")
st.write("# Cálculo Porcentaje de Beca")
st.write(
    "La aplicación permite consultar el porcentaje de beca de cada estudiante."
    )


a, b, c, d, f  = st.columns(5)

with c:
    cedula = st.text_input("Favor ingrese la cédula del estudiante.")
    tabla = buscar(cedula)
    
    
st.write(tabla)
    


    
    


